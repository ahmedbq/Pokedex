from flask_restful import Resource
from pathlib import Path
from models.pokemon import PokemonModel

import pandas as pd

folder_path = Path("data/")
file_path = folder_path / "pokemon.csv"

class Pokemon(Resource):
    def get(self):
        data = pd.read_csv(file_path)

        pokemons = []

        # There can be duplicates of Pokemon - difference of types
        # Data will be condensed to have a list of types per Pokemon
        for row in data.itertuples():
            pokemon = PokemonModel(row.Number, row.Name, row.Type,
                                   row.Total, row.HP, row.Attack,
                                   row.Defense, row.Special_Attack,
                                   row.Special_Defense, row.Speed)

            pokemonCopy = [x for x in pokemons if x.number == row.Number]

            # If it exists, then just add the type
            if len(pokemonCopy) > 0:
                pokemonCopy[0].addType(row.Type)
            # Otherwise add it to the list
            else:
                pokemons.append(pokemon)

        return {"pokemons": [x.json() for x in pokemons]}
