
from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "base de datos",
    "api": "esta es la api",
    "graphql": "esto es grahpql"
}


def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("el paquete no tiene funcion init")


list(map(load, paths))
