
#Idea, hacer otra lista con el valor total de cada producto, luego sumar cada valor e imprimirlo

products = [] #Lista de todos los productos, precios, cantidad y descuento
checkout = [] #Lista para ingresar el valor total de cada producto
items = [] #Lista de sólo el nombre de cada producto

print("====================================")
print("Welcome to your purchase list")
menu = True
while menu:
    print("====================================")
    print("What would you like to do?: ")
    print("1. Add products")
    print("2. Checkout")
    option = input("Select an option: 1/2> ")
    if option == "1":
        initiate = True
        while initiate: #Bucle para pedir más de un producto
            new_item = []
            print("Enter the name of the product: ")

            while True: #Bucle while en caso de que el ususario ingrese un número en vez de texto.
                product = input() 
                if product.isalpha():
                    break
                else:
                    print("Please enter a valid product name")

            while True: #Bucle while en caso de que el ususario ingrese un texto en vez de un número
                price = input("Please enter the price of the product: ") #Recibimos el precio del producto
                if price.isdigit():
                    price = float(price) #Convertimos el input en float para poder usarlo en una opración posterior
                    break
                else:
                    print("Please enter a valid price")

            while price < 0:  #Creamos un bucle while en caso de recibir un precio no válido
                print("Please enter a valid price:")
                price = float(input())


            while True: #Bucle while en caso de que el ususario ingrese un texto en vez de un número
                quantity = input("Enter the total amount of products you have bought: ") #Recibimos la cantidad del producto
                if quantity.isdigit():
                    quantity = int(quantity) 
                    break
                else:
                    print("Please enter a valid quantity")

            while quantity < 0:   #Creamos un bucle while en caso de recibir una cantidad no válida
                print("Please enter a valid quantity")
                quantity = int(input())

            while True:
                discount = input("Enter the total discount percentage: ") #Recibimos el descuento del producto
                if discount.isdigit():
                    discount = float(discount) #Convertimos el input en float para poder usarlo en una operación posterior
                    break
                else:
                    print("Please enter a valid discount percentage")

            while discount < 0 or discount > 100:     #Creamos un bucle while en caso de recibir un descuento por debajo de 0 o por encima de 100
                print("Please enter a discount within 0 and 100%")
                discount = float(input())
            new_item = [product, price, quantity, discount]
            products.append(new_item)
            subtotal = price*quantity - (price*(discount/100)*quantity) #Hice esta operación para guardar el precio total de un producto incluyendo el descuento en una variable
            checkout.append(subtotal)   #Guardamos el subtotal de cada producto en una lista.
            items.append(product)
            reset = input("Would you like to add another product? Y/N > ")
            if reset.upper() == "N":
                print("====================================")
                print(products)
                print(f"You have bought {len(products)} items in total.")
                initiate = False
    if option == "2":

        print("====================================")    
        Total = sum(checkout) 

        receipt = dict(zip(items, checkout)) #Creamos un diccionario para almacenar los pares de item:valor
        for key, value in receipt.items():
            print(f"Product: {key} ------------- Price: ${value:.2f}")
            
        
        if Total > 0:  #Creamos un IF en caso de que el precio total sea igual a cero o no para dar un mensaje especial.
            print("====================================")
            print(f"The total price of your purchase is: ${Total:.2f}") #Imprimimos el resultado en pantalla, mostrando el Total con 2 decimales
            print("====================================")
        else:
            print("Your purchase is free!")
            print("====================================") 
        menu = False
