import pygame as pg
import cv2
import numpy as np
import json

with open("json/pokedex.json", "r") as fichier:
    donneesPokedex = json.load(fichier)

class Pokedex:
    def __init__(self, largeur, hauteur):
        pg.init()
        self.largeur = largeur
        self.hauteur = hauteur
        self.fenetre = pg.display.set_mode((self.largeur, self.hauteur))
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
        self.cercle = pg.draw.circle(self.fenetre, (255, 0, 0), (155, 520), 25)

        self.couleur_fleche_gauche = (200, 0, 0)
        self.couleur_fleche_droite = (200, 0, 0)
        self.couleur_fleche_haut = (200, 0, 0)
        self.couleur_fleche_bas = (200, 0, 0)
        self.couleur_cercle = (200, 0, 0)

        self.son_clic = pg.mixer.Sound("musique/BEEP_touche.mp3")

        font_chemin = "police/Retro_Gaming.ttf"
        font = pg.font.Font(font_chemin, 25)

        self.acces_pokedex = font.render("Pokedex", True, (255, 0, 0))
        self.rect_acces_pokedex = self.acces_pokedex.get_rect(topleft=(270, 500))
        self.revenir_menu_pokedex = font.render("Revenir au menu", True, (255, 0, 0))
        self.rect_quitter_pokedex = self.revenir_menu_pokedex.get_rect(topleft=(270, 550))

        self.retour_menu = font.render("Retour", True, (255, 0, 0))
        self.rect_retour_menu = self.retour_menu.get_rect(topleft=(450, 620))


        self.index_pokemon = 0
        self.pokemon_affiche = 0
        self.index_evolution = 0

        self.afficher = True

    def flouterImage(self, image):
        image_np = pg.surfarray.array3d(image)
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        blurred_image = cv2.GaussianBlur(image_np, (25, 25), 0)

        blurred_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)
        blurred_surface = pg.surfarray.make_surface(blurred_image)

        return blurred_surface

    def diminuerLuminositeFleche(self, fleche):
        border_radius = 5
        fleche_couleur_temp = tuple(max(component - 50, 0) for component in self.couleur_fleche_bas)
        pg.draw.rect(self.fenetre, fleche_couleur_temp, fleche, border_radius=border_radius)
        pg.display.flip()
        pg.time.wait(100)
        pg.draw.rect(self.fenetre, self.couleur_fleche_bas, fleche, border_radius=border_radius)

    def gererDéfilementPokemon(self):
        for evenement in pg.event.get():
            if evenement.type == pg.QUIT:
                self.afficher = False
            elif evenement.type == pg.MOUSEBUTTONDOWN:
                if evenement.button == 1:
                    if self.fleche_gauche.collidepoint(evenement.pos):
                        self.son_clic.play()
                        self.diminuerLuminositeFleche(self.fleche_gauche)
                        self.afficherPokemon(self.index_pokemon - 1)
                        self.pokemon_affiche -= 1
                        if self.pokemon_affiche < 0:
                            self.afficherPokemon(len(donneesPokedex) - 1)
                            self.pokemon_affiche = len(donneesPokedex) - 1
                        print("Clic gauche sur la flèche gauche")
                    elif self.fleche_droite.collidepoint(evenement.pos):
                        self.son_clic.play()
                        self.diminuerLuminositeFleche(self.fleche_droite)
                        self.afficherPokemon(self.index_pokemon + 1)
                        self.pokemon_affiche += 1
                        if self.pokemon_affiche > len(donneesPokedex) - 1:
                            self.afficherPokemon(0)
                            self.pokemon_affiche = 0
                        print("Clic gauche sur la flèche droite")
                    elif self.fleche_haut.collidepoint(evenement.pos):
                        self.son_clic.play()
                        self.diminuerLuminositeFleche(self.fleche_haut)
                        self.afficherEvolutionPokemon(self.index_pokemon, self.index_evolution)
                        print("Clic gauche sur la flèche haut")
                    elif self.fleche_bas.collidepoint(evenement.pos):
                        self.son_clic.play()
                        self.diminuerLuminositeFleche(self.fleche_bas)
                        self.afficherEvolutionPokemon(self.index_pokemon, self.index_evolution)
                        print("Clic gauche sur la flèche bas")
                    elif self.cercle.collidepoint(evenement.pos):
                        self.cri_pokemon(self.index_pokemon)
                        print("Clic gauche sur le cercle")
                    elif self.rect_retour_menu.collidepoint(evenement.pos):
                        self.son_clic.play()
                        self.menuPokedex()
                        print("Clic gauche sur retour")

    def afficherPokemon(self, index_pokemon):
        if 0 <= index_pokemon < len(donneesPokedex):
            self.index_pokemon = index_pokemon
            pokemon = donneesPokedex[index_pokemon]
            chemin_image = pokemon["image"]
            image_pokemon = pg.image.load(chemin_image)
            image_redimensionnee = pg.transform.scale(image_pokemon, (210, 210))
            self.fenetre.blit(image_redimensionnee, (310, 125))

            font_chemin = "police/Retro_Gaming.ttf"
            font = pg.font.Font(font_chemin, 16)

            nom_pokemon = font.render(f"Nom : {pokemon['nom']}", True, (0, 0, 0))
            self.fenetre.blit(nom_pokemon, (270, 460))

            type_pokemon = font.render(f"Type : {pokemon['type']}", True, (0, 0, 0))
            self.fenetre.blit(type_pokemon, (270, 490))

            defense_pokemon = font.render(f"Défense : {pokemon['defense']}", True, (0, 0, 0))
            self.fenetre.blit(defense_pokemon, (270, 520))

            puissance_pokemon = font.render(f"Puissance d'attaque : {pokemon['puissance attaque']}", True, (0, 0, 0))
            self.fenetre.blit(puissance_pokemon, (270, 550))

            pointDeVie_pokemon = font.render(f"Point de vie : {pokemon['point de vie']}", True, (0, 0, 0))
            self.fenetre.blit(pointDeVie_pokemon, (270, 580))

            retour = font.render(f"Retour", True, (0, 200, 0))
            self.fenetre.blit(retour, (450, 620))

    def afficherEvolutionPokemon(self, index_pokemon, index_evolution):
        if 0 <= index_pokemon < len(donneesPokedex):
            self.index_pokemon = index_pokemon
            pokemon = donneesPokedex[index_pokemon]

            if 0 <= index_evolution < len(pokemon["evolution"]):
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

                puissance_pokemon = font.render(f"Puissance d'attaque : {evolution['puissance attaque']}", True, (0, 0, 0))
                self.fenetre.blit(puissance_pokemon, (270, 550))

                pointDeVie_pokemon = font.render(f"Point de vie : {evolution['point de vie']}", True, (0, 0, 0))
                self.fenetre.blit(pointDeVie_pokemon, (270, 580))

                
            
    def cri_pokemon(self, index_pokemon):
        if "cri" in donneesPokedex[index_pokemon]:
            chemin_cri = donneesPokedex[index_pokemon]["cri"]
            cri = pg.mixer.Sound(chemin_cri)
            cri.play()

    def afficherPokedex(self):
        while self.afficher:
            image_floue = self.flouterImage(self.image_fond)
            self.fenetre.blit(image_floue, (0, 0))
            self.fenetre.blit(self.imagePokedex_redimensionnee, (0, 80))
            self.afficherPokemon(self.pokemon_affiche)
            border_radius = 10
            pg.draw.rect(self.fenetre, self.couleur_fleche_gauche, self.fleche_gauche, border_radius=border_radius)
            pg.draw.rect(self.fenetre, self.couleur_fleche_droite, self.fleche_droite, border_radius=border_radius)
            pg.draw.rect(self.fenetre, self.couleur_fleche_haut, self.fleche_haut, border_radius=border_radius)
            pg.draw.rect(self.fenetre, self.couleur_fleche_bas, self.fleche_bas, border_radius=border_radius)
            self.cercle = pg.draw.circle(self.fenetre, self.couleur_cercle, (705, 535), 35)
            self.gererDéfilementPokemon()
            pg.display.flip()

    def menuPokedex(self):
        while self.afficher:
            image_floue = self.flouterImage(self.image_fond)
            self.fenetre.blit(image_floue, (0, 0))
            self.fenetre.blit(self.imagePokedex_redimensionnee, (0, 80))
            self.fenetre.blit(self.acces_pokedex, (270, 500))
            self.fenetre.blit(self.revenir_menu_pokedex, (270, 550))
            self.fenetre.blit(self.imageTitrePokedex_redimensionnee, (250, 185))
            border_radius = 10
            pg.draw.rect(self.fenetre, self.couleur_fleche_gauche, self.fleche_gauche, border_radius=border_radius)
            pg.draw.rect(self.fenetre, self.couleur_fleche_droite, self.fleche_droite, border_radius=border_radius)
            pg.draw.rect(self.fenetre, self.couleur_fleche_haut, self.fleche_haut, border_radius=border_radius)
            pg.draw.rect(self.fenetre, self.couleur_fleche_bas, self.fleche_bas, border_radius=border_radius)
            self.cercle = pg.draw.circle(self.fenetre, self.couleur_cercle, (705, 535), 35)

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
