#this uses dictionary while loops and if conditions

#setting variable
menu={'meat':5.95,'hawaiian':4.95,'vegdelight':3.95,'big mac':6.95,'mcflurry':3.59}
name = ""
more = "s"
qty = int(0)
total = 0

print('Welcome to pizza haven')
print('please place order from the following menu')
with open ('pizzamenu.txt', 'r') as f:
    read_content = f.read()
    print(read_content)
##f = open('pizzamenu.txt' , 'r')
##print(f.read())
##f.close()

print('')

name = input("Enter your name : ")



while more != 'n':


    item = input('Enter item name : ')
    if item not in menu:
        print('this item is not in menu')
        item = input('Enter item Name : ')
        try:
            qty = int(input('Enter quantity required : '))

        except ValueError:
            print('please enter positive numbers only')
            qty = int(input('Enter quantity required : '))
        price = menu[item]
        linetotal=price*qty
        total = total+linetotal

        print('your total is : ${:.2f}'.format(total))
        more = input('would you like another item : ')
        if more == "no":
            print("Thank you for eating at pizza haven!")
            exit()
