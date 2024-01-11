from classes.Pokemon import Pokemon
from classes.Attaque import Attaque
from classes.Combat import Combat
import random

def choisir_pokemon(liste_pokemons):
    print("Choisissez votre Pokémon:")
    for index, pokemon in enumerate(liste_pokemons, start=1):
        print(f"{index}. {pokemon.nom} (Type: {pokemon.type.nom}, Niveau: {pokemon.lvl})")
    choix = int(input("Entrez le numéro de votre Pokémon: "))
    if 1 <= choix <= len(liste_pokemons):
        return liste_pokemons[choix - 1]
    else:
        print("Choix non valide, veuillez réessayer.")
        return choisir_pokemon(liste_pokemons)

def main():
    Pokemon.import_json("json/pokemon.json")
    mon_pokemon = None

    while True:
        if mon_pokemon is None or mon_pokemon.pv <= 0:
            mon_pokemon = choisir_pokemon(Pokemon.tous_pokemons)
            mon_pokemon.attaque_de_base = Attaque.assigner_attaque_base(mon_pokemon)

        print(f"Votre Pokémon choisi est : {mon_pokemon.nom} (PV: {mon_pokemon.pv})")
        mon_pokemon.soigner()

        adversaire = random.choice(Pokemon.tous_pokemons)
        adversaire.attaque_de_base = Attaque.assigner_attaque_base(adversaire)
        adversaire.soigner()
        print(f"Vous rencontrez : {adversaire.nom} (PV: {adversaire.pv})")

        gagnant, a_fui = Combat.lancer_combat(mon_pokemon, adversaire)

        if a_fui:
            continuer = input("Voulez-vous continuer de combattre avec le même Pokémon ? (oui/non) : ").lower()
            if continuer == 'oui':
                continue
            else:
                nouveau_pokemon = input("Voulez-vous choisir un nouveau Pokémon ? (oui/non) : ").lower()
                if nouveau_pokemon == 'oui':
                    mon_pokemon = None
                    continue
                else:
                    print("Merci d'avoir joué ! À bientôt.")
                    break

        if mon_pokemon.nom == gagnant:
            rejouer = input("Voulez-vous combattre un nouvel adversaire avec le même Pokémon ? (oui/non) : ").lower()
            if rejouer != 'oui':
                changer_pokemon = input("Voulez-vous choisir un nouveau Pokémon ? (oui/non) : ").lower()
                if changer_pokemon == 'oui':
                    mon_pokemon = None
                else:
                    print("Merci d'avoir joué ! À bientôt.")
                    break
        else:
            print(f"{mon_pokemon.nom} est K.O. !")
            mon_pokemon = None  # Reset pour forcer le choix d'un nouveau Pokémon

if __name__ == "__main__":
    main()