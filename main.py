import os 
import requests
import json
from pydantic import BaseModel

url="https://tyradex.tech/api/v1"
reqPokemon="/pokemon/"

class Pokemon(BaseModel):
    name: str
    types: str
    generation: int

    def __str__(self):
        return f'{self.name.fr} le Pokémon {self.generation}G de type {self.types[0].name} !'

r = requests.get(url + reqPokemon + "larmeleon")
pok = Pokemon(**r.json())
print(pok)