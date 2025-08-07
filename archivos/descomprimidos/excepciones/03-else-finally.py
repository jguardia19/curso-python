try:
    n1 = int(input("Ingresa primer numero: "))
except Exception as e:
    print("Ocurrio un error")
else:
    print("No ocurrio ningun error")  # se ejecuta si no ocurre error
finally:  # se ejecuta siempre
    print("se ejecuta siempre")
