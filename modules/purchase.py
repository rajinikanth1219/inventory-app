from modules.inventory import inventory

def purchase_stock(source, item, quantity, cost_price):
    item = item.lower()

    if item in inventory:
        old_qty = inventory[item]["quantity"]
        old_cost = inventory[item]["cost_price"]

        new_qty = old_qty + quantity
        new_cost = ((old_qty * old_cost) + (quantity * cost_price)) / new_qty

        inventory[item]["quantity"] = new_qty
        inventory[item]["cost_price"] = new_cost
    else:
        inventory[item] = {
            "quantity": quantity,
            "cost_price": cost_price
        }

    return f"✅ Purchased {quantity} kg of {item} from {source}"