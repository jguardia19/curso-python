mascostas = [
    "Wolfgang",
    "Pelusa",
    "Pulga",
    "Felipe",
    "Pulga",
    "Chanchito Feliz"
]

mascostas.insert(1, "Melvin")
mascostas.append("Chanchito Triste")

mascostas.remove("Pulga")
mascostas.pop()  # remover ultimo elemento
mascostas.pop(1)  # remover uno en especifico
del mascostas[0]
mascostas.clear()
print(mascostas)
