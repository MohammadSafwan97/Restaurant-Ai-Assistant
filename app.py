"""
=========================================================
Flask Chatbot using OpenAI GPT (v1.x Compatible)
=========================================================

This Flask app connects to OpenAI's GPT model (gpt-3.5-turbo)
using the latest Python client (openai>=1.0.0).

Make sure you have:
    pip install openai flask flask_cors python-dotenv

Your .env file (in the project root) must contain:
    OPENAI_API_KEY=sk-your_api_key_here
=========================================================
"""

from flask import Flask, request, render_template
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client (new syntax)
client = OpenAI(api_key=api_key)

# -------------------------------
# Initialize Flask app
# -------------------------------
app = Flask(__name__)
CORS(app)

# Store chat history to maintain context
conversation_history = []

# -------------------------------
# Route: Home Page
# -------------------------------
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# -------------------------------
# Route: Chatbot API
# -------------------------------
@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        # Parse the incoming JSON request
        data = json.loads(request.get_data(as_text=True))
        user_prompt = data.get("prompt", "")

        if not user_prompt:
            return "No prompt provided", 400

        # Store the user's message
        conversation_history.append({"role": "user", "content": user_prompt})

        # Generate a response using OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or gpt-4 if you have access
            messages=[
                {"role": "system", "content": "You are a friendly AI assistant."},
                *conversation_history,
            ],
            temperature=0.7,
            max_tokens=50,
        )

        # Extract the assistant's reply
        reply = response.choices[0].message.content.strip()

        # Add the reply to conversation history
        conversation_history.append({"role": "assistant", "content": reply})

        return reply

    except Exception as e:
        print("Error:", e)
        return str(e), 500

# -------------------------------
# Run Flask App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
