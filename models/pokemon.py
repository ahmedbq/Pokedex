class PokemonModel:

    def __init__(self, number, name, type, total, hp,
                 attack, defense, special_attack, special_defense, speed):

        self.types = []
        self.types.append(type)

        self.number = number
        self.name = name
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    def addType(self, type):
        self.types.append(type)

    def json(self):
        return {"number": float(self.number),
                "name": self.name,
                "types": self.types,
                "total": self.total,
                "hp": self.hp,
                "attack": self.attack,
                "defense": self.defense,
                "special_attack": self.special_attack,
                "special_defense": self.special_defense,
                "speed": self.speed}
