import json
from .Type import Type
from .Attaque import Attaque
from .Combat import Combat

class Pokemon:
    tous_pokemons = []  # Attribut de classe pour stocker tous les Pokémon chargés

    def __init__(self, nom, type_pokemon, pv, attaque, defense, lvl, xp, attaque_de_base=None):
        self.nom = nom
        self.type = type_pokemon
        self.pv = pv
        self.attaque = attaque
        self.defense = defense
        self.lvl = lvl
        self.xp = xp
        self.attaque_de_base = attaque_de_base
    
        Pokemon.tous_pokemons.append(self) # Ajout du Pokémon nouvellement créé à la liste de tous les Pokémon

    def utiliser_attaque(self, cible):
        nom_attaque = self.attaque_de_base.nom
        degats = Combat.calculer_degats(self, self.attaque_de_base, cible)
        return nom_attaque, degats

    @staticmethod
    def import_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)

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
            # L'ajout à tous_pokemons se fait maintenant dans le __init__

        return Pokemon.tous_pokemons  # Retourner la liste complète des Pokémon chargés

    def __str__(self):
        return f"{self.nom} ({self.type.nom}) - PV: {self.pv} Attaque: {self.attaque} Défense: {self.defense} Niveau: {self.lvl} XP: {self.xp}"