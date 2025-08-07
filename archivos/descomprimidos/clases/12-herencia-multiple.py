class Animal:
    def comer(self):
        print("comiendo")


class Perro:
    def pasear(self):
        print("paseando")


class Chanchito(Perro, Animal):
    def programar(self):
        print("programando")


chanchito = Chanchito()
