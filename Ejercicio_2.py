def clasificar_edad():  #Definir el nombre de la funcion
    # Leer la entrada
    entrada = input("Por favor, ingrese su edad: ")

    # definir edad como el numero entero que se metió
    edad = int(entrada)

    # definir que la edad no puede ser negativa y definir intervalos
    if edad < 0:
        print("Error: La edad no puede ser negativa.")
    elif edad < 13:
        print("Niño")
    elif 13 <= edad <= 17:
        print("Adolescente")
    elif 18 <= edad <= 59:
        print("Adulto")
    else:
        print("Adulto mayor")

# Llamar a la función
clasificar_edad()