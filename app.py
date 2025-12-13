"""
=========================================================
General Purpose Flask Chatbot Framework (LangChain)
=========================================================
"""

from flask import Flask, request, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import json

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# -------------------------------
# Load environment
# -------------------------------
load_dotenv()

# -------------------------------
# Load chatbot configuration (UTF-8 SAFE)
# -------------------------------
with open("chatbot_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# -------------------------------
# Initialize Flask app
# -------------------------------
app = Flask(__name__)
CORS(app)

# -------------------------------
# LangChain LLM (OpenAI backend)
# -------------------------------
llm = ChatOpenAI(
    model=config["model"],
    temperature=config["temperature"],
    max_tokens=config["max_tokens"],
)

# -------------------------------
# Conversation history
# (same behavior as your original version)
# -------------------------------
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
        data = request.get_json(force=True)
        user_prompt = data.get("prompt", "").strip()

        if not user_prompt:
            return "No prompt provided", 400

        # Add user message
        conversation_history.append(
            HumanMessage(content=user_prompt)
        )

        # Build message list
        messages = [
            SystemMessage(content=config["description"]),
            *conversation_history,
        ]

        # Call LLM
        response = llm.invoke(messages)
        reply = response.content.strip()

        # Store assistant reply
        conversation_history.append(
            AIMessage(content=reply)
        )

        return reply

    except Exception as e:
        print("Error:", e)
        return "Internal server error", 500

# -------------------------------
# Run Flask app
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
