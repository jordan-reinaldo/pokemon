import json
from .Type import Type
from .Combat import Combat

class Pokemon:
    tous_pokemons = []  # Attribut de classe pour stocker tous les Pokémon chargés

    def __init__(self, nom, type_pokemon, pv, attaque, defense, lvl, xp, xp_necessaire, attaque_de_base=None):
        self.nom = nom
        self.type = type_pokemon
        self.pv = pv
        self.pv_max = pv
        self.attaque = attaque
        self.defense = defense
        self.lvl = lvl
        self.xp = xp
        self.xp_necessaire = xp_necessaire
        self.attaque_de_base = attaque_de_base
    
        Pokemon.tous_pokemons.append(self)  # Ajout du Pokémon nouvellement créé à la liste de tous les Pokémon

    @staticmethod
    def import_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        for donnee_pokemon in data:
            type_pokemon = getattr(Type, donnee_pokemon['type'].lower())()
            pokemon = Pokemon(
                nom=donnee_pokemon['nom'],
                type_pokemon=type_pokemon,
                pv=donnee_pokemon['pv'],
                attaque=donnee_pokemon['attaque'],
                defense=donnee_pokemon['defense'],
                lvl=donnee_pokemon['lvl'],
                xp=donnee_pokemon['xp'],
                xp_necessaire=donnee_pokemon['xp_necessaire']  
                )
        # L'ajout à tous_pokemons se fait dans le __init__

        return Pokemon.tous_pokemons  # Retour de la liste complète des Pokémon chargés

    def soigner(self):
        self.pv = self.pv_max  # Méthode pour soigner le Pokémon à ses PV max

    def __str__(self):
        return f"{self.nom} ({self.type.nom}) - PV: {self.pv} Attaque: {self.attaque} Défense: {self.defense} Niveau: {self.lvl} XP: {self.xp}"
    
    def gagner_xp(self, quantite):
        self.xp += quantite
        while self.xp >= self.xp_necessaire:
            self.monter_de_niveau()
    
    def monter_de_niveau(self):
        self.xp -= self.xp_necessaire
        self.lvl += 1
        self.xp_necessaire *= 1.2  # Augmenter le seuil pour le prochain niveau
        self.pv_max += 10  # Augmenter les PV max
        self.pv = self.pv_max  # Soigner le Pokémon à ses nouveaux PV max
        self.attaque += 5  # Augmenter l'attaque
        self.defense += 5  # Augmenter la défense
        print(f"{self.nom} est monté au niveau {self.lvl}!")