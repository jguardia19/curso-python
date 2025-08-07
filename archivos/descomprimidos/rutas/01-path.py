from pathlib import Path

# Path(r"C:\Archivos de Programa\Minecreaft")
# Path("/usr/bin")
# Path()
# Path.home()
# Path("one/__init__.py")

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("chanchito.py")

p = path.with_suffix(".php")

p = path.with_stem("feliz")

print(p)
