Menu=True
inventory = {}
def add(name,price,quantity):
    info = {"price":int(price), "quantity":int(quantity)}
    inventory[name]=info
    print(f"{name} has been successfully added!")

while Menu:
    print("="*50)
    print("Bienvenido a tu inventario!")
    print("1. Añadir productos")
    print("2. Consultar productos")
    print("3. Actualizar precios")
    print("4. Eliminar productos")
    print("5. Calcular el valor total del inventario")
    print("6. Salir")
    print("="*50)
    option = input("Selecciona una opción: 1/2/3/4/5/6: ")
    if option == "1":
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
    if option == "2":
        print(inventory)