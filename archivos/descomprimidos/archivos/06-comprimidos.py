from pathlib import Path
from zipfile import ZipFile


with ZipFile("archivos/comprimidos.zip", "w") as zip:
    # curso-py
    for path in Path().rglob("*.*"):
        print(path)
        if str(path) != "archivos/comprimidos.zip":
            zip.write(path)
