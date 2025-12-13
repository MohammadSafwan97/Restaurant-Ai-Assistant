🍽️ Safwan Restaurant Chatbot

A configurable, backend-driven chatbot built with Flask and LangChain, designed to act as a virtual assistant for a restaurant.
The project focuses on clean architecture, configuration-driven behavior, and practical LLM integration.

Overview

This project implements a restaurant chatbot that assists users with:

Menu-related questions

Opening hours

Location information

General restaurant inquiries

The chatbot behavior is fully controlled via configuration, allowing the same codebase to be reused for other restaurants or business domains with minimal changes.

Key Features

Flask-based backend with a simple REST API

LangChain-powered LLM integration

Configuration-driven chatbot behavior (no hardcoded prompts)

Clean separation between frontend and backend

UTF-8 safe configuration loading (Windows-compatible)

Minimal, readable code structure suitable for extension

Tech Stack

Python 3.13

Flask

LangChain

OpenAI API

TailwindCSS (frontend styling)

Project Structure
LLM_application_chatbot/
│
├── app.py                  # Flask backend + LangChain logic
├── chatbot_config.json     # Chatbot behavior & model configuration
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   ├── user.png
│   ├── Bot_logo.png
│   └── styles / scripts
├── requirements.txt
└── README.md

Configuration-Driven Design

All chatbot behavior is controlled via chatbot_config.json, including:

System instructions

Model selection

Temperature and token limits

Welcome and fallback messages

Domain constraints (restaurant-only responses)

This allows easy reuse of the same backend for:

Customer support bots

Travel assistants

Educational tutors

Other domain-specific chatbots

No backend code changes are required to alter chatbot behavior.

API Endpoints
GET /

Serves the chatbot frontend.

POST /chatbot

Handles chatbot interaction.

Request body:

{
  "prompt": "What dishes do you serve for dinner?"
}


Response:

Plain text chatbot reply

Setup Instructions
1. Clone the repository
git clone <repository-url>
cd LLM_application_chatbot

2. Create and activate virtual environment
python -m venv env
env\Scripts\activate    # Windows

3. Install dependencies
pip install -r requirements.txt

4. Set environment variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here

Running the Application
flask run


The app will be available at:

http://127.0.0.1:5000

Current Limitations

Conversation history is stored in memory (single-session)

Not designed for concurrent multi-user production use

No persistent database storage yet

These limitations are intentional for simplicity and clarity in a portfolio project.

Planned Improvements

Session-based conversation memory

Streaming responses

Redis-backed persistence

Tool/function calling (menu lookup, reservations)

Rate limiting and logging

Docker support

Why This Project

This project was built to demonstrate:

Practical LLM integration (beyond tutorials)

Clean backend architecture

Configurable system design

Real-world debugging and dependency management

Readable, maintainable Python code

Author

Muhammad Safwan