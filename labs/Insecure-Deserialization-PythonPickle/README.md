# Lab 04: Insecure Deserialization — Python Pickle Object Injection

## 📌 Description
This lab showcases the classic structural danger of **Insecure Deserialization** using Python's native `pickle` engine. 

Object serialization is extensively used across web session tracking handlers and modern machine learning/AI model training pipelines (such as loading unvetted `.pkl` models). The vulnerability manifests when the application backend passes an untrusted, client-controlled base64 tracking cookie directly into `pickle.loads()`. Because Python allows classes to declare custom recreation blueprints via the `__reduce__` magic method constructor, an attacker can substitute raw object states with system-level commands, achieving direct code execution when the file stream parsing logic executes.

---

## 🏗️ Environment Setup
To build and spin up this isolated python runtime workspace:

```bash
# Compile and trigger the flask container background daemon
docker compose up --build -d

# Track the container log matrix to confirm startup
docker compose logs -f

```

The target endpoint is available locally at: `http://localhost:5000/api/v1/dashboard`

**💥 Exploitation**

To demonstrate the arbitrary object instantiation breakout, fire the repository execution script:

```bash 

```

**Manual Mechanics**

If you make a normal request to the endpoint, the application assigns a safe, base64-encoded cookie payload to your storage scope:

```Bash
curl -i http://localhost:5000/api/v1/dashboard

```

When you transmit the malicious, engineered string back via the Cookie: session_data=[PAYLOAD] parameter, the internal stack evaluation triggers the execution hook automatically inside the container subshell.

**🧹 Cleanup**

To cleanly erase the target image layers and isolate network variables:

```Bash
docker compose down -v

```
```markdown
here is a screenshot of [poc](labs/Insecure-Deserialization-PythonPickle/assets/1.png) ```
