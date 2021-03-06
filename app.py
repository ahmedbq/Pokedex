from flask import Flask
from flask_restful import Api

from resources.pokemon import Pokemon, PokemonList
from resources.table import Table

app = Flask(__name__)
api = Api(app)

api.add_resource(Pokemon, '/pokemon/<string:number>')
api.add_resource(PokemonList, '/pokemon')
api.add_resource(Table, '/table')

if __name__ == '__main__':
    app.run(debug=True)
