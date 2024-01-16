import pygame as pg
import cv2
# import numpy as np
import json
import random

with open("json/pokemon.json", "r") as fichier:
    donneesPokedex = json.load(fichier)

class Nouvelle_partie:
    def __init__(self, largeur, hauteur):
        pg.init()
        self.largeur = largeur
        self.hauteur = hauteur
        self.fenetre = pg.display.set_mode((self.largeur, self.hauteur))
        pg.display.set_caption("Pokemon - Nouvelle partie")
        pg.display.set_icon(pg.image.load("images/logo/logopokeball.png"))
        self.image_fond = pg.image.load("images/background/paysage_pokemon_nouvelle_partie.jpg")
        self.image_fond_redimensionne = pg.transform.scale(self.image_fond, (800, 800))

        self.image_carte_pokemon = pg.image.load("images/background/cadre carte vide.png")
        self.image_carte_pokemon_redimensionne = pg.transform.scale(self.image_carte_pokemon, (450, 620))

        font_chemin = "police/Pokemon Solid.ttf"
        font = pg.font.Font(font_chemin, 30)

        self.nom_dresseur = pg.image.load("titre/nom-dresseur.png")
        self.nom_dresseur = pg.transform.scale(self.nom_dresseur, (400, 100))
        
        self.input_box = pg.Rect(300, 100, 290, 50)
        self.is_input_active = False
        self.texte = ""
        self.font = pg.font.Font(None, 36)

        self.fleche_gauche = pg.image.load("images/bouton/fleche-gauche.png")
        self.fleche_gauche = pg.transform.scale(self.fleche_gauche, (40, 40))

        self.fleche_droite = pg.image.load("images/bouton/fleche-droite.png")
        self.fleche_droite = pg.transform.scale(self.fleche_droite, (40, 40))



        self.index_pokemon = 0
        
    
    def flouterImage(self, image):
        image_np = pg.surfarray.array3d(image)
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        blurred_image = cv2.GaussianBlur(image_np, (25, 25), 0)

        blurred_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)
        blurred_surface = pg.surfarray.make_surface(blurred_image)

        return blurred_surface
    
    def fenetre_ecrire_nom(self):
        pg.draw.rect(self.fenetre, (255, 255, 255), self.input_box, 2)
        texte_surface = self.font.render(self.texte, True, (200, 0, 0))
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

    def afficherPokemon(self, index_pokemon):
        if 0 <= index_pokemon < len(donneesPokedex):
            self.index_pokemon = index_pokemon
            pokemon = donneesPokedex[index_pokemon]
            chemin_image = pokemon["image"]
            image_pokemon = pg.image.load(chemin_image)
            image_redimensionnee = pg.transform.scale(image_pokemon, (300, 300))
            self.fenetre.blit(image_redimensionnee, (250, 230))

            font_chemin = "police/Retro_Gaming.ttf"
            font = pg.font.Font(font_chemin, 16)

            font_chemin_nom = "police/Retro_Gaming.ttf"
            font_nom = pg.font.Font(font_chemin_nom, 30)
            nom_pokemon = font_nom.render(f"{pokemon['nom']}", True, (0, 0, 0))
            self.fenetre.blit(nom_pokemon, (300, 185))

            font_chemin_type = "police/Retro_Gaming.ttf"
            font_type = pg.font.Font(font_chemin_type, 20)
            type_pokemon = font_type.render(f"Type : {pokemon['type']}", True, (0, 0, 0))
            self.fenetre.blit(type_pokemon, (310, 525))

            defense_pokemon = font.render(f"Défense : {pokemon['defense']}", True, (0, 0, 0))
            self.fenetre.blit(defense_pokemon, (220, 580))

            puissance_pokemon = font.render(f"Puissance d'attaque : {pokemon['attaque']}", True, (0, 0, 0))
            self.fenetre.blit(puissance_pokemon, (220, 640))

            pointDeVie_pokemon = font.render(f"Point de vie : {pokemon['vie']}", True, (0, 0, 0))
            self.fenetre.blit(pointDeVie_pokemon, (220, 700))

            lancer_partie = font.render(f"Lancer", True, (0, 200, 0))
            self.fenetre.blit(lancer_partie, (535, 743))

            self.fenetre.blit(self.fleche_gauche, (200, 400))
            self.fenetre.blit(self.fleche_droite, (550, 400))

            chemin_bouton_retour = "images/bouton/bouton-retour.png"
            bouton_retour = pg.image.load(chemin_bouton_retour)
            bouton_retour_redimensionne = pg.transform.scale(bouton_retour, (110, 50))
            self.fenetre.blit(bouton_retour_redimensionne, (680, 720))

    
    def choix_pokemon_aleatoire(self):
        pokemon_aleatoire = random.choice(donneesPokedex)
        nom_pokemon = pokemon_aleatoire["nom"]
        print(f"Pokemon choisi aléatoirement : {nom_pokemon}")
        return nom_pokemon

    def choix_pokemon_joueur(self):
        nom_pokemon = donneesPokedex[self.index_pokemon]["nom"]
        print(f"Pokemon choisi par le joueur : {nom_pokemon}")
        return nom_pokemon


    def afficher_fenetre(self):
        while True:
            image_floue = self.flouterImage(self.image_fond_redimensionne)
            self.fenetre.blit(image_floue, (0, 0))
            self.fenetre.blit(self.nom_dresseur, (200, 20))
            self.fenetre.blit(self.image_carte_pokemon_redimensionne, (180, 170))
            self.fenetre_ecrire_nom()
            self.afficherPokemon(self.index_pokemon)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                self.zone_texte(event)
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 200 <= event.pos[0] <= 240 and 400 <= event.pos[1] <= 440:
                            self.afficherPokemon(self.index_pokemon - 1)
                        elif 550 <= event.pos[0] <= 590 and 400 <= event.pos[1] <= 440:
                            self.afficherPokemon(self.index_pokemon + 1)
                        elif 535 <= event.pos[0] <= 600 and 743 <= event.pos[1] <= 760:
                            self.choix_pokemon_aleatoire()
                            self.choix_pokemon_joueur()
                            print("Lancer la partie")
                            return True
                        elif 680 <= event.pos[0] <= 790 and 720 <= event.pos[1] <= 770:
                            print("Retour")
                            return False

            pg.display.flip()

fenetre = Nouvelle_partie(800, 800)
fenetre.afficher_fenetre()
