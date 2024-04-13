import json
from pydantic import BaseModel
from typing import List
import sqlite3

class LocalizedName(BaseModel):
    fr: str
    en: str
    jp: str

class PokemonType(BaseModel):
    name: str
    image: str

class Pokemon(BaseModel):
    pokedex_id : int
    name: LocalizedName
    types: List[PokemonType]
    generation: int




con = sqlite3.connect("pokedex.db")
try:
    con.executescript("""
    CREATE TABLE pokemon(
        dex_id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(50),
        json_sprites JSON,
        url_cri VARCHAR(255)
    );
    CREATE TABLE type(
        id INTEGER PRIMARY KEY NOT NULL,
        json_data JSON
    );
    CREATE TABLE pokemon_type(
        pokemon_dex_id INTEGER NOT NULL,
        type_id INTEGER NOT NULL,
        PRIMARY KEY(pokemon_dex_id, type_id),
        FOREIGN KEY(pokemon_dex_id) REFERENCES pokemon(dex_id)
        FOREIGN KEY(type_id) REFERENCES type(id)
    );
""")

    with open('./pokemons.json') as f:
        d = json.load(f)
        pokemons: List[Pokemon] = [Pokemon(**p) for p in d]
        print(pokemons[0])
        
    
    con.commit()
    print("Coommited !")
except sqlite3.Error as e:
    print(e)
    con.rollback()


