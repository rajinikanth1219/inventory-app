from flask import Flask, render_template, request
from modules.purchase import purchase_stock
from modules.sales import sell_stock
from modules.inventory import get_inventory, get_total_profit

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    message = ""

    if request.method == "POST":
        source = request.form.get("source")
        item = request.form.get("item")
        quantity = request.form.get("quantity")
        cost = request.form.get("cost")

        if not item or not quantity or not cost:
            message = "❌ Please fill all fields"
        else:
            try:
                quantity = int(quantity)
                cost = float(cost)

                message = purchase_stock(source, item, quantity, cost)

            except ValueError:
                message = "❌ Quantity must be number & cost must be valid"

    return render_template("purchase.html", message=message)

@app.route("/sell", methods=["GET", "POST"])
def sell():
    message = ""

    if request.method == "POST":
        item = request.form.get("item")
        quantity = request.form.get("quantity")
        price = request.form.get("price")

        if not item or not quantity or not price:
            message = "❌ Please fill all fields"
        else:
            try:
                quantity = int(quantity)
                price = float(price)

                message = sell_stock(item, quantity, price)

            except ValueError:
                message = "❌ Enter valid numbers"

    return render_template("sell.html", message=message)

@app.route("/inventory")
def inventory():
    data = get_inventory()
    profit = get_total_profit()
    return render_template("inventory.html", inventory=data, total_profit=profit)

if __name__ == "__main__":
    app.run(debug=True)