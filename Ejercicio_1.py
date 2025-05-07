suma_total = 0
# Pedimos los 5 números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
numero4 = int(input("Ingrese el cuarto número: "))
numero5 = int(input("Ingrese el quinto número: "))

# lista numeros ingresados
numeros = [numero1, numero2, numero3, numero4, numero5]

# suma cada numero
for numero in numeros:
    # sumar el numero a la suma total que va hasta el momento
    suma_total += numero
    
      # Verificar si el número es positivo
    if numero > 0:
        print(f"{numero} es positivo.")
    else:
        print(f"{numero} no es positivo.")
    
    # Verificar si el número es par
    if numero % 2 == 0:
        print(f"{numero} es par.")
    else:
        print(f"{numero} no es par.")

# Mostrar la suma total de los 5 números
print(f"La suma total de los números ingresados es: {suma_total}")
