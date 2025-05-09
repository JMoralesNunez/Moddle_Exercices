Menu=True
inventory = {}
def add(name,price,quantity):  #Función para agregar los productos al inventario, de forma que el nombre del producto sea la clave, y el precio y cantidad sean el valor como diccionario
    info = {"price":float(price), "quantity":int(quantity)}
    inventory[name.capitalize()]=info
    print(f"{name} has been successfully added!")
def show(): #Función para mostrar los elementos del inventario
    for product,info in inventory.items():
        print(f"{product}.................. Price: ${info['price']} | Quantity: {info['quantity']}")
def search_item(name): #Función para buscar un producto por su nombre
    format=inventory.get(name)
    if format == None:  
        print("Item not found")
    else:
        print(f"Name: {name}, Price: {format["price"]}, Quantity: {format["quantity"]}")
def update(name, newprice): #función para actualizar el precio de un producto
    inventory[name]["price"] = newprice
def delete(name): #Función para eliminar un producto y su información
    inventory.pop(name)
    print(f"{name} has been successfully deleted")

while Menu:  #Bucle para mostrar el menu principal
    print("="*50)
    print("Welcome to your inventory!")
    print("1. Add products")
    print("2. See products")
    print("3. Search for a product")
    print("4. Update prices")
    print("5. Delete products")
    print("6. Check total value of inventory")
    print("7. Exit")
    print("="*50)
    while True: #Bucle para validar la opción correcta
        option = input("Select an option: 1/2/3/4/5/6/7: ")
        if option.isdigit() and int(option) >= 1 and int(option) <=7:
            break
        else:
            print("Enter a valid option")
    if option == "1":
        while True: #Bucle para seguir agregando productos
            while True: #Bucle para validar la entrada del nombre del producto  
                name = input("Enter the name of the product: ")
                if name.isalpha() and name not in inventory.keys(): #Si el producto ya está en el inventario, no lo deja añadir de nuevo, pues sobreescribiria el anterior
                    break
                else:
                    print("The item name is not valid or the item is already on the inventory")
            while True: 
                try: #Try para validar la entrada el precio del producto, en caso contrario, seguirá en el bucle
                    price = float(input("Enter the price of the product: "))
                    if price >= 0.0:
                        break
                    else:
                        print("Invalid price, try again")
                except:
                    print("Enter a valid price")
            while True: #Validación de entrada de cantidad 
                quantity = input("Enter the quantity of the product: ")
                if quantity.isdigit() and int(quantity) > 0:
                    break
                else:
                    print("Please enter a valid quantity")
            add(name, price, quantity)
            while True: #Validación de reseteo de bucle para añadir productos
                reset = input("Would you like to add another product? 1.Yes/2.No: ")
                if reset.isdigit()==False:
                    print("Please enter a valid option(1/2)")
                elif int(reset) != 1 and int(reset) != 2:
                    print("Please enter a valid option(1/2)")
                else:
                    break
            if int(reset) == 2:
                break
    if option == "2":
        if not inventory: # En caso de que no haya productos en el inventario todavía
            print("No items in inventory yet")
        show()
    if option == "3":
        while True: #Validación del nombre de producto a buscar
            name_search = input("Enter the name of the product you are searching: ")
            if name_search.isalpha():
                name_search=name_search.capitalize()
                break
            else:
                print("Please enter a valid name")
        search_item(name_search)
    if option == "4":
        while True: #Validación del nombre de producto a cambiar el precio
            name_price = input("Enter the name of the product you would like to change its price: ")
            if name_price.isalpha() and name_price.capitalize() in inventory.keys():
                name_price=name_price.capitalize()
                break
            else:
                print("Please enter a valid name or the name of an item inside the inventory")
        while True: #Validación del nuevo precio
            try:
                newprice = float(input("Enter the new price of the product: "))
                if newprice >= 0.0:
                    break
                else:
                    print("Invalid price, try again")
            except:
                print("Enter a valid price")
        update(name_price,newprice)
        print(f"The price of {name} has been updated")
    if option == "5":
        while True: #Validación del producto a eliminar
            name_deletion = input("Enter the name of the product you would like delete: ")
            if name_deletion.isalpha() and name_deletion.capitalize() in inventory.keys():
                name_deletion=name_deletion.capitalize()
                break
            else:
                print("Please enter a valid item")
        delete(name_deletion)
    if option == "6":
        total_prices = dict(map(lambda item: (item[0], item[1]["price"] * item[1]["quantity"]), inventory.items())) #lambda consigue la key del inventario, que es el nombre, y multiplica el precio por la cantidad y lo deja como clave;
                                                                                                                    #esto queda dentro de una tupla con .items(). map() ejecuta lo anterior con cada producto del inventario. y Dict() deja todo en un Diccionario nuevo
        for item,price in total_prices.items(): #bucle for para mostrar el nombre y valor total de cada producto
            print(f"{item}................... Total price: ${price}")
        total=0
        for value in total_prices.values(): #bucle for para sumar el precio total de cada producto y sacar el valor total del inventario
            total += value
        print(f"The total price of all products in the inventory is: ${total}")
    if option == "7": #Opción para terminar el bucle del menu y terminar el programa
        print("Thanks for coming!")
        Menu=False
