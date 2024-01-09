class Combat:
    @staticmethod
    def calculer_degats(attaquant, attaque, defenseur):
        # Calcul du coefficient d'efficacité en fonction des types
        coefficient_eff = 1.0 
        if attaque.type.nom in defenseur.type.faiblesses:
            coefficient_eff = 2.0
        elif attaque.type.nom in defenseur.type.forces:
            coefficient_eff = 0.5
        elif attaque.type.nom in defenseur.type.nulle_defense:
            coefficient_eff = 0.0

        # Formule de base pour le calcul des dégâts
        degats = (((attaquant.lvl * 0.4 + 2) * attaquant.attaque * attaque.puissance / (defenseur.defense * 50)) + 2) * coefficient_eff
        return degats