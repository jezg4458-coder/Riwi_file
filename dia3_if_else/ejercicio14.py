print("Bienvenido al cajero Python")
print("1 Consultar saldo")
print("2 Retirar dinero")
print("3 Depositar dinero")
print("4 Salir")

opcion = str(input("Seleccione una opción: "))

if opcion == "1":
    print("Su saldo es: $500000")
elif opcion == "2":
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= 500000:
        print("Retiro exitoso. Su nuevo saldo es:", 500000 - monto)
    else:
        print("Fondos insuficientes")
elif opcion == "3":
    monto = float(input("Ingrese el monto a depositar: "))
    print("Depósito exitoso. Su nuevo saldo es:", 500000 + monto)
elif opcion == "4":
    print("Gracias por usar el cajero Python")
else:
    print("Opción no válida")