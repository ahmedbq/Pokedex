from pathlib import Path
from flask_restful import Resource

import pandas as pd


class Table(Resource):

    def get(self):
        folder_path = Path("data/")
        file_path = folder_path / "pokemon.csv"
        data = pd.read_csv(file_path)

        columns = [x for x in data.columns]
        numOfPokemon = len(data.Name.unique())

        return {"columns": columns, "numOfPokemon": numOfPokemon}
