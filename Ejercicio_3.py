def contar_vocales():
    # pedir una palabra
    palabra = input("ingrese una palabra: ")

    # contadores en ceros
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0

    # buscar letras en la palabra
    for letra in palabra:
        # Ver si la letra es vocal y si es su mayuscula
        if letra == 'a' or letra == 'A':
            contador_a += 1
        elif letra == 'e' or letra == 'E':
            contador_e += 1
        elif letra == 'i' or letra == 'I':
            contador_i += 1
        elif letra == 'o' or letra == 'O':
            contador_o += 1
        elif letra == 'u' or letra == 'U':
            contador_u += 1

    # Mostrar el total de vocales encontradas y la respectiva de cada una
    total_vocales = contador_a + contador_e + contador_i + contador_o + contador_u
    print(f"Total de vocales: {total_vocales}")
    print(f"A: {contador_a}, E: {contador_e}, I: {contador_i}, O: {contador_o}, U: {contador_u}")

# Llamar a la función
contar_vocales()
