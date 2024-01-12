import os
import pygame
from pygame.locals import *
import sys
import json
import time

class AjouterPokemon:
    def __init__(self):
        # Initialisation de pygame
        pygame.init()
        
        # Crée la fenêtre
        self.fenetre = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Ajouter un pokemon")
        
        # Horloge
        self.clock = pygame.time.Clock()

        # Chargement bg, titre, police, cadre texte
        self.bg = pygame.image.load("images/background/bg_ajout_pokemon1.png").convert()
        self.titre = pygame.image.load("titre/ajoute_ton_pokemon.png").convert_alpha()
        self.police = pygame.font.Font("police/Pokemon Solid.ttf", 30)
        self.police2 = pygame.font.Font("police/Retro_gaming.ttf", 15)
        self.cadre_texte = pygame.image.load("images/cadre_texte/cadre_texte1.png").convert_alpha()

        # Chargement des silhouettes
        self.silhouettes = [
            pygame.image.load("images/pokemon/roucoul1.png").convert_alpha(),
            pygame.image.load("images/pokemon/rattata1.png").convert_alpha(),
            pygame.image.load("images/pokemon/osselait1.png").convert_alpha()
        ]

        # Positions des silhouettes
        self.positions_silhouettes = [
            (70, 380),
            (300, 380),
            (570, 380)
        ]

        # Rectangles des silhouettes
        self.rectangles_silhouettes = [pygame.Rect(pos, (self.silhouettes[i].get_width(), self.silhouettes[i].get_height())) for i, pos in enumerate(self.positions_silhouettes)]

        # Initialisation des attributs
        self.nom = [
            "Roucool",
            "Rattata",
            "Osselait"
        ]
        self.type = [
            "vol",
            "Normal",
            "sol"
        ]

        self.vie = 100
        self.niveau = 1
        self.attaque = 20
        self.defense = 20

        self.index_pokemon = None
        self.message_affiche = False
        self.temps_affichage_message = 0

    def pour_ajouter_fichier(self):
        if self.index_pokemon is not None:
            with open("json/pokemon.json", "r") as f:
                pokemon = json.load(f)

            new_pokemon = {
                "nom": self.nom[self.index_pokemon],
                "type": self.type[self.index_pokemon],
                "vie": self.vie,
                "niveau": self.niveau,
                "attaque": self.attaque,
                "defense": self.defense
            }

            pokemon.append(new_pokemon)

            with open("json/pokemon.json", "w") as f:
                json.dump(pokemon, f, indent=-1)
    
    def gerer_evenements(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                for i, rect in enumerate(self.rectangles_silhouettes):
                    if rect.collidepoint(event.pos):
                        self.index_pokemon = i
                        self.pour_ajouter_fichier()
                        self.message_affiche = True
                        
                        pygame.display.flip()
                        

    def afficher(self):
        # Affiche bg, titre
        self.fenetre.blit(self.bg, (0, 0))
        self.fenetre.blit(self.titre, (110, 240))

        # Affiche les silhouettes
        for i, silhouette in enumerate(self.silhouettes):
            self.fenetre.blit(silhouette, self.positions_silhouettes[i])

        # Affiche cadre texte
        for i in range(3):
            self.fenetre.blit(self.cadre_texte, (20 + i * 270, 530))

        # Affiche les informations du premier Pokémon
        self.texte = self.police2.render(f"Nom : {self.nom[0]}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (50, 565))
        self.texte = self.police2.render(f"Type : {self.type[0]}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (50, 595))
        self.texte = self.police2.render(f"Vie : {self.vie}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (50, 625))
        self.texte = self.police2.render(f"Niveau : {self.niveau}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (50, 655))
        self.texte = self.police2.render(f"Attaque : {self.attaque}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (50, 685))
        self.texte = self.police2.render(f"Défense : {self.defense}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (50, 715))

        # Affiche les informations du deuxième Pokémon
        self.texte = self.police2.render(f"Nom : {self.nom[1]}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (320, 565))
        self.texte = self.police2.render(f"Type : {self.type[1]}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (320, 595))
        self.texte = self.police2.render(f"Vie : {self.vie}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (320, 625))
        self.texte = self.police2.render(f"Niveau : {self.niveau}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (320, 655))
        self.texte = self.police2.render(f"Attaque : {self.attaque}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (320, 685))
        self.texte = self.police2.render(f"Défense : {self.defense}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (320, 715))

        # Affiche les informations du troisième Pokémon
        self.texte = self.police2.render(f"Nom : {self.nom[2]}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (590, 565))
        self.texte = self.police2.render(f"Type : {self.type[2]}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (590, 595))
        self.texte = self.police2.render(f"Vie : {self.vie}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (590, 625))
        self.texte = self.police2.render(f"Niveau : {self.niveau}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (590, 655))
        self.texte = self.police2.render(f"Attaque : {self.attaque}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (590, 685))
        self.texte = self.police2.render(f"Défense : {self.defense}", True, (0, 0, 0))
        self.fenetre.blit(self.texte, (590, 715))

    # Afficher le message si nécessaire
        if self.message_affiche:
            if pygame.time.get_ticks() - self.temps_affichage_message < 8000:
                self.texte = self.police.render(f"Le pokemon {self.nom[self.index_pokemon]} est ajouté !", True, (0, 0,0))
                self.fenetre.blit(self.texte, (200, 350))
            else:
                self.message_affiche = False
                

                


# Test du code
if __name__ == "__main__":
    ajout_pokemon = AjouterPokemon()
    
    while True:
        
        ajout_pokemon.afficher()
        ajout_pokemon.gerer_evenements()
        pygame.display.flip()
        ajout_pokemon.clock.tick(60)  # 30 FPS
