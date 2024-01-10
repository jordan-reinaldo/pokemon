from .Type import Type

class Attaque:
    def __init__(self, nom, puissance, type_attaque):
        self.nom = nom
        self.puissance = puissance
        self.type = type_attaque

    @staticmethod
    def flammeche():
        return Attaque("Flammèche", 40, Type.feu())

    @staticmethod
    def pistolet_a_o():
        return Attaque("Pistolet à O", 40, Type.eau())
    
    @staticmethod
    def tonnerre():
        return Attaque("Tonnerre", 90, Type.electrik())
    
    @staticmethod
    def tranche_herbe():
        return Attaque("Tranche Herbe", 70, Type.plante())
    
    @staticmethod
    def charge():
        return Attaque("Charge", 40, Type.normal())