persona = {
    "nombre": "Jose Guardia",
    "edad": 30,
    "ciudad": "Bogota"
}

persona["telefono"] = "3124567890"

for llave, valor in persona.items():
    print(f"{llave}: {valor}")
