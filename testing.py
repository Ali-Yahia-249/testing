def calculate_total(price, quantity):
    tax_rate = 0.05
    # Intentional Error 1: Using 'tax' instead of 'tax_rate' (NameError)
    total = (price * quantity) + (price * quantity * tax)
    return total

# Intentional Error 2: Passing a string instead of an integer/float for quantity (TypeError)
item_price = 19.99
item_quantity = "two"

final_price = calculate_total(item_price, item_quantity)

# Intentional Error 3: Trying to concatenate a string and a float directly without conversion (TypeError)
print("The final total is: " + final_price)
