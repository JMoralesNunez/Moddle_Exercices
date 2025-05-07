Menu=True
inventory = {}
def add(name,price,quantity):
    info = {"price":int(price), "quantity":int(quantity)}
    inventory[name]=info
    print(f"{name} has been successfully added!")
def show():
    for product,info in inventory.items():
        print(f"{product}.................. price: {info['price']} Quantity: {info['quantity']}")
def update(name, newprice):
    inventory[name]["price"] = newprice

while Menu:
    print("="*50)
    print("Welcome to your inventory!")
    print("1. Add products")
    print("2. See products")
    print("3. Update prices")
    print("4. Delete products")
    print("5. Check total value of inventory")
    print("6. Exit")
    print("="*50)
    option = input("Selecciona una opción: 1/2/3/4/5/6: ")
    if option == "1":
        while True:
            while True:
                name = input("Enter the name of the product: ")
                if name.isalpha():
                    break
                else:
                    print("Please enter a valid name")
            while True:
                price = input("Enter the price of the product: ")
                if price.isdigit() and int(price) > 0:
                    break
                else:
                    print("Please enter a valid price")
            while True:
                quantity = input("Enter the quantity of the product: ")
                if quantity.isdigit() and int(quantity) > 0:
                    break
                else:
                    print("Please enter a valid quantity")
            add(name, price, quantity)
            reset = input("Would you like to add another product? 1.Yes/2.No: ")
            if reset.isdigit() and int(reset) == 2:
                break
    if option == "2":
        show()
    if option == "3":
        while True:
            name = input("Enter the name of the product you would like to change its price: ")
            if name.isalpha() and name in inventory.keys():
                break
            else:
                print("Please enter a valid name")
        while True:
            newprice = input("Enter the new price of the product: ")
            if newprice.isdigit() and int(newprice) > 0:
                break
            else:
                print("Please enter a valid price")
        update(name,newprice)
        print(f"The price of {name} has been updated")