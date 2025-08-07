class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Chao perro {self.nombre} 😔😔")

    def __str__(self):
        return f"Case perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau")


perro = Perro("Chachito", 7)
del perro
