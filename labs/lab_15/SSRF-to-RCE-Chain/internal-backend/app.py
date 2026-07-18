from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def internal_home():
    return "Secure Internal Management Portal. Authorized Access Only."

# VULNERABLE ENDPOINT: Performs system interaction without sanitation
@app.route('/api/maintenance/ping')
def system_ping():
    host = request.args.get('host')
    if not host:
        return jsonify({"status": "error", "message": "Missing 'host' target"}), 400

    try:
        # Vulnerable shell execution primitive modeling classic command injection
        # e.g., ping -c 1 [user_input]
        command = f"ping -c 1 {host}"
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return jsonify({"status": "success", "output": output})
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "failed", "output": e.output}), 500

if __name__ == '__main__':
    # Listens strictly within the internal Docker bridge network
    app.run(host='0.0.0.0', port=5000)
