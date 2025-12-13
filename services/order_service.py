current_order = []


def add_item(name, details):
    for item in current_order:
        if item["name"] == name:
            item["quantity"] += 1
            return f"✅ {name} quantity updated to {item['quantity']}."

    current_order.append({
        "name": name,
        "price": details["price"],
        "quantity": 1
    })
    return f"✅ {name} added to your order (Rs {details['price']})."


def remove_item(name):
    global current_order
    current_order = [item for item in current_order if item["name"] != name]
    return f"❌ {name} removed from your order."


def view_order():
    if not current_order:
        return "🛒 Your order is currently empty."

    total = 0
    response = "🛒 Your current order:\n\n"

    for item in current_order:
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        response += f"{item['name']} x{item['quantity']} — Rs {subtotal}\n"

    response += f"\n💰 Total: Rs {total}"
    return response


def checkout():
    receipt = "🧾 Safwan Restaurant Receipt\n\n"
    receipt += view_order()
    receipt += "\n\n🙏 Thank you for dining with us!"
    current_order.clear()
    return receipt
