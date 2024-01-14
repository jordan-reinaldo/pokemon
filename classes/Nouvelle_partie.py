import pygame as pg
import cv2
import numpy as np
import json

with open("json/pokedex.json", "r") as fichier:
    donneesPokedex = json.load(fichier)

class Nouvelle_partie:
    def __init__(self, largeur, hauteur):
        pg.init()
        self.largeur = largeur
        self.hauteur = hauteur
        self.fenetre = pg.display.set_mode((self.largeur, self.hauteur))
        pg.display.set_caption("Pokemon - Nouvelle partie")
        self.image_fond = pg.image.load("images/background/Pikachu_de_dos.jpg")
        self.image_fond_redimensionne = pg.transform.scale(self.image_fond, (800, 800))

        font_chemin = "police/Pokemon Solid.ttf"
        font = pg.font.Font(font_chemin, 30)

        self.nom_dresseur = font.render("Nom du dresseur", True, (200, 0, 0))
        self.nom_dresseur_rect = self.nom_dresseur.get_rect(topleft=(270, 150))
        self.input_box = pg.Rect(250, 200, 290, 50)
        self.is_input_active = False
        self.texte = ""
        self.font = pg.font.Font(None, 36)
    
    def flouterImage(self, image):
        image_np = pg.surfarray.array3d(image)
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        blurred_image = cv2.GaussianBlur(image_np, (25, 25), 0)

        blurred_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)
        blurred_surface = pg.surfarray.make_surface(blurred_image)

        return blurred_surface
    
    def fenetre_ecrire_nom(self):
        pg.draw.rect(self.fenetre, (255, 255, 255), self.input_box, 2)
        texte_surface = self.font.render(self.texte, True, (0, 0, 0))
        width = max(200, texte_surface.get_width() + 10)
        self.input_box.w = width
        self.fenetre.blit(texte_surface, (self.input_box.x + 5, self.input_box.y + 5))

    def zone_texte(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.is_input_active = not self.is_input_active
            else:
                self.is_input_active = False

        if event.type == pg.KEYDOWN:
            if self.is_input_active:
                if event.key == pg.K_RETURN:
                    print(self.texte)
                    self.texte = ""
                elif event.key == pg.K_BACKSPACE:
                    self.texte = self.texte[:-1]
                else:
                    self.texte += event.unicode
    
    def afficher_fenetre(self):
        while True:
            image_floue = self.flouterImage(self.image_fond_redimensionne)
            self.fenetre.blit(image_floue, (0, 0))
            self.fenetre.blit(self.nom_dresseur, (270, 150))
            self.fenetre_ecrire_nom()
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                self.zone_texte(event)

fenetre = Nouvelle_partie(800, 800)
fenetre.afficher_fenetre()
