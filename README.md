```text
====================================================================================
 ███████╗███████╗██████╗  ██████╗ ██████╗  ███████╗██╗  ██╗███████╗██╗     ██╗
 ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗╚════██╗ ██╔════╝██║  ██║██╔════╝██║     ██║
   ███╔╝ █████╗  ██████╔╝██║   ██║ █████╔╝ ███████╗███████║█████╗  ██║     ██║
  ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██╔═══╝  ╚════██║██╔══██║██╔══╝  ██║     ██║
 ███████╗███████╗██║  ██║╚██████╔╝███████╗ ███████║██║  ██║███████╗███████╗███████╗
 ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
                                                      [ 50 Containerized RCE Labs ]
====================================================================================
```
<p align="center">
  <img src="https://img.shields.io/badge/Labs-15%20%2F%2050-vividblue?style=for-the-badge&logo=docker" alt="Labs Progress">
  <img src="https://img.shields.io/badge/Focus-RCE%20%26%20Deserialization-red?style=for-the-badge&logo=target" alt="Focus Area">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

---

### From Zero to Shell — Master Modern RCE Exploitation in 50 Hands-On Labs

`Zero2Shell-50` is a comprehensive, containerized training platform featuring 50 meticulously crafted Remote Code Execution (RCE) environments spanning critical vulnerabilities from 2014 to 2026. Each lab transforms real-world CVEs into deterministic, isolated, and fully reproducible exploitation scenarios.

## 🎯 Why ZeroToShell-50?

Modern application security demands practical expertise in contemporary attack surfaces. `ZeroToShell-50` targets the full spectrum of modern exploitation:

- **Java Enterprise Frameworks** — Struts2 OGNL injection, Spring path traversal, ActiveMQ deserialization

- **Modern JavaScript Runtimes** — Prototype pollution, React Server Components exploitation

- **AI/ML Attack Surface** — LLM agent framework injection, notebook terminal abuse, model serialization attacks

- **PHP Deserialization** — POP chain construction, PHAR stream wrapper abuse

- **Next-Gen Web Frameworks** — Langflow code injection, Crawl4AI hook abuse, Marimo WebSocket exploitation

- **Classic & Modern CVEs** — Log4Shell, Shellshock, Struts2, Apache Path Traversal, GitHub Enterprise, Confluence chained exploits

## 🧪 What Makes This Different

Unlike traditional CVE databases or read-only proof-of-concepts, `Zero2Shell-50` is built for **active learning**:

| Feature | Description |
|---------|-------------|
| 🐳 **Fully Containerized** | Every lab runs in isolated Docker environments — no dependency hell |
| 📝 **Root Cause Analysis** | Each lab includes detailed vulnerability analysis, not just exploit scripts |
| 🎯 **Deterministic Exploitation** | Consistent, repeatable exploits verified against pinned vulnerable versions |
| 🔬 **Diverse Attack Surface** | Covers Java, Python, PHP, JavaScript, and shell-based vulnerabilities |
| 🛡️ **Defense Perspective** | Mitigation strategies and detection rules included for blue team training |
| 📐 **Standardized Structure** | Uniform lab architecture for rapid deployment and easy navigation |
| 🏦 **Historical Impact** | Labs tied to real-world breaches (Equifax, Log4Shell, Shellshock) |


## 👥 Who Is This For?

- **Penetration Testers** — Practice modern exploitation techniques in safe, legal environments

- **Security Researchers** — Study root cause analysis of recent critical vulnerabilities

- **Application Security Engineers** — Understand vulnerability patterns to secure your codebase

- **Blue Team / SOC Analysts** — Learn attacker TTPs to build better detection rules

- **CTF Players** — Sharpen your skills against real-world vulnerability classes

- **Students & Educators** — Hands-on curriculum for modern application security courses

## ✅ Verified Labs

