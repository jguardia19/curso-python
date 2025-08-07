def get_product(**datos):
    print(datos["id"], datos["name"])


get_product(id="23", name="iphone", stock=5, desc="Esto es un iphone")
