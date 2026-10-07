# receipt

from pyscript import document


def calculate_receipt(order_items):
    subtotal = 0.0

    for name, price, qty in order_items:
        item_total = price * qty
        subtotal += item_total

    vat = subtotal * 0.12
    total_amount = subtotal + vat

    return subtotal, vat, total_amount


def generate_receipt(event):

    order = []

    if document.getElementById("friedChicken").checked:
        qty = int(document.getElementById("qtyFriedChicken").value)
        order.append(("Fried Chicken", 120.00, qty))

    if document.getElementById("chickenBurger").checked:
        qty = int(document.getElementById("qtyChickenBurger").value)
        order.append(("Chicken Burger", 150.00, qty))

    if document.getElementById("chickenNuggets").checked:
        qty = int(document.getElementById("qtyChickenNuggets").value)
        order.append(("Chicken Nuggets", 180.00, qty))

    if document.getElementById("chickenMeal").checked:
        qty = int(document.getElementById("qtyChickenMeal").value)
        order.append(("Chicken Meal", 210.00, qty))

    if len(order) == 0:
        document.getElementById("receiptItems").innerHTML = "Please select an item."
        document.getElementById("receipt").style.display = "block"
        return

    subtotal, vat, total_amount = calculate_receipt(order)

    receipt_items = ""

    for name, price, qty in order:
        item_total = price * qty

        receipt_items += f"""
        <div class="receipt-row">
            <span>{name} (x{qty})</span>
            <span>₱{item_total:.2f}</span>
        </div>
        """

    document.getElementById("receiptItems").innerHTML = receipt_items
    document.getElementById("subtotal").innerHTML = f"₱{subtotal:.2f}"
    document.getElementById("vat").innerHTML = f"₱{vat:.2f}"
    document.getElementById("totalAmount").innerHTML = f"₱{total_amount:.2f}"

    document.getElementById("receipt").style.display = "block"