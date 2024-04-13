import requests
import json
from pydantic import BaseModel
from typing import List, Optional
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
    types: Optional[List[PokemonType]]
    generation: int

    def __str__(self):
        showType = ' et '.join(map(lambda x : x.name, self.types or []))
        return f'{self.name.fr} le Pokémon {self.generation}G de type {showType} !'

with open('./migrations/pokemons.json') as f:
    d = json.load(f)
    pokemons: List[Pokemon] = [Pokemon(**p) for p in d]
    print(pokemons[0])