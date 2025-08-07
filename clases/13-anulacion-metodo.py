class Ave:
    def __init__(self):
        self.volador = True

    def vuela(self):
        print("vuela")


class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nada = True

    def vuela(self):
        super().vuela()
        print("vuela pato")


pato = Pato()
pato.vuela()
