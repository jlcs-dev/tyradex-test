import sqlite3


con = sqlite3.connect("pokedex.db")
try:
    con.executescript("""CREATE TABLE pokemon(dex_id, name, )""")
    con.commit()
except sqlite3.Error:
    con.rollback()


