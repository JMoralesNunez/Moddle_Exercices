menu = True
grades = []
print("Welcome to the grades program!")
while menu:
    print("===============================================")
    print("1. Enter your grade and validate if you passed.")
    print("2. Calculate average on list.")
    print("3. Count grades above a value.")
    print("4. Verify the average of a grades list.")
    print("5. Add more grades to the list.")
    print("6. Exit")
    print("===============================================")
    print("===============================================")
    while True:       #Bucle while para asegurarse de recibir la opción correcta
        option = input("Select an option 1/2/3/4/5/6: ")
        if option.isdigit() and int(option) >= 1 and int(option) <= 6:
            break
        else:
            print("Please enter a valid option")
    if option == "1":
        while True: #Bucle while para asegurarse de recibir el dato correcta
            grade = input("Enter your grade (0-100): ")
            if grade.isdigit() and int(grade) <= 100:
                break
            else:
                print("Please enter a valid grade")
        grade = int(grade)
        if grade >= 65:  #If para confirmar si la nota ingresada aprueba o no
            print("===============================================")
            print("Congrats! You have passed")
        elif grade >= 0 and grade <65:
            print("===============================================")
            print("Sorry, you have failed!")
        else:
            print("===============================================")
            print("Enter a valid item")
    if option == "2":
        print("The grades list have been reset")
        while True: #Bucle para validar que los datos ingresados por el usuario sean enteros y dentro del rango requerido
            grades_input = input("Enter the grades you would like to calculate, separated with commas: ")
            grades_input = grades_input.replace(" ", "")
            grades = grades_input.split(",")
            valid = True
            for grade in grades:
                if not grade.isdigit() or not (0 <= int(grade) <= 100):
                    print(f"'{grade}' is not a valid grade. Please enter numbers between 0 and 100.")
                    valid = False
                    break
            if valid:
                break
        converterList = []  
        for item in grades:   #bucle for para convertir los datos str en grades a int, para ingresarlos a una lista temporal
            item = int(item)
            converterList.append(item)
        grades = converterList  #reasignamos los valores convertidos a int a la lista principal grades
        addition = 0
        for i in grades: #Bucle for para calcular el promedio de la lista grades
            addition += i
        average = addition/len(grades)
        print(f"The grades you have entered are: {grades}")
        print(f"According to your grades, your average is: {average:.2f}")
    if option == "3":
        if not grades:
            print("Please create a list of grades using the option 2")
            continue
        while True:  #Bucle while para asegurarse de recibir el dato correcto
            compare = input("Enter the grade you would like to compare: ")
            if compare.isdigit() and int(compare) <= 100 and int(compare) >= 0:
                break
            else:
                print("Enter a valid grade.")
        compare = int(compare) 
        counter = 0 #Iniciamos un contador
        initiate = True
        while initiate:  #Bucle while para contar las cuantas notas dentro de la lista "grades" son mayores que "compare"
            for item in grades:
                if compare < item:
                    counter += 1
            initiate = False
        print(f"There is a total of ({counter}) grades above the grade you entered")
    if option == "4":
        if not grades:
            print("Please create a list of grades using the option 2")
            continue
        while True: #Bucle while para asegurarse de recibir el dato correcto
            count = input("Enter the grade you would like to check its appereances within the list: ")
            if count.isdigit() and int(count) <= 100 and int(count) >= 0:
                break
            else:
                print("Enter a valid grade.")
        count = int(count)
        counter2 = 0 #iniciamos contador
        for item in grades: #Bucle for para contar las apariciones de "count" en la lista "grades"
            if count == item:
                counter2 += 1
                continue
        if counter2 > 0:
            print(f"The grade: {count} has appeared a total of {counter2} times.")
        else:
            print("The grade cannot be found in the list")
    if option == "5":  #Agregué esta función para que el usuario agregara más notas a la lista creada con la opción 2, en caso de requerirlo
            print(f"The current grades are: {grades}")
            while True:  #Bucle de validación de notas, es el mismo de la opción 2 básicamente
                grades_input = input("Enter the grade(s) you would like to add, separated with commas: ")
                grades_input = grades_input.replace(" ", "")
                add_grades = grades_input.split(",")
                valid = True
                for grade in add_grades:
                    if not grade.isdigit() or not (0 <= int(grade) <= 100):
                        print(f"'{grade}' is not a valid grade. Please enter numbers between 0 and 100.")
                        valid = False
                        break
                if valid:
                    break
            converter = []  
            for item in add_grades:   
                item = int(item)
                converterList.append(item)
            add_grades = converter
            grades += add_grades  #Con esto se agregan las notas añadidas en esta opción, a la lista general de notas
            print("grade(s) have been successfully added:")
            print(f"The new grades list is {grades}")
    if option == "6":
        print("See you later!")
        menu = False
    
