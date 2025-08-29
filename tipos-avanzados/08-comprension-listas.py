usuarios = [
    ["Cahanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombres = []
# for name in usuarios:
#     nombres.append(name[0])

# print(nombres)

# nombres = [expresion for item in items]
# map
# nombres = [usuario[1] for usuario in usuarios]
# print(nombres)

# filtrar = filter
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)

# filtrar y transformar -
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]


# nombres = list(map(lambda usuario: usuario[0], usuarios))

# menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
# print(menosUsuarios)
