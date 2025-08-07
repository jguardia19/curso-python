numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort()
# numeros.sort(reverse=True)

numeros2 = sorted(numeros)
print(numeros)
print(numeros2)

usuarios = [
    ["Cahanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]


# def ordena(elemento):
#     return elemento[1]


# usuarios.sort(key=ordena, reverse=True)

usuarios.sort(key=lambda el: el[1])

print(usuarios)
