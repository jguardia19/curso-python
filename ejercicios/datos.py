numero1 = int(input("Ingresa primer numero: "))
numero2 = int(input("Ingresa segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multi = numero1 * numero2
div = numero1 / numero2

mensaje = f"""
Para los numeros {numero1} y {numero2},
el resultado de la suma es {suma},
el resultado de la resta es {resta},
el resultado de la multiplicacion es {multi},
el resultado de la division es {div}.
Fin.
"""

print(mensaje)
