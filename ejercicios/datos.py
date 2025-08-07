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

#print(mensaje)

cuadros = list(map(lambda x: x**2 ,range(1,50)))
print(cuadros)

try:
    if numero1 > numero2:
        print("El numero 1 es mayor")
    else:
        print("El numero 2 es mayor")   
except Exception as e:
    print("Ingrese un valor que corresponda")
