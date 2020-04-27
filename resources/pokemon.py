from flask_restful import Resource
from pathlib import Path
from models.pokemon import PokemonModel

import pandas as pd

folder_path = Path("data/")
file_path = folder_path / "pokemon.csv"


class Pokemon(Resource):

    def get(self, number):

        # Skip rows to increase performance
        # There are numbers such as 9.1 or 229.1 which are rounded down
        data = pd.read_csv(file_path, skiprows=range(1, int(float(number))))

        pokemon = None

        for row in data.itertuples():
            # Remember that there can be duplicate pokemon with different/same types
            # If it does not exist yet
            if float(row.Number) == float(number) and pokemon is None:
                pokemon = PokemonModel(row.Number, row.Name, row.Type,
                                       row.Total, row.HP, row.Attack,
                                       row.Defense, row.Special_Attack,
                                       row.Special_Defense, row.Speed)
            # If it exists but the type does not
            elif float(row.Number) == float(number) and row.Type not in pokemon.types:

                pokemon.types.append(row.Type)

        if pokemon is not None:
            return {"pokemon": pokemon.json()}

        return {"message": f"Could not find pokemon with number: {number}"}


class PokemonList(Resource):

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
                # There can be duplicates of the same pokemon
                # with the same type
                if row.Type not in pokemonCopy[0].types:
                    pokemonCopy[0].addType(row.Type)
            # Otherwise add it to the list
            else:
                pokemons.append(pokemon)

        return {"pokemons": [x.json() for x in pokemons]}
