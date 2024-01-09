import json
from .Type import Type
from .Combat import Combat

class Pokemon:
    def __init__(self, nom, type_pokemon, pv, attaque, defense, lvl, xp, attaque_de_base=None):
        self.nom = nom
        self.type = type_pokemon
        self.pv = pv
        self.attaque = attaque
        self.defense = defense
        self.lvl = lvl
        self.xp = xp
        self.attaque_de_base = attaque_de_base

    def utiliser_attaque(self, cible):
        return Combat.calculer_degats(self, self.attaque_de_base, cible)

    @staticmethod
    def import_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        pokemons = []
        for donnee_pokemon in data:
            type_pokemon = getattr(Type, donnee_pokemon['type'].lower())()
            pokemon = Pokemon(
                donnee_pokemon['nom'],
                type_pokemon,
                donnee_pokemon['pv'],
                donnee_pokemon['attaque'],
                donnee_pokemon['defense'],
                donnee_pokemon['lvl'],
                donnee_pokemon['xp']
            )
            pokemons.append(pokemon)

        return pokemons