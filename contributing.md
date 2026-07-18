# Contributing to Zero2Shell-50 🚀

First off, thank you for considering contributing to Zero2Shell-50! This project aims to build the most comprehensive, modern collection of containerized RCE labs for security education. **We've built 15 labs — we need your help to reach 50.**

Every contribution helps make cybersecurity training more accessible.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [What We're Looking For](#what-were-looking-for)
- [Quality Requirements](#quality-requirements)
- [Lab Architecture Standards](#lab-architecture-standards)
- [Pull Request Process](#pull-request-process)
- [Quality Checklist](#-quality-checklist)
- [Current Lab Coverage](#-current-lab-coverage)
- [Questions?](#questions)

---

## Code of Conduct

This project and everyone participating in it is governed by the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct.html). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

---

## What We're Looking For

### 🎯 The "Zero2Shell" Mandate

**Every lab must result in Remote Code Execution (RCE) or system-level command injection.** This project is called Zero2Shell for a reason — if it doesn't end with a shell, it doesn't belong here.

### ✅ High-Priority Contributions

- **Modern CVEs (2024-2026):** Focused on recent, actively exploited vulnerabilities
- **Unauthenticated RCE:** The holy grail — no credentials required
- **Authenticated RCE:** Admin-to-shell chains are acceptable if well-documented
- **Framework-Level Flaws:** Vulnerabilities in popular frameworks, not custom code
- **Logic-Based RCE:** Deserialization, injection, prototype pollution — not memory corruption

### 🔥 Urgently Needed: Java Labs

We have only 1 unexploited Java lab (Spring Cloud Gateway SPEL). We need help with:
- **ActiveMQ Deserialization** (CVE-2023-46604)
- **JBoss/WildFly RCE**
- **Jenkins Pipeline RCE**
- **WebLogic T3 Deserialization**

### ❌ What We Don't Accept

- **Information Disclosure:** Reading files without code execution
- **SSRF Alone:** Unless it chains to RCE
- **XSS/CSRF:** Client-side only, no shell
- **Denial of Service:** Crashing services without code execution
- **Local Privilege Escalation:** Unless chained from initial RCE
- **Memory Corruption:** Buffer overflows, heap sprays, kernel exploits
- **SQL Injection:** Unless it leads to `xp_cmdshell` or equivalent OS execution

### 🎯 Vulnerability Categories (RCE-Only)

| Category | RCE Mechanism | CVSS Range | Priority |
|----------|--------------|------------|----------|
| **Insecure Deserialization** | POP gadget chains → `Runtime.exec()` / `system()` | 8.0-10.0 | 🔴 High |
| **OS Command Injection** | Unsanitized input → `subprocess.run(shell=True)` | 8.0-10.0 | 🔴 High |
| **Prototype Pollution → RCE** | `__proto__` pollution → gadget chain → `execSync()` | 8.0-10.0 | 🔴 High |
| **Server-Side Template Injection (SSTI)** | Template engine → `os.popen()` / `Runtime.exec()` | 8.0-10.0 | 🔴 High |
| **Expression Language Injection** | EL/OGNL/SpEL → `Runtime.getRuntime().exec()` | 8.0-10.0 | 🔴 High |
| **JNDI Injection** | JNDI lookup → Remote class loading → RCE | 10.0 | 🔴 High |
| **Unsafe Reflection/Introspection** | Dynamic method invocation → command execution | 8.0-9.0 | 🟡 Medium |
| **File Upload → RCE** | Unrestricted upload → web shell → command execution | 8.0-9.0 | 🟡 Medium |
| **Argument Injection** | CLI argument injection → `--exec` flags → RCE | 8.0-9.0 | 🟡 Medium |
| **Zip Slip → RCE** | Path traversal → overwrite critical files → RCE | 7.0-9.0 | 🟢 Low |
| **WebSocket Abuse → RCE** | Unauthenticated terminal/execution sockets | 8.0-10.0 | 🔴 High |
| **Chained Access Control → RCE** | Auth bypass + plugin upload / code execution | 9.0-10.0 | 🔴 High |

### 📋 Technology Stack Focus

| Stack | RCE Patterns | Existing Examples |
|-------|-------------|-------------------|
| **Java/Spring** | JNDI injection, EL injection, deserialization, Struts OGNL | Log4Shell, Struts2 (x2), Confluence |
| **PHP** | Unserialize POP chains, `system()` injection, phar deserialization | FreePBX |
| **Python** | `pickle` deserialization, SSTI (Jinja2), `subprocess` injection, `eval()` | Langflow, Crawl4AI, Marimo, Python Pickle |
| **Node.js/JavaScript** | Prototype pollution → RCE, `eval()` injection, `child_process.exec()` | React2Shell |
| **Shell/OS** | Command injection, argument injection, path traversal | Shellshock, PAN-OS, Apache Path Traversal |
| **Go** | Template injection, command injection, unsafe deserialization | — *Needs contributors!* |
| **Ruby** | `Marshal.load` deserialization, ERB SSTI, command injection | — *Needs contributors!* |

### 🔬 The "Vulnerable Sink" Requirement

Every lab submission MUST identify the exact vulnerable function. Examples:

```python
# ✅ Good: Exact vulnerable sink identified
# File: server.py, Line 42
# Vulnerable Sink: subprocess.run(command, shell=True)
command = f"echo 'Log entry: {user_input}' >> log"
subprocess.run(command, shell=True)  # <-- RCE HERE

# ✅ Good: Exact vulnerable sink identified  
# File: index.php, Line 28
// Vulnerable Sink: unserialize($rawPayload)
$data = unserialize($_FILES['backup']['manifest']);  // <-- RCE HERE

# ✅ Good: WebSocket terminal abuse
# File: server.py
# Vulnerable Sink: No validate_auth() call on /terminal/ws endpoint
@app.websocket("/terminal/ws")
async def terminal(websocket):  # <-- No auth check!
    pty = PTY()
    await pty.connect(websocket)

# ❌ Bad: Vague, no specific sink
# "The application has an RCE vulnerability somewhere"
```

---

## 📊 Current Lab Coverage

| # | CVE | Name | Stack | Status |
|---|-----|------|-------|--------|
| 1 | CVE-2026-26978 | FreePBX Deserialization | PHP | ✅ |
| 2 | CVE-2026-26216 | Crawl4AI Hook Injection | Python | ✅ |
| 3 | CVE-2021-44228 | Log4Shell JNDI Injection | Java | ✅ |
| 4 | CVE-2014-6172 | Shellshock | Shell | ✅ |
| 5 | — | Python Pickle Deserialization | Python | ✅ |
| 6 | CVE-2023-50164 | Struts2 Path Traversal | Java | ✅ |
| 7 | CVE-2024-3400 | Palo Alto PAN-OS | Shell | ✅ |
| 8 | CVE-2026-3854 | GitHub Enterprise | Header Injection | ✅ |
| 9 | CVE-2022-22947 | Spring Cloud Gateway SPEL | Java | ⚠️ Unexploited |
| 10 | CVE-2021-41773 | Apache Path Traversal | Shell | ✅ |
| 11 | CVE-2026-39987 | Marimo PTY Terminal | Python | ✅ |
| 12 | CVE-2023-22515/18 | Confluence Access Control | Java | ✅ |
| 13 | CVE-2025-3248 | Langflow Code Injection | Python | ✅ |
| 14 | CVE-2017-5638 | Struts2 OGNL (Equifax) | Java | ✅ |
| 15 | — | SSRF to RCE | Web | ✅ |

**Gaps We Need Filled:**
- 🔴 **Go/Ruby labs** — None yet!
- 🔴 **Node.js beyond prototype pollution** — SSTI, deserialization
- 🟡 **More Java deserialization** — WebLogic, JBoss, Jenkins
- 🟡 **CI/CD pipeline RCE** — GitHub Actions, GitLab CI injection

---

## Lab Architecture Standards

Every lab MUST follow this structure:

```text
labs/CVE-YYYY-NNNNN-Descriptive-Name/
├── app/                          # Application source code
│   ├── src/                      # Source files (if applicable)
│   └── config/                   # Configuration files
├── exploit/                      # Exploitation scripts
│   ├── exploit.py                # Primary exploit script
│   ├── exploit.sh                # Shell-based exploit (optional)
│   └── README.md                 # Exploit usage instructions
├── src/                          # Java/PHP source (when applicable)
│   └── main/                     # Maven/Gradle structure
├── Dockerfile                    # Pinned vulnerable versions
├── docker-compose.yml            # Container orchestration
├── .dockerignore                 # Docker build exclusions
├── pom.xml                       # Maven config (Java labs)
├── requirements.txt              # Python dependencies (Python labs)
└── README.md                     # Lab documentation
```

---

## Quality Requirements

### Lab MUST:

- ✅ Build and run with a single `docker compose up --build -d` command
- ✅ Include a working exploit (manual curl commands OR automated script)
- ✅ Document the vulnerability with root cause analysis
- ✅ Run in isolation (no external dependencies)
- ✅ Use pinned vulnerable versions (never `latest` tags)
- ✅ Include cleanup instructions
- ✅ Verify exploit works on clean `docker compose up --build`
- ✅ Use `--no-cache` build to ensure reproducibility

### Lab SHOULD:

- 👍 Support both automated and manual exploitation
- 👍 Include detection/mitigation guidance
- 👍 Have commented, readable exploit code
- 👍 Follow the standard directory structure
- 👍 Reference original CVE and research
- 👍 Include a `PAYLOAD` variable or helper function for easy reuse
- 👍 Add relevant treasure files for post-exploitation discovery (optional)

### Lab MUST NOT:

- ❌ Require external API keys or paid services
- ❌ Download exploits from untrusted sources at runtime
- ❌ Include actual malware or backdoors
- ❌ Target real systems or services
- ❌ Expose sensitive information in logs or configs

---

## Pull Request Process

1. **Check Existing Labs:** Ensure your CVE isn't already covered
2. **Follow the Template:** Use the standard directory structure
3. **Test Thoroughly:** Verify on a clean Docker environment
4. **Document Completely:** Every lab needs a proper README (see [lab_14](labs/lab_14/CVE-2017-5638-Struts2/README.md) for the gold standard)
5. **One CVE Per PR:** Submit one vulnerability per pull request
6. **Respond to Review:** Address maintainer feedback promptly
7. **Update Main README:** Add your lab to the verified labs table

---

## 📐 Quality Checklist

**Before submitting, verify your lab:**

```bash
# 1. Does it build cleanly?
docker compose up --build -d

# 2. Does the exploit work?
python3 exploit/exploit.py
# OR
./exploit/exploit.sh

# 3. Do you get a shell?
# Expected: uid=0(root) or uid=33(www-data) or similar

# 4. Can you execute multiple commands?
# Test: id, whoami, hostname, uname -a

# 5. Is the vulnerable sink documented?
grep -n "VULNERABILITY\|VULNERABLE SINK\|SINK" app/* src/* 2>/dev/null

# 6. Does it clean up properly?
docker compose down -v

# 7. Does it rebuild from scratch?
docker compose build --no-cache && docker compose up -d
```

**Remember:** If a student can't go from `docker compose up` to a reverse shell by following your README, the lab isn't ready for submission.

---

## Questions?

- **🐛 Bug Reports & Feature Requests:** [Open an Issue](https://github.com/HaakimSec/zero2shell-50/issues)
- **💬 General Discussion:** [GitHub Discussions](https://github.com/HaakimSec/zero2shell-50/discussions)
- **🔒 Security Concerns (Private Disclosure):** Email `hakimabdi206@gmail.com`
- **📧 Direct Contact:** `hakimabdi206@proton.me` (for collaboration inquiries only)

> ⚠️ Please do NOT email for basic questions answered in the README. Open an issue instead so others can benefit from the answer.

---

<div align="center">
  <b>Let's build the future of security education together. 🐚</b>
</div>
