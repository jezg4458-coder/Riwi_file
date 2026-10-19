print("Welcome")
temperatura = float(input("Di la temperatura a consultar:"))
if temperatura <10:
    print("Clima frío")
if temperatura >= 10 and temperatura <25:
    print("El cliema es templado")
if temperatura >=25 and temperatura <35:
    print("El clima es caluroso")
if temperatura >=35:
    print("El clima es extremo u caluroso")