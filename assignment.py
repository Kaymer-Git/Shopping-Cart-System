products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
price = [2, 2.5, 1.5, 3, 1, 5]
shopping_cart = []
check_out = False
def main_menu():
    print("========== KAYMER'S SHOPPING CART ==========")
    print("")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")
    print("")
    return int(input("Enter your choice: "))
def choice_1():
    print("========== AVAILABLE PRODUCTS ==========")
    print("")
    n = 1
    for p in products:
        print(n, p, " " * (8-len(p)), ":$", price[n - 1])
        n += 1
    print("")
def choice_2():
    print("Which product would you like to add?")
    print("")
    n = 1
    for p in products:
        print(n, p)
        n += 1
    print("")
    add_products = int(input("Enter product number: "))
    if add_products == 1:
        shopping_cart.append(products[int(add_products) - 1])
    elif add_products == 2:
        shopping_cart.append(products[int(add_products) - 1])
    elif add_products == 3:
        shopping_cart.append(products[int(add_products) - 1])
    elif add_products == 4:
        shopping_cart.append(products[int(add_products) - 1])
    elif add_products == 5:
        shopping_cart.append(products[int(add_products) - 1])
    elif add_products == 6:
        shopping_cart.append(products[int(add_products) - 1])
    else:
        print("Invalid product!")
        print("Please choose a number between 1 and 6.")
    print("")
    if add_products >= 1 and add_products <= 6:
        print(products[int(add_products) - 1], "was added to your cart!")
def choice_3():
    print("========== YOUR SHOPPING CART ==========")
    print("")
    n = 1
    for s in shopping_cart:
        print(n, s)
        n += 1
    print("")
while check_out == False:
    choice = main_menu()
    print("")
    if choice == 1:
        choice_1()
    elif choice == 2:
        choice_2()
    elif choice == 3:
        choice_3()