from classes.Pokemon import Pokemon
from classes.Attaque import Attaque

def main():
    # Charger les Pokémon à partir du fichier JSON
    pokemons = Pokemon.import_json("json/pokemon.json")
    
    # Trouver Salamèche et Carapuce
    salameche = next(p for p in pokemons if p.nom == "Salameche")
    carapuce = next(p for p in pokemons if p.nom == "Carapuce")
    pikachu = next(p for p in pokemons if p.nom == "Pikachu")

    salameche.attaque_de_base = Attaque.flammèche()
    carapuce.attaque_de_base = Attaque.pistolet_a_o()
    pikachu.attaque_de_base = Attaque.tonnerre()


    # Simulation d'une attaque de Salamèche sur Carapuce
    degats_salamèche = salameche.utiliser_attaque(carapuce)
    print(f"Dégâts infligés par Salamèche à Carapuce : {int(degats_salamèche)}")

    # Simulation d'une attaque de Carapuce sur Salamèche
    degats_carapuce = carapuce.utiliser_attaque(salameche)
    print(f"Dégâts infligés par Carapuce à Salamèche : {int(degats_carapuce)}")

    # Simulation d'une attaque de Pikachu sur Salamèche
    degats_pikachu = pikachu.utiliser_attaque(salameche)
    print(f"Dégâts infligés par Pikachu à Salamèche : {int(degats_pikachu)}")

if __name__ == "__main__":
    main()