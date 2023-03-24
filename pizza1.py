#this program takes orders from user and displays invoice

name = ""
order = int(0)
Meatlovers = 9.95
Hawaiian = 4.95
Vegdelight = 5.95
print("##############toppings##############")
Pepperoni = 0.50
Onions = 0.50
Mushrooms = 0.50
Cheese = 0.50
Tomatos = 0.50
total = 0


print("########################################")
print("Welcome to pizza heaven!")
print("Please place orders from the following menu")
print("")
print("meatlovers:", Meatlovers)
print("hawaiian:", Hawaiian)
print("vegdelight:", Vegdelight)
print("pepperoni:", Pepperoni)
print("onions:", Onions)
print("cheese:", Cheese)
print("mushrooms:", Mushrooms)
print("tomatos:", Tomatos)
print("Enter 1 for meatlovers, 2 for hawaiian, 3 for vegdelight, 4 for pepperoni, 5 for onions, 6 for cheese, 7 for mushrooms, 8 for tomatos, and 0 to finish order")


name = input("What is your name? : ")
order = int(input("Enter any number between 1 and 3 : "))




while order != 0:

    if order == 1:
        total = total + 9.95
        order = int(input("What is your order? "))
        print("{:.2f}".format(total))

    if order == 2:
        total = total + 4.95
        order = int(input("What is your order? "))
        print("{:.2f}".format(total))

    if order == 3:
        total = total + 5.95
        order = int(input("What is your order? "))
        print("{:.2f}".format(total))

    if order == 4:
        total = total + 0.50
        order = int(input("What is your order? "))
        print("{:.2f}".format(total))

    if order == 5:
        total = total + 0.50
        order = int(input("What is your order? "))
        print("{:.2f}".format(total))

    if order == 6:
        total = total + 0.50
        order = int(input("What is your order? "))
        print("{:.2f}".format(total))

    if order == 7:
        total = total + 0.50
        order = int(input("What is your order? "))
        print("{:.2f}".format(total))

    if order == 8:
        total = total + 0.50
        order = int(input("What is your order? "))
        print("{:.2f}".format(total))

    if order <0 or order > 8:
        order = int(input("Enter any number between 1 and 8 or 0 to finish order : "))

print("your total is: ${:.2f}" .format(total))


print(name, ", your order will be ready in 5 minutes")
