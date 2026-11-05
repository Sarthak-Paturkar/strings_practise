##Take a product name, quantity and price. Display a formatted bill showing the total amount.
product_name = input("Enter the name of product: ")
quantity = int(input("Enter the quantity: "))
price = int(input("Enter the price: "))
print(f"Purchased item: {product_name}")
print(f"Total items purchased: {quantity}")
print(f"Price of one item: {price}")
print(f"Total Price: {price * quantity}")
