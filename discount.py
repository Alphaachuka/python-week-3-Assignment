# calculate discount based on the given percentage

def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        actual_price = price * (1 - discount_percentage / 100)
    else:
        discount_percentage < 20
        actual_price = price  # no discount applied
    return actual_price

calculate_final_price = input("Enter the price of the item: ")
price = float(calculate_final_price)
discount_percentage = float(input("Enter the discount percentage: "))
final_price = calculate_discount(price, discount_percentage)
print(f"The final price after discount is: {final_price}")

# This code calculates the final price after applying a discount based on the given percentage.
# If the discount percentage is 20% or more, it applies the discount; otherwise, it keeps the original price.
