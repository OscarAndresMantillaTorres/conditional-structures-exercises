def verificar_set(juegos_a, juegos_b):
    # Comprobar si los resultados son inválidos
    if juegos_a < 0 or juegos_b < 0:
        return "Invalido"
    if juegos_a > 7 or juegos_b > 7:
        return "Invalido"
    if (juegos_a >= 6 and juegos_a - juegos_b < 2) or (juegos_b >= 6 and juegos_b - juegos_a < 2):
        return "Invalido"

    # Verificar si alguien ganó el set
    if juegos_a >= 6 and juegos_a - juegos_b >= 2:
        return "Gano A"
    elif juegos_b >= 6 and juegos_b - juegos_a >= 2:
        return "Gano B"
    # Verificar si el set aún no ha terminado
    else:
        return "Aun no termina"

# Ciclo para recibir entradas del usuario
while True:
    try:
        juegos_a = int(input("Juegos ganados por A: "))
        juegos_b = int(input("Juegos ganados por B: "))

        # Verificar el estado del set y mostrar el resultado
        resultado = verificar_set(juegos_a, juegos_b)
        print(resultado)

        # Preguntar si se desea continuar
        continuar = input("¿Desea ingresar otro resultado? (si/no): ")
        if continuar.lower() != 'si':
            break
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número entero.")
