from classes.Pokemon import Pokemon
from classes.Attaque import Attaque
from classes.Combat import Combat
import random

def assigner_attaque_base(pokemon):
    # Configuration de l'attaque de base du Pokémon en fonction de son type et du niveau du Pokémon
    if pokemon.type.nom.lower() == 'feu':
        return Attaque.attaque_feu(pokemon.lvl)
    elif pokemon.type.nom.lower() == 'eau':
        return Attaque.attaque_eau(pokemon.lvl)
    elif pokemon.type.nom.lower() == 'electrik':
        return Attaque.attaque_electrik(pokemon.lvl)
    elif pokemon.type.nom.lower() == 'plante':
        return Attaque.attaque_plante(pokemon.lvl)
    elif pokemon.type.nom.lower() == 'normal':
        return Attaque.attaque_normal(pokemon.lvl)
    # Ajoutez des cas pour d'autres types d'attaques si nécessaire
    # Retourne None ou une attaque par défaut si le type n'est pas géré
    return None

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

def main():
    # Charger tous les Pokémon à partir du fichier JSON
    Pokemon.import_json("json/pokemon.json")
    mon_pokemon = None  # Initialisation de la variable pour stocker le Pokémon choisi

    while True:  # Boucle principale du jeu
        if not Pokemon.tous_pokemons:
            print("Aucun Pokémon n'a été chargé du fichier JSON.")
            break

        # Si le joueur n'a pas encore de Pokémon ou choisit de changer, il en sélectionne un nouveau
        if mon_pokemon is None:
            mon_pokemon = choisir_pokemon(Pokemon.tous_pokemons)
            mon_pokemon.attaque_de_base = assigner_attaque_base(mon_pokemon)

        # Soin du Pokémon avant le combat
        mon_pokemon.soigner()
        print(f"Votre Pokémon choisi est : {mon_pokemon.nom} (PV: {mon_pokemon.pv})")

        # Sélection aléatoire d'un adversaire différent du Pokémon choisi
        adversaire = random.choice([p for p in Pokemon.tous_pokemons if p != mon_pokemon])
        adversaire.attaque_de_base = assigner_attaque_base(adversaire)
        adversaire.soigner()
        print(f"Vous rencontrez : {adversaire.nom} (PV: {adversaire.pv})")

        # Lancement du combat
        Combat.lancer_combat(mon_pokemon, adversaire)

        # Vérifier si le Pokémon du joueur a survécu au combat
        if mon_pokemon.pv <= 0:
            print(f"{mon_pokemon.nom} est K.O. !")
            mon_pokemon = None  # Le joueur doit choisir un nouveau Pokémon
            continue  # Retourner au début de la boucle

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

if __name__ == "__main__":
    main()