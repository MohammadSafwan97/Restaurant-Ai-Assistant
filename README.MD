🤖 Flask Chatbot using OpenAI GPT

A modular and configurable chatbot built with Flask and OpenAI GPT models.
Easily adaptable for different domains (e.g., restaurant assistant, travel planner, customer support) by editing a configuration file.

⚙️ Features

Flask backend with OpenAI GPT integration

Configurable chatbot behavior via chatbot_config.json

Conversation context memory

Domain-restricted responses

Frontend built with HTML, CSS, and JavaScript

🛠️ Setup

1. Clone the Repository
   git clone https://github.com/MohammadSafwan97/LLM_application_chatbot.git
   cd LLM_application_chatbot

2. Create and Activate Virtual Environment
   python -m venv venv
   venv\Scripts\activate # Windows
   source venv/bin/activate # macOS/Linux

3. Install Dependencies
   pip install -r requirements.txt

4. Configure Environment

Create a .env file in the project root:

OPENAI_API_KEY=sk-your_api_key_here

🧩 Configuration

Edit chatbot_config.json to define chatbot behavior:

{
"name": "Restaurant Assistant",
"description": "You are a polite restaurant chatbot that only answers restaurant-related questions.",
"model": "gpt-3.5-turbo",
"temperature": 0.6,
"max_tokens": 200,
"off_topic_response": "I'm sorry, I can only answer questions related to our restaurant."
}

▶️ Run the Application
python app.py

Access the chatbot at http://127.0.0.1:5000

🧠 Key Parameters
Parameter Description
description Defines chatbot’s tone and scope
model OpenAI model (e.g., gpt-3.5-turbo, gpt-4)
temperature Creativity control (0 = factual, 1 = creative)
max_tokens Limits response length
off_topic_response Default message for unrelated queries
📦 Dependencies

Flask

Flask-CORS

OpenAI (v1.0+)

python-dotenv

🔒 Security

.env file is excluded via .gitignore

Never commit your API key to source control

Regenerate keys if exposed

👤 Author

Muhammad Safwan
📧 mohammadsafwan248@gmail.com

🌐 GitHub: MohammadSafwan97
