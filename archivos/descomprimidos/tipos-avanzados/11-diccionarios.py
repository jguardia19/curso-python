punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45

print(punto)

if "lala" in punto:
    print("encontre a lala")

print(punto.get("lala", 97))
# del punto["x"]
# del (punto["y"])

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, vlor in punto.items():
    print(llave, valor)


usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 1, "nombre": "Felipe"},
]

for usuario in usuarios:
    print(usuario["nombre"])
