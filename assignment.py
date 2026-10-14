products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
price = [2, 2.5, 1.5, 3, 1, 5]
shopping_cart = []

print("========== SMART SHOPPING CART ==========")
print("")
print("1. View Available Products")
print("2. Add Product to Cart")
print("3. Remove Product from Cart")
print("4. View Shopping Cart")
print("5. View Current Total")
print("6. Checkout")
print("")
choice = input("Enter your choice: ")

if choice == "1":
    print("========== AVAILABLE PRODUCTS ==========")
    print("")
    n = 1
    for p in products:
        print(n, p, " " * (8-len(p)), ":$", price[n - 1])
        n += 1