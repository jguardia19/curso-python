from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")
# archivo.exists()
# archivo.rename()
# archivo.unlink()

# print(archivo.stat())

print("acceso", ctime(archivo.stat().st_atime))
