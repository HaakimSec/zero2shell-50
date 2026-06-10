# Contributing to Zero2Shell-50 🚀

First off, thank you for considering contributing to ZeroToShell-50! This project aims to build the most comprehensive, modern collection of containerized RCE labs for security education. Every contribution helps make cybersecurity training more accessible.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [What We're Looking For](#what-were-looking-for)
- [Quality Requirements](#quality-requirements)
- [Pull Request Process](#pull-request-process)
- [Quality Checklist](#-quality-checklist)
- [Questions?](#questions)




## Code of Conduct

This project and everyone participating in it is governed by the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct.html). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.


## What We're Looking For

### 🎯 The "Zero2Shell" Mandate

**Every lab must result in Remote Code Execution (RCE) or system-level command injection.** This project is called ZeroToShell for a reason — if it doesn't end with a shell, it doesn't belong here.

### ✅ High-Priority Contributions

- **Modern CVEs (2024-2026):** Focused on recent, actively exploited vulnerabilities
- **Unauthenticated RCE:** The holy grail — no credentials required
- **Authenticated RCE:** Admin-to-shell chains are acceptable if well-documented
- **Framework-Level Flaws:** Vulnerabilities in popular frameworks, not custom code
- **Logic-Based RCE:** Deserialization, injection, prototype pollution — not memory corruption

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

### 📋 Technology Stack Focus

| Stack | RCE Patterns | Examples |
|-------|-------------|----------|
| **Java/Spring** | JNDI injection, EL injection, deserialization, Struts OGNL | Log4Shell, Spring4Shell, Struts2 |
| **PHP** | Unserialize POP chains, `system()` injection, phar deserialization | FreeBPX, WordPress plugins, Laravel deserialization |
| **Python** | `pickle` deserialization, SSTI (Jinja2), `subprocess` injection, `eval()` | Flask SSTI, Django pickle, PyYAML RCE |
| **Node.js/JavaScript** | Prototype pollution → RCE, `eval()` injection, `child_process.exec()` | React2Shell, Next.js, Nuxt.js |
| **Go** | Template injection, command injection, unsafe deserialization | Go SSTI, Mattermost RCE |
| **Ruby** | `Marshal.load` deserialization, ERB SSTI, command injection | Rails deserialization |

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

# ❌ Bad: Vague, no specific sink
# "The application has an RCE vulnerability somewhere"

## Lab Architecture Standards

Every lab MUST follow this structure:

```text
labs/CVE-YYYY-NNNNN-Descriptive-Name/
├── app/                          # Application source code
│   ├── src/                      # Source files (if applicable)
│   └── config/                   # Configuration files
├── exploit/                      # Exploitation scripts
│   ├── exploit.py                # Primary exploit script
│   └── README.md                 # Exploit usage instructions
├── Dockerfile                    # Pinned vulnerable versions
├── docker-compose.yml            # Container orchestration
├── .dockerignore                 # Docker build exclusions
└── README.md                     # Lab documentation (see template below)
```

## Quality Requirements

### Lab Must:

- ✅ Build and run with a single docker compose up --build -d command

- ✅ Include a working exploit (manual curl commands OR automated script)

- ✅ Document the vulnerability with root cause analysis

- ✅ Run in isolation (no external dependencies)

- ✅ Use pinned vulnerable versions (never latest tags)

- ✅ Include cleanup instructions

### Lab Should:

- 👍 Support both automated and manual exploitation

- 👍 Include detection/mitigation guidance

- 👍 Have commented, readable exploit code

- 👍 Follow the standard directory structure

- 👍 Reference original CVE and research

### Lab Must NOT:

- ❌ Require external API keys or paid services

- ❌ Download exploits from untrusted sources at runtime

- ❌ Include actual malware or backdoors

- ❌ Target real systems or services

- ❌ Expose sensitive information in logs or configs

## Pull Request Process

1. **Check Existing Labs:** Ensure your CVE isn't already covered

2. **Follow the Template:** Use the standard directory structure

3. **Test Thoroughly:** Verify on a clean Docker environment

4. **Document Completely:** Every lab needs a proper README

5. **One CVE Per PR:** Submit one vulnerability per pull request

6. **Respond to Review:** Address maintainer feedback promptly


## 📐 Quality Checklist

**Before submitting, verify your lab:**

```bash
# 1. Does it build cleanly?
docker compose up --build -d

# 2. Does the exploit work?
python3 exploit/exploit.py

# 3. Do you get a shell?
# Expected: uid=0(root) or uid=33(www-data)

# 4. Is the vulnerable sink documented?
grep -n "VULNERABILITY\|VULNERABLE SINK" app/*
```
**Remember:** If a student can't go from docker compose up to a reverse shell by following your README, the lab isn't ready for submission.

## Questions?

- **🐛 Bug Reports & Feature Requests:** [Open an Issue](https://github.com/HaakimSec/zero2shell-50/issues)
- **💬 General Discussion:** [GitHub Discussions](https://github.com/HaakimSec/zero2shell-50/discussions)
- **🔒 Security Concerns (Private Disclosure):** Email `hakimabdi206@gmail.com`
- **📧 Direct Contact:** `hakimabdi206@proton.me` (for collaboration inquiries only)

> ⚠️ Please do NOT email for basic questions answered in the README. Open an issue instead so others can benefit from the answer.
