print("Bienvenido al sistema de facturación")
nombreCliente = input("Ingrese el nombre del cliente: ")
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))

subtotal = precio * cantidad

if subtotal >= 500000:
    descuento = subtotal * 0.15
elif subtotal >= 200000:
    descuento = subtotal * 0.10
else:
    descuento = 0

total = subtotal - descuento

print("\nFactura")
print("Cliente:", nombreCliente)
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Total a pagar:", total)                                  
