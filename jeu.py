from classes.Pokemon import Pokemon
from classes.Attaque import Attaque
from classes.Combat import Combat
import random

def choisir_pokemon(liste_pokemons):
    print("Choisissez votre Pokémon:")
    for index, pokemon in enumerate(liste_pokemons, start=1):
        print(f"{index}. {pokemon.nom} (Type: {pokemon.type.nom}, Niveau: {pokemon.lvl})")
    choix = int(input("Entrez le numéro de votre Pokémon: "))
    # Assurez-vous que le choix est valide
    if 1 <= choix <= len(liste_pokemons):
        return liste_pokemons[choix - 1]
    else:
        print("Choix non valide, veuillez réessayer.")
        return choisir_pokemon(liste_pokemons)  # Récursivité pour forcer un choix valide

# Importez vos modules/classes nécessaires ici

def jeu():
    # Charger tous les Pokémon à partir du fichier JSON
    Pokemon.import_json("json/pokemon.json")
    mon_pokemon = None  # Initialisation de la variable pour stocker le Pokémon choisi

    while True:
        if mon_pokemon is None or mon_pokemon.pv <= 0:
            if mon_pokemon and mon_pokemon.pv <= 0:
                choix = input("Votre Pokémon est K.O. Voulez-vous le soigner et continuer avec lui ? (oui/non) : ").lower()
                if choix == 'oui':
                    mon_pokemon.soigner()
                else:
                    mon_pokemon = choisir_pokemon(Pokemon.tous_pokemons)
                    mon_pokemon.attaque_de_base = Attaque.assigner_attaque_base(mon_pokemon)
            else:
                mon_pokemon = choisir_pokemon(Pokemon.tous_pokemons)
                mon_pokemon.attaque_de_base = Attaque.assigner_attaque_base(mon_pokemon)
            
            print(f"Votre Pokémon choisi est : {mon_pokemon.nom} (PV: {mon_pokemon.pv})")
        
        # Soin du Pokémon avant le combat
        mon_pokemon.soigner()

        # Sélection aléatoire d'un adversaire différent du Pokémon choisi
        adversaire = random.choice(Pokemon.tous_pokemons)
        adversaire.attaque_de_base = Attaque.assigner_attaque_base(adversaire)
        adversaire.soigner()
        print(f"Vous rencontrez : {adversaire.nom} (PV: {adversaire.pv})")

        # Lancement du combat
        gagnant = Combat.lancer_combat(mon_pokemon, adversaire)

        # Vérifier si le Pokémon du joueur a survécu au combat
        if mon_pokemon.nom == gagnant:
            # Demander au joueur s'il veut relancer un combat avec le même Pokémon
            rejouer = input("Voulez-vous combattre un nouvel adversaire avec le même Pokémon ? (oui/non) : ").lower()
            if rejouer != 'oui':
                # Demander si le joueur veut choisir un nouveau Pokémon
                changer_pokemon = input("Voulez-vous choisir un nouveau Pokémon ? (oui/non) : ").lower()
                if changer_pokemon == 'oui':
                    mon_pokemon = None  # Le joueur peut choisir un nouveau Pokémon
                else:
                    print("Merci d'avoir joué ! À bientôt.")
                    break
        else:
            print(f"{mon_pokemon.nom} est K.O. !")

if __name__ == "__main__":
    jeu()
