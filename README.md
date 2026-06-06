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
  <img src="https://img.shields.io/badge/Labs-7%20%2F%2050-vividblue?style=for-the-badge&logo=docker" alt="Labs Progress">
  <img src="https://img.shields.io/badge/Focus-RCE%20%26%20Deserialization-red?style=for-the-badge&logo=target" alt="Focus Area">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

---

> **From Zero to Shell — Master Modern RCE Exploitation in 50 Hands-On Labs**

`ZeroToShell-50` is a comprehensive, containerized training platform featuring **50 meticulously crafted Remote Code Execution (RCE) environments** spanning critical vulnerabilities from **2024 to 2026**. Each lab transforms real-world CVEs into deterministic, isolated, and fully reproducible exploitation scenarios.

## 🎯 Why ZeroToShell-50?

Modern application security demands practical expertise in contemporary attack surfaces. While traditional training resources focus on decades-old vulnerabilities, `ZeroToShell-50` targets the bleeding edge:

- **Cloud-Native Architectures** — Container escape, serverless injection, microservice deserialization
- **Modern JavaScript Runtimes** — Prototype pollution, React Server Components exploitation
- **AI/ML Attack Surface** — LLM agent framework injection, model serialization attacks
- **Enterprise Supply Chain** — Dependency confusion, CI/CD pipeline injection, artifact poisoning
- **Next-Gen Web Frameworks** — Next.js, Remix, Astro, and modern SSR vulnerability chains

## 🧪 What Makes This Different

Unlike traditional CVE databases or read-only proof-of-concepts, `ZeroToShell-50` is built for **active learning**:

| Feature | Description |
|---------|-------------|
| 🐳 **Fully Containerized** | Every lab runs in isolated Docker environments — no dependency hell |
| 📝 **Root Cause Analysis** | Each lab includes detailed vulnerability analysis, not just exploit scripts |
| 🎯 **Deterministic Exploitation** | Consistent, repeatable exploits verified against pinned vulnerable versions |
| 🔬 **Modern Attack Surface** | Focused exclusively on 2024-2026 CVEs in contemporary tech stacks |
| 🛡️ **Defense Perspective** | Mitigation strategies and detection rules included for blue team training |
| 📐 **Standardized Structure** | Uniform lab architecture for rapid deployment and easy navigation |

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
| 1 | [CVE-2024-3400](labs/CVE-2024-3400-CommandInjection/) | PAN-OS GlobalProtect Command Injection | 10.0 | OS Command Injection | ✅ Verified |
| 2 | [CVE-2025-55182](labs/CVE-2025-55182-React2Shell/) | React Server Components Prototype Pollution RCE | Critical | Prototype Pollution | ✅ Verified |
| 3 | [CVE-2026-26978](labs/CVE-2026-26978-freeBPX/) | FreeBPX Backup & Restore Deserialization RCE | 8.8 | PHP Deserialization | ✅ Verified |
| 4-50 | *Coming Soon* | More modern RCE vulnerabilities... | — | — | 🚧 In Development |

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/HaakimSec/zero2shell-50.git
cd zero2shell-50

# Navigate to any lab
cd labs/CVE-2024-3400-CommandInjection

# Deploy the vulnerable environment
docker compose up --build -d

# Follow the lab README for exploitation steps
```

---

**🏗️ Repository Architecture**

Every vulnerability in this repository follows a strict structural blueprint to ensure clean deployment and deep academic readability:

```text
ZeroToShell-50/
├── .github/                 # CI/CD verification workflows
├── labs/
│   └── [CVE-ID-Name]/       # Target Lab Identifier
│       ├── app/             # Raw application source / code configurations
│       ├── exploit/         # Exploit automation & helper tools
│       ├── Dockerfile       # Pinning precise vulnerable layers
│       ├── docker-compose.yml
│       └── README.md        # Lab-specific Root Cause Analysis (RCA)
└── README.md                # Master index and project roadmap

```
---

**🛡️ Educational Philosophy**

`ZeroToShell-50` operates on a simple principle: You cannot defend what you don't understand. Each lab is designed to:

1. Replicate the vulnerable environment with pinned dependencies

2 Explain the root cause with annotated source code analysis

3. Exploit the vulnerability step-by-step with working payloads

4. Mitigate with practical, immediately applicable fixes

5. Detect with log analysis patterns and WAF rule suggestions

---

**⚠️ Disclaimer**

This repository is for educational purposes only. All labs must be run in isolated, controlled environments. Never exploit these vulnerabilities against systems you do not own or have explicit written permission to test. The authors assume no liability for misuse.

---

**Start your journey from Zero to Shell. 🐚**
