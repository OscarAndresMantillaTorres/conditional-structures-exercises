def calcular_bmi(peso, altura):
    """Calcula el índice de masa corporal (IMC)."""
    return peso / (altura ** 2)

def determinar_riesgo(bmi, edad):
    """Determina la condición de riesgo basado en el IMC y la edad."""
    if edad < 45:
        if bmi < 22.0:
            return "bajo"
        else:
            return "medio"
    else:  # edad >= 45
        if bmi < 22.0:
            return "medio"
        else:
            return "alto"

# Ciclo para recibir entradas del usuario
while True:
    try:
        altura = float(input("Ingrese su altura en metros: "))
        peso = float(input("Ingrese su peso en kilogramos: "))
        edad = int(input("Ingrese su edad: "))

        # Calcular IMC
        bmi = calcular_bmi(peso, altura)

        # Determinar riesgo
        riesgo = determinar_riesgo(bmi, edad)

        # Mostrar el resultado
        print(f"Su índice de masa corporal (IMC) es: {bmi:.2f}")
        print(f"Su condición de riesgo es: {riesgo}")

        # Preguntar si se desea continuar
        continuar = input("¿Desea ingresar otra persona? (si/no): ")
        if continuar.lower() != 'si':
            break
    except ValueError:
        print("Entrada no válida. Por favor ingrese valores numéricos.")
