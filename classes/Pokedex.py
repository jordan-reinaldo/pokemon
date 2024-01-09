import pygame as pg
import cv2
import numpy as np
import json

with open ("pokemon/json/pokedex.json", "r") as fichier: #ouvrir le fichier pokedex.json en mode lecture
    donneesPokedex = json.load(fichier) #charger les données du fichier pokedex.json dans la variable donnees


class Pokedex:
    def __init__(self, largeur, hauteur):
        pg.init()
        self.largeur = largeur
        self.hauteur = hauteur
        self.fenetre = pg.display.set_mode((self.largeur, self.hauteur)) #set_mode = définir le mode d'affichage de la fenêtre 
        pg.display.set_caption("Pokedex")
        self.image_fond = pg.image.load("pokemon/images/pokedex/paysage.jpg").convert()
        self.imagePokedex = pg.image.load("pokemon/images/pokedex/pokedex1.png")
        self.imagePokedex_redimensionnee = pg.transform.scale(self.imagePokedex, (800, 600))
        
        self.afficher = True #afficher = True : afficher le pokedex ; afficher = False : ne pas afficher le pokedex

    def flouterImage(self, image):
        # Convertir l'image Pygame en tableau numpy pour OpenCV
        image_np = pg.surfarray.array3d(image) #array3d = tableau 3 dimensions (x, y, couleur) #surfarray = tableau de surface
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR) # Convertir l'image RGB en BGR pour OpenCV #RGB = Red Green Blue ; BGR = Blue Green Red #cvtColor = convertir la couleur

        # Appliquer le flou gaussien avec OpenCV
        blurred_image = cv2.GaussianBlur(image_np, (25, 25), 0) # 25, 25 = taille du noyau gaussien (doit être impair) ; 0 = écart-type en x et y 

        # Convertir l'image floutée de retour à Pygame
        blurred_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB) #cv2.cvtColor = convertir la couleur #cv2.COLOR_BGR2RGB = convertir de BGR à RGB
        blurred_surface = pg.surfarray.make_surface(blurred_image)

        return blurred_surface

    def gererEvenements(self):
        for evenement in pg.event.get():
            if evenement.type == pg.QUIT:
                self.afficher = False #fermer le pokedex

    def afficherPokemon(self, index_pokemon): #afficher le pokemon
        # Afficher les informations du pokemon
        pokemon = donneesPokedex[index_pokemon] #index_pokemon = numéro du pokemon
    
        chemin_image = pokemon["image"]

        image_pokemon = pg.image.load(chemin_image)
        image_redimensionnee = pg.transform.scale(image_pokemon, (125, 125))
        self.fenetre.blit(image_redimensionnee, (350, 190)) #afficher l'image du pokemon (redimensionnée) aux coordonnées (350, 190) 
        
        pg.display.flip()

    def zone_cliquable(self, x, y, largeur, hauteur):
        # Créer une zone cliquable rectangulaire aux coordonnées spécifiées
        rect = pg.Rect(x, y, largeur, hauteur)
        couleur = (255, 0, 0)  # Couleur de la zone 
        couleur_hover = (0, 255, 0)  # Couleur lorsque la souris survole la zone (vert dans cet exemple)
        est_survol = False  # Indicateur pour savoir si la souris survole la zone

        while self.afficher:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.afficher = False
                elif event.type == pg.MOUSEMOTION:
                    est_survol = rect.collidepoint(pg.mouse.get_pos())

                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clic gauche de la souris
                        if rect.collidepoint(event.pos):
                            print("Clic dans la zone cliquable !")

            # Dessiner la zone cliquable sur la fenêtre
            couleur_affichage = couleur_hover if est_survol else couleur
            pg.draw.rect(self.fenetre, couleur_affichage, rect)
            pg.display.flip()
        

    def afficherPokedex(self): #afficher le pokedex 
        while self.afficher: #tant que self.afficher = True
            image_floue = self.flouterImage(self.image_fond) #flouter l'image de fond du pokedex (paysage.jpg) 
            self.fenetre.blit(image_floue, (0, 0)) #afficher l'image floutée
            self.fenetre.blit(self.imagePokedex_redimensionnee, (0, 80)) #afficher l'image du pokedex
            self.gererEvenements() #gérer les évènements (fermer le pokedex)
            self.afficherPokemon(0) #afficher le pokemon numéro 0 (Pikachu)
            self.zone_cliquable(110, 520, 50, 25) #afficher la zone cliquable du pokedex 
            pg.display.flip() #rafraichir l'affichage

fenetre = Pokedex(800, 800)

fenetre.afficherPokedex()
