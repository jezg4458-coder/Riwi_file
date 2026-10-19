print("Welcome")
valorCompra = float(input("¿Cuál fué el valor de la compra? Escríbelo, por favor:"))
if valorCompra >=200000:
    valorCompra = (valorCompra*-0.20)+valorCompra
    print(valorCompra)
elif valorCompra >100000 and valorCompra <200000:
    print("El Valor de la compra con el descuento aplicado es de:")
    print((valorCompra *10)-valorCompra) 
else:
    print("No tienen descuento")