def calculate_item_total(price, quantity):
    return price * quantity

def apply_discount(total, discount_percentage):
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Invalid discount percentage")
    return total - (total * discount_percentage / 100)

def calculate_order_total(cart, discount_percentage):
    total = 0
    for item in cart:
        item_total = calculate_item_total(item['price'], item['quantity'])
        print(f"Item: {item['name']}, Total: {item_total}")  # debug here
        total += item_total

    # BUG: wrong variable used - should be discount_percentage
    discounted_total = apply_discount(total, item['discount'])
    return discounted_total

if __name__ == "__main__":
    cart = [
        {"name": "Apple", "price": 0.5, "quantity": 10, "discount": 10},
        {"name": "Banana", "price": 0.2, "quantity": 30, "discount": 10},
        {"name": "Chocolate", "price": 2.0, "quantity": 3, "discount": 10},
    ]
    discount = 15  # This should be used, but there's a bug in the code

    try:
        total = calculate_order_total(cart, discount)
        print(f"Final total after discount: ${total:.2f}")
    except Exception as e:
        print("Error calculating order total:", e)
