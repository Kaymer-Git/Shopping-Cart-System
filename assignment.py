products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
price = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]
shopping_cart = []
check_out = False
def main_menu():
    print("========== KAYMER'S SHOPPING CART ==========")
    print("")
    print("1 View Available Products")
    print("2 Add Product to Cart")
    print("3 Remove Product from Cart")
    print("4 View Shopping Cart")
    print("5 View Current Total")
    print("6 Checkout")
    print("")
    return int(input("Enter your choice: "))
def choice_1():
    print("========== AVAILABLE PRODUCTS ==========")
    print("")
    n = 0
    for p in products:
        print(n + 1, p, " " * (8-len(p)), ":$", price[n])
        n += 1
    print("")
def choice_2():
    print("Which product would you like to add?")
    print("")
    n = 0
    for p in products:
        print(n + 1, p)
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
        print("Invalid option!")
    print("")
    if add_products >= 1 and add_products <= 6:
        print(products[int(add_products) - 1], "was added to your cart!")
def choice_3():
    print("========== YOUR SHOPPING CART ==========")
    print("")
    if len(shopping_cart) == 0:
        print("Your shopping cart is empty!")
        print("There is nothing to remove.")
        print("")
    else:
        n = 0
        for s in shopping_cart:
            print(n + 1, s)
            n += 1
        print("")
        print("Which item would you like to remove?")
        remove = int(input("Enter item number: "))
        while remove > n:
            print("Invalid option!")
            remove = int(input("Enter item number: "))

            
        print("")
        item_removed = shopping_cart.pop(int(remove) - 1)
        print(item_removed, "was removed from your cart!")
        print("")
def choice_4():
    print("========== YOUR SHOPPING CART ==========")
    print("")
    n = 0
    for s in shopping_cart:
        print(n + 1, s, " " * (8-len(s)), "$", price[products.index(s)])
        n += 1
    print("")
    print("Total items:", len(shopping_cart))
    print("")
def choice_5():
    print("========== CURRENT TOTAL ==========")
    print("")
    n = 0
    for s in shopping_cart:
        print(n + 1, s, " " * (8-len(s)), "$", price[products.index(s)])
        n += 1
    print("")
    total_cost = 0
    for s in shopping_cart:
        total_cost += price[products.index(s)]
    print("Total cost:", total_cost)
    print("")
def choice_6():
    print("========== CHECKOUT ==========")
    print("")
    total_cost = 0
    for s in shopping_cart:
        total_cost += price[products.index(s)]
    print("Subtotal:     $", total_cost)
    if total_cost < 10:
        print("Discount:       No")
    elif total_cost < 20:
        print("Discount:       5%")
    elif total_cost < 40:
        print("Discount:       10%")
    else:
        print("Discount:       15%")
    if total_cost < 10:
        print("Amount Saved: $ 0")
    elif total_cost < 20:
        print("Amount Saved: $", total_cost * 0.05)
    elif total_cost < 40:
        print("Amount Saved: $", total_cost * 0.10)
    else:
        print("Amount Saved: $", total_cost * 0.15)
    print("")
    if total_cost < 10:
        print("Final Total:  ", total_cost)
    elif total_cost < 20:
        print("Final Total:  ", total_cost * 0.95)
    elif total_cost < 40:
        print("Final Total:  ", total_cost * 0.9)
    else:
        print("Final Total:  ", total_cost * 0.85)
while check_out == False:
    choice = main_menu()
    print("")
    if choice == 1:
        choice_1()
    elif choice == 2:
        choice_2()
    elif choice == 3:
        choice_3()
    elif choice == 4:
        choice_4()
    elif choice == 5:
        choice_5()
    elif choice == 6:
        choice_6()
        check_out = True
    else:
        print("Invalid option!")
print("Thank you for shopping :)")