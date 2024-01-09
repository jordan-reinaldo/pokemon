import pygame as pg 

class Pokedex:
    def __init__(self, largeur, hauteur):
        pg.init()
        self.largeur = largeur
        self.hauteur = hauteur
        self.fenetre = pg.display.set_mode((self.largeur, self.hauteur))
        self.couleur_fond = (255, 255, 255)
        pg.display.set_caption("Pokedex")
        self.imagePokedex = pg.image.load("pokemon/images/pokedex/pokedex1.png")
        self.imagePokedex_redimensionnee = pg.transform.scale(self.imagePokedex, (800, 600))
        self.afficher = True

    def gererEvenements(self):
        for evenement in pg.event.get():
            if evenement.type == pg.QUIT:
                self.afficher = False

    def raffraichirAffichage(self):
        pg.display.flip()

    def afficherPokedex(self):
        while self.afficher:
            self.fenetre.fill(self.couleur_fond)
            self.fenetre.blit(self.imagePokedex_redimensionnee, (0, 80))
            self.gererEvenements()
            self.raffraichirAffichage()

fenetre = Pokedex(800, 800)
fenetre.afficherPokedex()
