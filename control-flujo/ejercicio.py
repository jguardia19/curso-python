print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, multi, div y resta")

resultado = ""
while True:  # loop infinito
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)

    op = input("Ingrese tipo de operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese Segundo número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op == "suma":
        resultado += n2
    elif op == "resta":
        resultado -= n2
    elif op == "multi":
        resultado *= n2
    elif op == "div":
        resultado /= n2
    else:
        print("La operacion es incorrecta")
        break

    print(f"El resultado es: {resultado}")
