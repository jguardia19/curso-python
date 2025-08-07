import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Jose Guardia"),
        (3, "Carolina Machado"),
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?)",
        usuarios,
    )
