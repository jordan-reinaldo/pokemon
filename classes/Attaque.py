from .Type import Type

class Attaque:
    def __init__(self, nom, puissance, type_attaque):
        self.nom = nom
        self.puissance = puissance
        self.type = type_attaque

    @staticmethod
    def flammèche():
        return Attaque("Flammèche", 40, Type.feu())

    @staticmethod
    def pistolet_a_o():
        return Attaque("Pistolet à O", 40, Type.eau())
    
    @staticmethod
    def tonnerre():
        return Attaque("Tonnerre", 90, Type.electrik())