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

def main():
    # Charger tous les Pokémon à partir du fichier JSON
    Pokemon.import_json("json/pokemon.json")

    while True:  # Boucle principale du jeu
        if Pokemon.tous_pokemons:
            mon_pokemon = choisir_pokemon(Pokemon.tous_pokemons)
            mon_pokemon.attaque_de_base = assigner_attaque_base(mon_pokemon)
            print(f"Votre Pokémon choisi est : {mon_pokemon.nom} (PV: {mon_pokemon.pv})")

            # Sélection aléatoire d'un adversaire différent du Pokémon choisi
            adversaire = random.choice([p for p in Pokemon.tous_pokemons if p != mon_pokemon])
            adversaire.attaque_de_base = assigner_attaque_base(adversaire)
            print(f"Vous rencontrez : {adversaire.nom} (PV: {adversaire.pv})")

            # Lancement du combat
            Combat.lancer_combat(mon_pokemon, adversaire)

            # Demander au joueur s'il veut relancer un combat
            rejouer = input("Voulez-vous relancer un combat ? (oui/non) : ").lower()
            if rejouer != 'oui':
                print("Merci d'avoir joué ! À bientôt.")
                break
        else:
            print("Aucun Pokémon n'a été chargé du fichier JSON.")
            break

if __name__ == "__main__":
    main()