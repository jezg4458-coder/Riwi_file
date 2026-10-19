print("Welcome")
lado1 = float(input("Ingresa el lado 1 del triángulo:"))
lado2 = float(input("Ingresa el lado 2 del triángulo:"))
lado3 = float(input("Ingresa el lado 3 del triángulo:"))
if lado1 == lado2 and lado3 == lado1:
    print("Es un triángulo equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("Es un triángulo isóseles")
else:
    print("El Triángulo es escaleno")