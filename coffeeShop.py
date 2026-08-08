print("******************************")
print("Welcome to the coffee shop🤗")
    #  Menu of the shop
print('/nMenu')
print('1.Espresso = pkr.1500')
print('2.cappuccino = pkr.1800')
print('3.Latte = pkr.1200')
print('4.Americano = pkr.1500')

bill = 0
choice= int(input('\nEnter coffee number from (1-4):'))
qty = int(input('enter the quantity:'))

if choice ==1:
    coffee= 'Espresso'
    price=1500
elif choice==2:
    coffee='cappuccino'
    price=1800
elif choice==3:
    coffee='Latte'
    price=1200
elif choice==4:
    coffee='Americano'
    price=1500
else:
    print('invalid error')

bill = price* qty
print("=========Bill===========")
print("coffee:",coffee)
print("price:",price)
print("quantity:",qty)
print("subtotal:pkr" , bill)