| # | CVE | Description | CVSS | Type | Status |
|---|-----|-------------|------|------|--------|
| 1 | [CVE-2026-26978](labs/lab_01/CVE-2026-26978-FreePBX/) | FreePBX Backup & Restore Deserialization RCE | 8.8 | PHP Deserialization | ✅ Verified |
| 2 | [CVE-2026-26216](labs/lab_02/CVE-2026-26216-Crawl4AI/) | Crawl4AI Hook Injection RCE | Critical | Python Code Injection | ✅ Verified |
| 3 | [CVE-2021-44228](labs/lab_03/CVE-2021-44228-Log4shell/) | Apache Log4Shell JNDI Injection RCE | 10.0 | Java JNDI Injection | ✅ Verified |
| 4 | [CVE-2014-6172](labs/lab_04/CVE-2014-6172-Shell-shock/) | GNU Bash Shellshock RCE | 10.0 | OS Command Injection | ✅ Verified |
| 5 | [Python Pickle](labs/lab_05/) | Python Pickle Deserialization RCE | — | Python Deserialization | ✅ Verified |
| 6 | [CVE-2023-50164](labs/lab_06/CVE-2023-50164-Struts2/) | Apache Struts2 Path Traversal RCE | 9.8 | Path Traversal → RCE | ✅ Verified |
| 7 | [CVE-2024-3400](labs/lab_07/CVE-2024-3400-palo-alto/) | Palo Alto PAN-OS Command Injection | 10.0 | OS Command Injection | ✅ Verified |
| 8 | [CVE-2026-3854](labs/lab_08/CVE-2026-3854-Github/) | GitHub Enterprise Parameter Injection RCE | 9.8 | Header Injection | ✅ Verified |
| 9 | [CVE-2022-22947](labs/lab_09/CVE-2022-22947-spel-gate-way/) | Spring Cloud Gateway SPEL Injection RCE | 10.0 | Expression Injection | ⚠️ Unexploited |
| 10 | [CVE-2021-41773](labs/lab_10/CVE-2021-41773-apache-path-traversal/) | Apache HTTPD 2.4.49 Path Traversal RCE | 9.8 | Path Traversal → CGI | ✅ Verified |
| 11 | [CVE-2026-39987](labs/lab_11/CVE-2026-39987-Marimo/) | Marimo Pre-Auth PTY Terminal RCE | Critical | WebSocket Abuse | ✅ Verified |
| 12 | [CVE-2023-22515/18](labs/lab_12/CVE-2023-22515-Confluence/) | Confluence Broken Access Control → RCE | 9.8 | Chained Access Control | ✅ Verified |
| 13 | [CVE-2025-3248](labs/lab_13/CVE-2025-3248-Langflow/) | Langflow Flow Execution RCE | Critical | Python Code Injection | ✅ Verified |
| 14 | [CVE-2017-5638](labs/lab_14/CVE-2017-5638-Struts2/) | Apache Struts2 OGNL Injection RCE (Equifax) | 10.0 | OGNL Expression Injection | ✅ Verified |
| 15 | [SSRF to RCE](labs/lab_15/) | Server-Side Request Forgery → RCE | — | SSRF Chain | ✅ Verified |
| 16-50 | *Coming Soon* | More modern RCE vulnerabilities... | — | — | 🚧 In Development |

### Stats

| Category | Count | Percentage |
|----------|-------|------------|
| **Verified & Exploited** | **13** | 87% |
| **Unexploited** | **1** | 7% |
| **In Development** | **1** | 6% |


## 🚀 Quick Start

```bash
# Clone the repository
git clone --depth 1 https://github.com/HaakimSec/zero2shell-50.git
cd zero2shell-50

# Navigate to any lab
cd labs/lab_14/CVE-2017-5638-Struts2

# Deploy the vulnerable environment
docker compose up --build -d

# Follow the lab README for exploitation steps
```

## 🏗️ Repository Architecture

Every vulnerability in this repository follows a strict structural blueprint to ensure clean deployment and deep academic readability:

```text 
ZeroToShell-50/
├── .github/                 # CI/CD verification workflows
├── labs/
│   └── lab_XX/              # Target Lab Identifier
│       ├── app/             # Raw application source / code configurations
│       ├── exploit/         # Exploit automation & helper tools
│       ├── src/             # Java/PHP/Python source files (when applicable)
│       ├── Dockerfile       # Pinning precise vulnerable layers
│       ├── docker-compose.yml
│       └── README.md        # Lab-specific Root Cause Analysis (RCA)
└── README.md                # Master index and project roadmap
```

## 🛡️ Educational Philosophy

`Zero2Shell-50` operates on a simple principle: You cannot defend what you don't understand. Each lab is designed to:

1. **Replicate** the vulnerable environment with pinned dependencies

2. **Explain** the root cause with annotated source code analysis

3. **Exploit** the vulnerability step-by-step with working payloads

4. **Mitigate** with practical, immediately applicable fixes

5. **Detect** with log analysis patterns and WAF rule suggestions

---

## 🤝 Contributing

`Zero2Shell-50` is a ambitious project — **50 RCE labs** spanning modern exploitation techniques across multiple technology stacks. While 15 labs are already verified and exploitable, I cannot build the remaining 35 alone.

I am actively seeking collaboration from the security community:

- 🔬 **Security Researchers** — Contribute new CVE labs with root cause analysis
- 🐳 **DevOps Engineers** — Improve Docker configurations and CI/CD pipelines
- 📝 **Technical Writers** — Enhance documentation, READMEs, and exploitation guides
- 🎯 **Penetration Testers** — Verify exploits against pinned vulnerable versions
- 🛡️ **Blue Teamers** — Add detection rules, log analysis patterns, and WAF signatures

Whether you want to add a single lab, fix a typo, or contribute an entirely new vulnerability class — **every contribution matters**.

> *"The best security training doesn't come from reading advisories — it comes from breaking things, understanding why they broke, and sharing that knowledge with others."*

Check out **[CONTRIBUTING.md](CONTRIBUTING.md)** for guidelines on lab structure, exploit verification standards, and how to submit your first lab.

Let's build the future of security education together. 🐚

## ⚠️ Disclaimer

This repository is for educational purposes only. All labs must be run in isolated, controlled environments. Never exploit these vulnerabilities against systems you do not own or have explicit written permission to test. The authors assume no liability for misuse.

**Start your journey from Zero to Shell. 🐚**


