import requests
import json
from pydantic import BaseModel
from typing import List
import sqlite3

url="https://tyradex.tech/api/v1"
reqPokemon="/pokemon/"

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

    def __str__(self):
        return f'{self.name.fr} le Pokémon {self.generation}G de type {', '.join(map(lambda x : x.name, self.types))} !'

r = requests.get(url + reqPokemon + "grimalin")
pok = Pokemon(**r.json())
print(pok)