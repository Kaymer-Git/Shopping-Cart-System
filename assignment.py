# import datetime into python
import datetime
# set t to the time right now
t = datetime.datetime.now()
# make time into month/day/year
format_month_date_year = t.strftime("%m/%d/%Y")
# products
products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
# price of every products
price = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]
# users shopping cart
shopping_cart = []
# check if the user checked out to decide if ended the while loop
check_out = False
# make a function of the menu
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
    # return the users choice to decide what function to use
    return int(input("Enter your choice: "))
# the function to look at available products
def choice_1():
    print("========== AVAILABLE PRODUCTS ==========")
    print("")
    # n is the number infront of every product to show how many different products there are
    n = 0
    # this for loop listed every product in the pruducts list
    for p in products:
        # n+1 so the number 1 is infront of the first product, p is the product name, then is the number of spaces needed to make the price are in the same column, last, print out the price of the product, the n here will be the index in the price list
        print(n + 1, p, " " * (8-len(p)), ":$", price[n])
        # add 1 to n so the next pruduct will start with the number 2
        n += 1
    print("")
# function for adding products
def choice_2():
    print("Which product would you like to add?")
    print("")
    # n is the number infront of every product to show how many avaliable items there are
    n = 0
    # this for loop prints out every product
    for p in products:
        print(n + 1, p)
        n += 1
    print("")
    # ask the user which product they want to add
    add_products = int(input("Enter product number: "))
    # add Chips
    if add_products == 1:
        shopping_cart.append(products[int(add_products) - 1])
    # add Soda
    elif add_products == 2:
        shopping_cart.append(products[int(add_products) - 1])
    # add Candy
    elif add_products == 3:
        shopping_cart.append(products[int(add_products) - 1])
    # add Cookies
    elif add_products == 4:
        shopping_cart.append(products[int(add_products) - 1])
    # add Water
    elif add_products == 5:
        shopping_cart.append(products[int(add_products) - 1])
    # add Sandwich
    elif add_products == 6:
        shopping_cart.append(products[int(add_products) - 1])
    # the user cannot enter a number besides 1~6
    else:
        print("Invalid option!")
    print("")
    # if the user enter a accectable number, it will show a message of the item added to the cart
    if add_products >= 1 and add_products <= 6:
        print(products[int(add_products) - 1], "was added to your cart!")
# function for removing items
def choice_3():
    print("========== YOUR SHOPPING CART ==========")
    print("")
    # check if the shopping cart is empty
    if len(shopping_cart) == 0:
        print("Your shopping cart is empty!")
        print("There is nothing to remove.")
        print("")
    # if the shopping cart is not empty
    else:
        # the number before the item in the shopping cart
        n = 0
        # print out everything in the shoppong cart
        for s in shopping_cart:
            # n+1 is the place number of the item in the shopping cart and the item
            print(n + 1, s)
            n += 1
        print("")
        # ask the user what they would like to remove
        print("Which item would you like to remove?")
        # take the users input
        remove = int(input("Enter item number: "))
        # don't let the user enter a numer greater than the number of items in the shopping cart
        while remove > n:
            print("Invalid option!")
            remove = int(input("Enter item number: "))

            
        print("")
        # store and delete the item that the user wnat to delete
        item_removed = shopping_cart.pop(int(remove) - 1)
        # let the user see what has been deleted
        print(item_removed, "was removed from your cart!")
        print("")
# function for showing everything inside the current shopping cart
def choice_4():
    print("========== YOUR SHOPPING CART ==========")
    print("")
    n = 0
    # print the items in the shopping cart
    for s in shopping_cart:
        print(n + 1, s, " " * (8-len(s)), "$", price[products.index(s)])
        n += 1
    print("")
    # print out how many things are in the shopping cart
    print("Total items:", len(shopping_cart))
    print("")
# function for showing the total cost of the current shopping cart
def choice_5():
    print("========== CURRENT TOTAL ==========")
    print("")
    n = 0
    # print out every items in the users shopping cart
    for s in shopping_cart:
        print(n + 1, s, " " * (8-len(s)), "$", price[products.index(s)])
        n += 1
    print("")
    # store the total cost into a variable
    total_cost = 0
    # calculate the total cost by adding the price of everything one by one
    for s in shopping_cart:
        total_cost += price[products.index(s)]
    # print out the total cost
    print("Total cost:", total_cost)
    print("")
# function for receipt and check out
def choice_6():
    print("========== RECEIPT ==========")
    print("")
    # print out the date format from the begining out the program
    print("Date:", format_month_date_year)
    print("")
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
# the while loop that keep the user shopping if not check out
while check_out == False:
    # call the main menu everytime the user selected a choice
    choice = main_menu()
    print("")
    # if the user choose 1, view the avaliable items
    if choice == 1:
        choice_1()
    # if the user choose 2, call the function the add item to the shopping cart
    elif choice == 2:
        choice_2()
    # if the user choose 3, call the function to remove item from the shopping cart
    elif choice == 3:
        choice_3()
    # if the user choose 4, show the items that are currently in their shopping cart
    elif choice == 4:
        choice_4()
    # if the user choose 5, this shows the total price of everything in their current shopping cart
    elif choice == 5:
        choice_5()
    # if the user choose 6, call the function to check out
    elif choice == 6:
        choice_6()
        # after check out is true, the while loop will end
        check_out = True
    # the user cannot enter a number outside of 1~6
    else:
        print("Invalid option!")
# shopping is finished
print("Thank you for shopping :)")