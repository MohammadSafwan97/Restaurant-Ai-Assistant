# 🤖 OpenAI Chatbot using Flask

This is a simple web-based chatbot built with **Flask** (Python) and **OpenAI's GPT API**.  
You can chat with the bot through a web interface similar to ChatGPT.

---

## 🚀 Features

- 💬 Conversational chatbot powered by OpenAI GPT (gpt-3.5-turbo or gpt-4)
- 🌐 Flask backend + HTML/JS frontend
- 🔒 API key secured via `.env` file
- 🎨 Simple, responsive chat interface

---

## 🧱 Project Structure

chatbot_project/
│
├── app.py # Flask backend
├── .env # OpenAI API key (not committed)
├── .gitignore # Ignore sensitive files
├── requirements.txt # Dependencies
├── README.md # Documentation
│
├── templates/
│ └── index.html # Webpage frontend
│
└── static/
├── css/style.css # Styling
├── script.js # Chat logic (fetches from Flask)
└── images/ # User/Bot icons

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/chatbot_project.git
cd chatbot_project
2️⃣ Create a virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Create .env file
In the project root, create a .env file and add:

ini
Copy code
OPENAI_API_KEY=sk-your_openai_api_key_here
5️⃣ Run the Flask app
bash
Copy code
python app.py
By default, the server will run at:
👉 http://127.0.0.1:5000/

🧠 Usage
Open the app in your browser at http://127.0.0.1:5000/

Type a message and press Enter.

The chatbot will respond using OpenAI's GPT model.

🧩 Technologies Used
Python

Flask

OpenAI GPT API

HTML / CSS / JavaScript


🧑‍💻 Author
Created by Muhammad Safwan
📧 Email: mohammadsafwan248@gmail.com
🌐 GitHub: MohammadSafwan97
```
