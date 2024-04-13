import json
from pydantic import BaseModel
from typing import List, Optional
import sqlite3


class LocalizedName(BaseModel):
    fr: str
    en: str
    jp: str


class PokemonType(BaseModel):
    name: str
    image: str


class Sprites(BaseModel):
    regular: Optional[str] = None
    shiny: Optional[str] = None


class Pokemon(BaseModel):
    pokedex_id : int
    name: LocalizedName
    sprites: Sprites
    types: List[PokemonType]
    generation: int




con = sqlite3.connect("pokedex.db")
try:
    con.executescript("""
    CREATE TABLE pokemon(
        dex_id INTEGER PRIMARY KEY NOT NULL,
        name JSON,
        generation INTEGER,
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

    with open('./migrations/pokemons.json') as f:
        d = json.load(f)
        pokemons: List[Pokemon] = [Pokemon(**p) for p in d]
        con.executemany("INSERT INTO pokemon(dex_id,name,generation,json_sprites) VALUES(?,?,?,?)", map(lambda x:(x.pokedex_id, json.dumps(x.name,default=lambda y: y.__dict__), x.generation, json.dumps(x.sprites,default=lambda y: y.__dict__)),pokemons))
           
    con.commit()
    print("Coommited !")
except sqlite3.Error as e:
    print(e)
    con.rollback()


