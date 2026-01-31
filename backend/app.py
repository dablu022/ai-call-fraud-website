from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

KEYWORDS = ["otp","kyc","bank","urgent","payment","upi"]

@app.route("/analyze", methods=["POST"])
def analyze():
    transcript = "Urgent call regarding your bank KYC verification"
    score = sum(1 for k in KEYWORDS if k in transcript.lower())

    if score >= 3:
        result = "🔴 FRAUD CALL DETECTED"
    elif score >= 1:
        result = "🟡 SUSPICIOUS CALL"
    else:
        result = "🟢 SAFE CALL"

    return jsonify({
        "transcript": transcript,
        "result": result
    })

app.run()
