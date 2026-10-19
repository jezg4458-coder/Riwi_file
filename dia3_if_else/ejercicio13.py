print("welcome to calculator")
print("1 sumar")
print("2 restar")
print("3 multiplicar")
print("4 dividir")
operacion = str(input("introduce la operacion: "))
num1 = float(input("introduce el primer numero: "))
num2 = float(input("introduce el segundo numero: "))

if operacion == "1":
    print("Resultado:", num1 + num2)
elif operacion == "2":
    print("Resultado:", num1 - num2)
elif operacion == "3":
    print("Resultado:", num1 * num2)
elif operacion == "4":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: division por cero")

    