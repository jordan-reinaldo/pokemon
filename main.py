from classes.Pokemon import Pokemon
from classes.Attaque import Attaque
from classes.Combat import Combat
import random

def main():
    # Charger tous les Pokémon à partir du fichier JSON
    Pokemon.import_json("json/pokemon.json")
    
    if Pokemon.tous_pokemons:
        # Sélection aléatoire d'un Pokémon
        mon_pokemon = random.choice(Pokemon.tous_pokemons)
        print(f"Mon Pokémon est : {mon_pokemon.nom}")

        # Configuration de l'attaque de base du Pokémon en fonction de son type et du niveau du pokemon
        if mon_pokemon.type.nom.lower() == 'feu':
            mon_pokemon.attaque_de_base = Attaque.attaque_feu(mon_pokemon.lvl)
        elif mon_pokemon.type.nom.lower() == 'eau':
            mon_pokemon.attaque_de_base = Attaque.attaque_eau(mon_pokemon.lvl)
        elif mon_pokemon.type.nom.lower() == 'electrik':
            mon_pokemon.attaque_de_base = Attaque.attaque_electrik(mon_pokemon.lvl)
        elif mon_pokemon.type.nom.lower() == 'plante':
            mon_pokemon.attaque_de_base = Attaque.attaque_plante(mon_pokemon.lvl)
        elif mon_pokemon.type.nom.lower() == 'normal':
            mon_pokemon.attaque_de_base = Attaque.attaque_normal(mon_pokemon.lvl)

        # Sélection aléatoire d'un adversaire
        adversaire = random.choice(Pokemon.tous_pokemons)
        print(f"Vous rencontrez : {adversaire.nom}")

        # Le Pokémon utilise son attaque
        nom_attaque, degats = mon_pokemon.utiliser_attaque(adversaire)
        pv_restants = Combat.appliquer_degats(adversaire, degats)
        print(f"{mon_pokemon.nom} utilise {nom_attaque} contre {adversaire.nom} !")
        print(f"Dégâts infligés : {degats}")
        print(f"PV restants de {adversaire.nom} : {pv_restants}")
    else:
        print("Aucun Pokémon n'a été chargé du fichier JSON.")

if __name__ == "__main__":
    main()