import modules.inventory as inv

def sell_stock(item, quantity, selling_price):
    item = item.lower()

    if item not in inv.inventory:
        return "❌ Item not found!"

    if quantity > inv.inventory[item]["quantity"]:
        return "❌ Not enough stock!"

    inv.inventory[item]["quantity"] -= quantity

    revenue = quantity * selling_price
    cost = quantity * inv.inventory[item]["cost_price"]
    profit = revenue - cost

    # ✅ Correct way to update global variable
    inv.total_profit += profit

    remaining = inv.inventory[item]["quantity"]

    return f"✅ Revenue: ₹{revenue} | Profit: ₹{profit} | Remaining: {remaining} kg"