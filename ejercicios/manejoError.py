try:
    numer1 = float(input("Ingresa un numero: "))
    numer2 = float(input("Ingresa otro numero: "))

    resultado = numer1 / numer2
    print(f"El resultado es: {resultado}")
except ZeroDivisionError as e:
    print("No se puede dividir por 0")
except ValueError as e:
    print("Ingrese un valor que corresponda")
