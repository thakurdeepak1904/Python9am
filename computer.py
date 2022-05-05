print('Welcome to Computer Bazaar')
print('We have:\n 1. Dell(20000)\n 2. Toshiva(30000)\n 3. Mac(50000)')
total_price = 0
while True:
    select_Laptop = int(input("Enter option you want to buy: "))
    if select_Laptop == 1:
        initial_price = 20000
        quantity = int(input("How many laptop you want to buy: "))
        laptop_price = initial_price * quantity
        break
    elif select_Laptop == 2:
        initial_price = 30000
        quantity = int(input("How many laptop you want to buy: "))
        laptop_price = initial_price * quantity
        break
    elif select_Laptop == 3:
        initial_price = 50000
        quantity = int(input("How many laptop you want to buy: "))
        laptop_price = initial_price * quantity
        break
    else:
        print("Choose a valid option.")
print('Delivery Option: \n 1.Home Delivery (1000) \n 2.Self Pickup (Free)')
while True:
    delivery = int(input('Enter option for delivery Type: '))
    delivery_price = 0
    if delivery == 1:
        delivery_price += 1000
        break
    elif delivery == 2:
        break
    else:
        print('Enter a vaild option')

print('Packing Option: \n 1.Plastic (500) \n 2.Bag (1000) \n 3.Gift Packing (5000) \n 4.None')
while True:
    packing = int(input('Enter packing option: '))
    packing_price = 0
    if packing == 1:
        packing_price = quantity * 500
        break
    elif packing == 2:
        packing_price = quantity * 1000
        break
    elif packing == 3:
        packing_price = quantity * 5000
        break
    elif packing == 4:
        break
    else:
        print('Enter a valid option')

location = input('Enter your address. e.g: ktm,bkt,ltp: ')
vat_price = 0
if location == 'ktm':
    vat_price = laptop_price * 0.13
else:
    pass
Total_price = laptop_price + delivery_price + packing_price + vat_price
print(f'Quantity: {quantity}, Total Price: {laptop_price}, Tax price: {vat_price}, Grand Total: {Total_price}')

