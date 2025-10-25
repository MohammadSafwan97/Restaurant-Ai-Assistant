"""
=========================================================
General Purpose Flask Chatbot Framework (OpenAI GPT)
=========================================================

This app provides a reusable chatbot backend.
Modify `chatbot_config.json` to customize chatbot behavior
for different clients or use cases.

Example use cases:
- Customer Support
- Travel Assistant
- Restaurant Bot
- Educational Tutor
=========================================================
"""

from flask import Flask, request, render_template
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# -------------------------------
# Load environment and config
# -------------------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Load chatbot configuration from file
with open("chatbot_config.json", "r") as f:
    config = json.load(f)

# -------------------------------
# Initialize Flask app
# -------------------------------
app = Flask(__name__)
CORS(app)

conversation_history = []

# -------------------------------
# Route: Home Page
# -------------------------------
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# -------------------------------
# Route: Chatbot Interaction
# -------------------------------
@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        data = json.loads(request.get_data(as_text=True))
        user_prompt = data.get("prompt", "")

        if not user_prompt:
            return "No prompt provided", 400

        # Add user message to history
        conversation_history.append({"role": "user", "content": user_prompt})

        # Create chat completion request dynamically from config
        response = client.chat.completions.create(
            model=config["model"],
            messages=[
                {
                    "role": "system",
                    "content": config["description"]
                },
                *conversation_history,
            ],
            temperature=config["temperature"],
            max_tokens=config["max_tokens"],
        )

        # Extract assistant response
        reply = response.choices[0].message.content.strip()

        # Store assistant reply in conversation history
        conversation_history.append({"role": "assistant", "content": reply})

        return reply

    except Exception as e:
        print("Error:", e)
        return str(e), 500

# -------------------------------
# Run Flask app
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
