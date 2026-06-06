# ZeroToShell-50 🚀

> A highly curated, containerized training ground featuring **50 Modern Remote Code Execution (RCE) Environments** spanning **2024 to 2026**.

`ZeroToShell-50` is a hands-on laboratory designed for security researchers, penetration testers, and application security engineers. While traditional vulnerability repositories span decades of legacy flaws, this project focuses exclusively on the modern attack surface: cloud-native architectures, prototype pollution in modern JS runtimes, AI agent framework injections, and cutting-edge enterprise supply-chain failures.

Each lab is engineered to be **deterministic, isolated, and completely self-contained** via Docker Compose, bridging the gap between raw vulnerability discovery and weaponized local exploitation.

---

## 🏗️ Repository Architecture

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
