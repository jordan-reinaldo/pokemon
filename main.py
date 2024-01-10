from classes.Pokemon import Pokemon
from classes.Attaque import Attaque
from classes.Combat import Combat
import random

def main():
    # Charger tous les Pokémon à partir du fichier JSON
    Pokemon.import_json("json/pokemon.json")
    
    # Exemple d'accès au premier Pokémon chargé
    if Pokemon.tous_pokemons:
        mon_pokemon = random.choice(Pokemon.tous_pokemons)
        print(f"mon pokemon est : {mon_pokemon.nom}")

        # Exemple de configuration de l'attaque de base du premier Pokémon
        if mon_pokemon.type.nom.lower() == 'feu':
            mon_pokemon.attaque_de_base = Attaque.flammeche()
        elif mon_pokemon.type.nom.lower() == 'eau':
            mon_pokemon.attaque_de_base = Attaque.pistolet_a_o()
        elif mon_pokemon.type.nom.lower() == 'electrik':
            mon_pokemon.attaque_de_base = Attaque.tonnerre()
        elif mon_pokemon.type.nom.lower() == 'plante':
            mon_pokemon.attaque_de_base = Attaque.tranche_herbe()
        else:
            mon_pokemon.attaque_de_base = Attaque.charge()


        adversaire = random.choice(Pokemon.tous_pokemons)
        print(f"Vous rencontrez : {adversaire}")
        degats = mon_pokemon.utiliser_attaque(adversaire)
        print(f"Dégâts infligés par {mon_pokemon.nom} à {adversaire.nom} = {int(degats)}")
    else:
        print("Aucun Pokémon n'a été chargé du fichier JSON.")

if __name__ == "__main__":
    main()