import json

with open("data/restaurant_data.json", "r", encoding="utf-8") as f:
    restaurant_data = json.load(f)

last_dish_context = None


def find_dish(text):
    global last_dish_context
    text = text.lower()

    for meal in restaurant_data["menu"].values():
        for dish, details in meal.items():
            if dish.lower() in text:
                last_dish_context = dish
                return dish, details
    return None, None


def get_dish_details():
    if not last_dish_context:
        return None
    for meal in restaurant_data["menu"].values():
        if last_dish_context in meal:
            return meal[last_dish_context]
    return None


def get_menu(meal_type):
    return restaurant_data["menu"].get(meal_type, {})


def get_hours():
    return restaurant_data["hours"]


def get_location():
    return restaurant_data["location"]
