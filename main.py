# Función para realizar operaciones
def calcular(operando1, operador, operando2):
    if operador == '+':
        return operando1 + operando2
    elif operador == '-':
        return operando1 - operando2
    elif operador == '*':
        return operando1 * operando2
    elif operador == '/':
        if operando2 != 0:
            return operando1 / operando2
        else:
            return "Error: División por cero."
    elif operador == '**':
        return operando1 ** operando2
    else:
        return "Operador no válido."

# Pedir al usuario los operandos y el operador
while True:
    try:
        operando1 = float(input("Enter the first operand: "))
        operador = input("Enter the operator (+, -, *, /, **): ")
        operando2 = float(input("Enter the second operand: "))

        # Calcular el resultado
        resultado = calcular(operando1, operador, operando2)

        # Mostrar el resultado
        print(f"{operando1} {operador} {operando2} = {resultado}")
        
        # Preguntar si quiere continuar
        continuar = input("Do you want to perform another calculation? (yes/no): ")
        if continuar.lower() != 'yes':
            break
    except ValueError:
        print("Invalid input. Please enter numeric values.")
