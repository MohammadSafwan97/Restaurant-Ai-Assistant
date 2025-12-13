from flask import Flask, request, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import json

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from services.menu_service import (
    find_dish,
    get_dish_details,
    get_menu,
    get_hours,
    get_location
)

from services.order_service import (
    add_item,
    remove_item,
    view_order,
    checkout
)

load_dotenv()

with open("data/chatbot_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

app = Flask(__name__)
CORS(app)

llm = ChatOpenAI(
    model=config["model"],
    temperature=config["temperature"],
    max_tokens=config["max_tokens"]
)

conversation_history = []


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json(force=True)
    user_text = data.get("prompt", "").strip().lower()

    # MENU
    if "breakfast" in user_text:
        return f"Our breakfast menu includes: {', '.join(get_menu('breakfast').keys())}."
    if "lunch" in user_text:
        return f"Our lunch menu includes: {', '.join(get_menu('lunch').keys())}."
    if "dinner" in user_text:
        return f"Our dinner menu includes: {', '.join(get_menu('dinner').keys())}."

    # HOURS / LOCATION
    if "hours" in user_text or "timing" in user_text:
        h = get_hours()
        return f"Breakfast: {h['breakfast']}, Lunch: {h['lunch']}, Dinner: {h['dinner']}."

    if "location" in user_text or "where" in user_text:
        return f"We are located in {get_location()}."

    # DISH CONTEXT
    dish, details = find_dish(user_text)
    if dish and "add" not in user_text:
        return (
            f"🍽️ {dish}\n"
            f"Price: Rs {details['price']}\n"
            f"Portion: {details['portion']}\n"
            f"Serves: {details['serves']}\n"
            f"Spice Level: {details['spice_level']}"
        )

    # ORDER
    if user_text.startswith("add"):
        return add_item(dish, details)

    if user_text.startswith("remove"):
        return remove_item(dish)

    if "my order" in user_text:
        return view_order()

    if "checkout" in user_text or "receipt" in user_text:
        return checkout()

    # AI FALLBACK (LAST)
    conversation_history.append(HumanMessage(content=user_text))
    response = llm.invoke([
        SystemMessage(content=config["description"]),
        *conversation_history
    ])
    conversation_history.append(AIMessage(content=response.content))
    return response.content


if __name__ == "__main__":
    app.run(debug=True)
