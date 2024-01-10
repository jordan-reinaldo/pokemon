import time
class Combat:
    @staticmethod
    def calculer_degats(attaquant, attaque, defenseur):
        # Calcul du coefficient d'efficacité en fonction des types
        coefficient_eff = 1.0 
        if attaque.type.nom in defenseur.type.faiblesses:
            coefficient_eff = 2
        elif attaque.type.nom in defenseur.type.forces:
            coefficient_eff = 0.5
        elif attaque.type.nom in defenseur.type.nulle_defense:
            coefficient_eff = 0.0

        # Formule de base pour le calcul des dégâts
        degats = int((((attaquant.lvl * 0.4 + 2) * attaquant.attaque * attaque.puissance / (defenseur.defense * 50)) + 2)) * coefficient_eff
        return degats

    @staticmethod
    def appliquer_degats(defenseur, degats):
        defenseur.pv -= degats
        if defenseur.pv < 0:
            defenseur.pv = 0
        return defenseur.pv

    @staticmethod
    def lancer_combat(pokemon1, pokemon2):
        print(f"Le combat commence entre {pokemon1.nom} et {pokemon2.nom} !")

        while True:  # Boucle infinie qui ne sera interrompue que par une fuite ou un K.O.
            time.sleep(1)
            # Demander au joueur de choisir une action pour le Pokémon 1
            action = input(f"{pokemon1.nom}, que voulez-vous faire ? 'attaquer' ou 'fuir' : ").lower()
            if action == 'fuir':
                print(f"{pokemon1.nom} a fui le combat.")
                print(f"Le {pokemon2.nom} adverse est déclaré vainqueur par forfait !")
                return pokemon2.nom  # Pokémon 2 est déclaré vainqueur si le Pokémon 1 fuit
            elif action == 'attaquer':
                # Pokémon 1 attaque le Pokémon 2
                degats = Combat.calculer_degats(pokemon1, pokemon1.attaque_de_base, pokemon2)
                Combat.appliquer_degats(pokemon2, degats)
                print(f"{pokemon1.nom} attaque {pokemon2.nom} avec {pokemon1.attaque_de_base.nom}, infligeant {degats} dégâts. PV restants de {pokemon2.nom} : {pokemon2.pv}")
                if pokemon2.pv <= 0:
                    print(f"{pokemon1.nom} est le vainqueur du combat !")
                    return pokemon1.nom
            else:
                print("Action non reconnue. Veuillez choisir 'attaquer' ou 'fuir'.")
                continue  # Continue la boucle si l'action n'est pas reconnue

            time.sleep(1)
            # Pokémon 2 attaque le Pokémon 1
            degats = Combat.calculer_degats(pokemon2, pokemon2.attaque_de_base, pokemon1)
            Combat.appliquer_degats(pokemon1, degats)
            print(f"{pokemon2.nom} attaque {pokemon1.nom} avec {pokemon2.attaque_de_base.nom}, infligeant {degats} dégâts. PV restants de {pokemon1.nom} : {pokemon1.pv}")
            if pokemon1.pv <= 0:
                print(f"Le {pokemon2.nom} adverse a gagné le combat !")
                return pokemon2.nom