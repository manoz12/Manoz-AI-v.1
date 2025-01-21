from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Hugging Face API Configuration
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message")
        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        # Get the response from Hugging Face API
        response = query({"inputs": user_input})
        
        # Debugging: Print response to check its structure
        print(response)

        # Check if the response is a list and handle accordingly
        if isinstance(response, list):
            bot_reply = response[0].get("generated_text", "Sorry, I couldn't understand that.")
        else:
            bot_reply = response.get("generated_text", "Sorry, I couldn't understand that.")
        
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
