if __name__ != "__main__":
    from ..gestion.crud import guardar  # import relativo
    # from usuarios.gestion.crud import guardar (import absoluto)

    print(__name__)

    def pagar_impuestos():
        print("pagando impúestos")
        guardar()

if __name__ == "__main__":
    print("Tarea de Mantenieminto")
