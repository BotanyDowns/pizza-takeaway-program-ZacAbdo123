
#setting variables
name = ""
order = int(0)
meat_lovers = 9.95
hawaiian = 4.95
veg_delight = 5.95
total = 0

print('Welcome to Pizza Haven')
print('please order from the following menu')

print("Meat Lovers", meat_lovers)
print("Hawaiian:", hawaiian)
print("Veg Delight", veg_delight)
print("enter 1 for meat lovers, 2 for hawaiian, 3 for veg delight")

name = input("Enter your name : ")

while True:
    try:
        order = int(input("enter 1 for meat lovers, 2 for hawaiian, 3 for veg delight"))
        while order !=0:
            if order <0 or order >3:
                order = int(input("enter 1 for meat lovers, 2 for hawaiian, 3 for veg delight"))

                if order ==1:
                    total = total+9.95
                    order = int(input('what is your order'))

                if order ==2:
                    total = total+4.95
                    order = int(input('what is your order'))

                if order ==3:
                    total = total+5.95
                    order = int(input('what is your order'))

                print('your total is : ${:.2f}'.format(total))
                break

            except ValueError:
                print('please enter positive number')
        
