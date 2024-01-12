import pygame as pg
import cv2
import numpy as np
import json


with open ("json/pokedex.json", "r") as fichier: #ouvrir le fichier pokedex.json en mode lecture
    donneesPokedex = json.load(fichier) #charger les données du fichier pokedex.json dans la variable donnees

class Pokedex: #classe Pokedex #classe = modèle de données (attributs) et de fonctions (méthodes) #objet = instance de la classe (ex: pokedex = Pokedex(800, 800))
    def __init__(self, largeur, hauteur):
        pg.init()
        self.largeur = largeur
        self.hauteur = hauteur
        self.fenetre = pg.display.set_mode((self.largeur, self.hauteur)) #set_mode = définir le mode d'affichage de la fenêtre 
        pg.display.set_caption("Pokedex")
        self.image_fond = pg.image.load("images/pokedex/paysage.jpg")
        
        self.imagePokedex = pg.image.load("images/pokedex/pokedex1.png")
        self.imagePokedex_redimensionnee = pg.transform.scale(self.imagePokedex, (800, 600))

        self.imageTitrePokedex = pg.image.load("images/pokedex/titrePokedex.png")
        self.imageTitrePokedex_redimensionnee = pg.transform.scale(self.imageTitrePokedex, (300, 100))
        
        self.fleche_gauche = pg.Rect(110, 520, 50, 25)
        self.fleche_droite = pg.Rect(175, 520, 50, 25)
        self.fleche_haut = pg.Rect(155, 475, 25, 50)
        self.fleche_bas = pg.Rect(155, 540, 25, 50)
        
        self.couleur_fleche_gauche = (255, 0, 0)
        self.couleur_fleche_droite = (255, 0, 0)
        self.couleur_fleche_haut = (255, 0, 0)
        self.couleur_fleche_bas = (255, 0, 0)

        self.son_clic = pg.mixer.Sound("musique/BEEP_touche.mp3")

        font_chemin = "police/Retro_Gaming.ttf"
        font = pg.font.Font(font_chemin, 25)
        # font.set_bold(True)
        self.acces_pokedex = font.render("Pokedex", True, (255, 0, 0))
        self.rect_acces_pokedex = self.acces_pokedex.get_rect(topleft = (270, 500))
        self.revenir_menu_pokedex = font.render("Revenir au menu", True, (255, 0, 0))
        self.rect_quitter_pokedex = self.revenir_menu_pokedex.get_rect(topleft = (270, 550))

        self.index_pokemon = 0 #index du pokemon 
        self.pokemon_affiche = 0 #numéro du pokemon affiché
        self.index_evolution = 0 #index de l'évolution du pokemon


        self.afficher = True #afficher = True : afficher le pokedex ; afficher = False : ne pas afficher le pokedex

    def flouterImage(self, image): #flouter l'image de fond du pokedex (paysage.jpg) 
        # Convertir l'image Pygame en tableau numpy pour OpenCV
        image_np = pg.surfarray.array3d(image) #array3d = tableau 3 dimensions (x, y, couleur) #surfarray = tableau de surface
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR) # Convertir l'image RGB en BGR pour OpenCV #RGB = Red Green Blue ; BGR = Blue Green Red #cvtColor = convertir la couleur

        # Appliquer le flou gaussien avec OpenCV
        blurred_image = cv2.GaussianBlur(image_np, (25, 25), 0) # 25, 25 = taille du noyau gaussien (doit être impair) ; 0 = écart-type en x et y 

        # Convertir l'image floutée de retour à Pygame
        blurred_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB) #cv2.cvtColor = convertir la couleur #cv2.COLOR_BGR2RGB = convertir de BGR à RGB
        blurred_surface = pg.surfarray.make_surface(blurred_image)

        return blurred_surface

    def gererDéfilementGaucheDroitePokemon(self):
        for evenement in pg.event.get():
            if evenement.type == pg.QUIT:
                self.afficher = False
            elif evenement.type == pg.MOUSEBUTTONDOWN:
                if evenement.button == 1:
                    if self.fleche_gauche.collidepoint(evenement.pos):
                        self.son_clic.play()
                        self.afficherPokemon(self.index_pokemon - 1)
                        self.pokemon_affiche -= 1
                        if self.pokemon_affiche < 0:
                            self.afficherPokemon(len(donneesPokedex) - 1)  # Afficher le dernier Pokémon
                            self.pokemon_affiche = len(donneesPokedex) - 1
                        print("Clic gauche sur la flèche gauche")
                    elif self.fleche_droite.collidepoint(evenement.pos):
                        self.son_clic.play()
                        self.afficherPokemon(self.index_pokemon + 1)
                        self.pokemon_affiche += 1
                        if self.pokemon_affiche > len(donneesPokedex) - 1:
                            self.afficherPokemon(0)  # Afficher le premier Pokémon
                            self.pokemon_affiche = 0
                        print("Clic gauche sur la flèche droite")
                    elif self.fleche_haut.collidepoint(evenement.pos):
                        self.son_clic.play()
                        self.afficherEvolutionPokemon(self.index_pokemon, self.index_evolution)
                        print("Clic gauche sur la flèche haut")
                    elif self.fleche_bas.collidepoint(evenement.pos):
                        self.son_clic.play()
                        self.afficherEvolutionPokemon(self.index_pokemon, self.index_evolution) 
                        print("Clic gauche sur la flèche bas")

    def afficherPokemon(self, index_pokemon):
        if 0 <= index_pokemon < len(donneesPokedex):  # Vérifie si l'index est dans la plage valide
            self.index_pokemon = index_pokemon  # Mettre à jour l'index du Pokémon actuel
            pokemon = donneesPokedex[index_pokemon]
            chemin_image = pokemon["image"]
            image_pokemon = pg.image.load(chemin_image)
            image_redimensionnee = pg.transform.scale(image_pokemon, (210, 210))
            self.fenetre.blit(image_redimensionnee, (310, 125))

            font_chemin = "police/Retro_Gaming.ttf"
            font = pg.font.Font(font_chemin, 16)
            # font.set_bold(True)

            nom_pokemon = font.render(f"Nom : {pokemon["nom"]}", True, (0, 0, 0))
            self.fenetre.blit(nom_pokemon, (270, 460))

            type_pokemon = font.render(f"Type : {pokemon["type"]}", True, (0, 0, 0))
            self.fenetre.blit(type_pokemon, (270, 490))

            defense_pokemon = font.render(f"Défense : {pokemon["defense"]}", True, (0, 0, 0))
            self.fenetre.blit(defense_pokemon, (270, 520))
            
            puissance_pokemon = font.render(f"Puissance d'attaque : {pokemon["puissance attaque"]}", True, (0, 0, 0))
            self.fenetre.blit(puissance_pokemon, (270, 550))

            pointDeVie_pokemon = font.render(f"Point de vie : {pokemon["point de vie"]}", True, (0, 0, 0))
            self.fenetre.blit(pointDeVie_pokemon, (270, 580))

        
    def afficherEvolutionPokemon(self, index_pokemon, index_evolution): #afficher l'évolution du pokemon
         
        if 0 <= index_pokemon < len(donneesPokedex): # Vérifie si l'index est dans la plage valide
            self.index_pokemon = index_pokemon
            pokemon = donneesPokedex[index_pokemon]

            if 0 <= index_evolution < len(pokemon["evolution"]): # Vérifie si l'index est dans la plage valide
                evolution = pokemon["evolution"][index_evolution]
                chemin_image = evolution["image"]
                image_pokemon = pg.image.load(chemin_image)
                image_redimensionnee = pg.transform.scale(image_pokemon, (210, 210))
                self.fenetre.blit(image_redimensionnee, (310, 125))

                font_chemin = "police/Retro_Gaming.ttf"
                font = pg.font.Font(font_chemin, 16)

                nom_pokemon = font.render(f"Nom : {evolution['nom']}", True, (0, 0, 0))
                self.fenetre.blit(nom_pokemon, (270, 460))

                type_pokemon = font.render(f"Type : {evolution['type']}", True, (0, 0, 0))
                self.fenetre.blit(type_pokemon, (270, 490))

                defense_pokemon = font.render(f"Défense : {evolution['defense']}", True, (0, 0, 0))
                self.fenetre.blit(defense_pokemon, (270, 520))

                puissance_pokemon = font.render(f"Puissance d'attaque : {evolution['puissance attaque']}", True,
                                               (0, 0, 0))
                self.fenetre.blit(puissance_pokemon, (270, 550))

                pointDeVie_pokemon = font.render(f"Point de vie : {evolution['point de vie']}", True, (0, 0, 0))
                self.fenetre.blit(pointDeVie_pokemon, (270, 580))

    def afficherPokedex(self): #afficher le pokedex 
        while self.afficher: #tant que self.afficher = True
            image_floue = self.flouterImage(self.image_fond) #flouter l'image de fond du pokedex (paysage.jpg) 
            self.fenetre.blit(image_floue, (0, 0)) #afficher l'image floutée
            self.fenetre.blit(self.imagePokedex_redimensionnee, (0, 80)) #afficher l'image du pokedex
            self.afficherPokemon(self.pokemon_affiche)
            pg.draw.rect(self.fenetre, self.couleur_fleche_gauche, self.fleche_gauche)
            pg.draw.rect(self.fenetre, self.couleur_fleche_droite, self.fleche_droite)
            pg.draw.rect(self.fenetre, self.couleur_fleche_haut, self.fleche_haut)
            pg.draw.rect(self.fenetre, self.couleur_fleche_bas, self.fleche_bas)
            self.gererDéfilementGaucheDroitePokemon() 
            pg.display.flip() #rafraichir l'affichage

    def menuPokedex(self):
        while self.afficher:
            image_floue = self.flouterImage(self.image_fond)
            self.fenetre.blit(image_floue, (0, 0))
            self.fenetre.blit(self.imagePokedex_redimensionnee, (0, 80))
            self.fenetre.blit(self.acces_pokedex, (270, 500))  # Affichage du bouton
            self.fenetre.blit(self.revenir_menu_pokedex, (270, 550))  # Affichage du bouton
            self.fenetre.blit(self.imageTitrePokedex_redimensionnee, (250, 185))

            for evenement in pg.event.get():
                if evenement.type == pg.QUIT:
                    self.afficher = False
                elif evenement.type == pg.MOUSEBUTTONDOWN:
                    if evenement.button == 1:
                        if self.rect_acces_pokedex.collidepoint(evenement.pos):
                            self.son_clic.play()
                            self.afficherPokedex()
                            print("Clic sur Pokedex")
                        elif self.rect_quitter_pokedex.collidepoint(evenement.pos):
                            self.son_clic.play()
                            print("Clic sur Quitter") 
                    

            pg.display.flip()


            
fenetre = Pokedex(800, 800)

fenetre.menuPokedex()