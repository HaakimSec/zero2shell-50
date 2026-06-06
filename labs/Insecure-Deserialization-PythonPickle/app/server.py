import base64
import pickle
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/api/v1/dashboard', methods=['GET'])
def dashboard():
    # Retrieve the session cookie supplied by the client
    session_cookie = request.cookies.get('session_data')
    
    if not session_cookie:
        # Create a default benign session profile if none exists
        default_profile = {"username": "guest_user", "role": "viewer"}
        serialized = base64.b64encode(pickle.dumps(default_profile)).decode()
        
        resp = make_response(jsonify({"message": "Welcome guest! Session initialized."}))
        resp.set_cookie('session_data', serialized)
        return resp

    try:
        # VULNERABILITY SINK: Unsafely deserializing untrusted user input.
        # Python's pickle module will execute the __reduce__ method of any 
        # object instantiated within the stream automatically upon loading.
        decoded_data = base64.b64decode(session_cookie)
        user_profile = pickle.loads(decoded_data)
        
        return jsonify({
            "status": "authenticated",
            "welcome": f"Hello {user_profile.get('username', 'User')}!",
            "role": user_profile.get('role', 'none')
        }), 200
        
    except Exception as e:
        return jsonify({"status": "error", "message": f"Session processing failure: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
