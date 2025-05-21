from flask import Flask, jsonify, request
from chat import get_response  # Import your chatbot function
import os  # ✅ Needed for environment variables

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Chatbot API is running!"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' field"}), 400
    
    user_message = data["message"].strip()
    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400
    
    # Get chatbot response
    bot_response = get_response(user_message)
    
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # ✅ Use Render’s dynamic port
    app.run(host="0.0.0.0", port=port)
