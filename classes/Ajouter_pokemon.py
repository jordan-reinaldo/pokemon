import os
import pygame
from pygame.locals import *
import sys
from json import *
import random

class Ajouter_pokemon:
    script_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        pygame.init()

        # Créer la fenêtre
        self.__fenetre = pygame.display.set_mode((800, 800))
        self.__bg = pygame.image.load("images/background/bg_ajout_pokemon.png")
        pygame.display.set_caption("Pokemon Arena-Fighter")

        # Charger la police
        self.police = pygame.font.Font("police/pokemon Solid.ttf", 30)

        # silhouette pikachu
        self.__silhouette = pygame.image.load("images/pokemon/pikachu1.png").convert_alpha()
        self.__silhouette_rect = self.__silhouette.get_rect()
        self.__silhouette_rect.x = 50
        self.__silhouette_rect.y = 400

        # silhouette carapuce
        self.__silhouette_carapuce = pygame.image.load("images/pokemon/carapuce1.png").convert_alpha()
        self.__silhouette_carapuce_rect = self.__silhouette_carapuce.get_rect()
        self.__silhouette_carapuce_rect.x = 250
        self.__silhouette_carapuce_rect.y = 300

        # silhouette salameche
        self.__silhouette_salameche = pygame.image.load("images/pokemon/salameche1.png").convert_alpha()
        self.__silhouette_salameche_rect = self.__silhouette_salameche.get_rect()
        self.__silhouette_salameche_rect.x = 350
        self.__silhouette_salameche_rect.y = 500

        # silhouette bulbizarre
        self.__silhouette_bulbizarre = pygame.image.load("images/pokemon/bulbizarre1.png").convert_alpha()
        self.__silhouette_bulbizarre_rect = self.__silhouette_bulbizarre.get_rect()
        self.__silhouette_bulbizarre_rect.x = 450
        self.__silhouette_bulbizarre_rect.y = 300

        # silhouette evoli
        self.__silhouette_evoli = pygame.image.load("images/pokemon/evoli1.png").convert_alpha()
        self.__silhouette_evoli_rect = self.__silhouette_evoli.get_rect()
        self.__silhouette_evoli_rect.x = 600
        self.__silhouette_evoli_rect.y = 400

    

    # choisir silhouette en cliquant dessus
    def choisir_silhouette(self):
        self.__fenetre.blit(self.__bg, (0, 0))
        self.__fenetre.blit(self.__silhouette, self.__silhouette_rect)
        self.__fenetre.blit(self.__silhouette_carapuce, self.__silhouette_carapuce_rect)
        self.__fenetre.blit(self.__silhouette_salameche, self.__silhouette_salameche_rect)
        self.__fenetre.blit(self.__silhouette_bulbizarre, self.__silhouette_bulbizarre_rect)
        self.__fenetre.blit(self.__silhouette_evoli, self.__silhouette_evoli_rect)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.__silhouette_rect.collidepoint(event.pos):
                            return "pikachu"
                        elif self.__silhouette_carapuce_rect.collidepoint(event.pos):
                            return "carapuce"
                        elif self.__silhouette_salameche_rect.collidepoint(event.pos):
                            return "salameche"
                        elif self.__silhouette_bulbizarre_rect.collidepoint(event.pos):
                            return "bulbizarre"
                        
    # méthode afficher
    def afficher_menu(self):
        self.__fenetre.blit(self.__bg, (0, 0))
        self.__fenetre.blit(self.__silhouette, self.__silhouette_rect)
        self.__fenetre.blit(self.__silhouette_carapuce, self.__silhouette_carapuce_rect)
        self.__fenetre.blit(self.__silhouette_salameche, self.__silhouette_salameche_rect)
        self.__fenetre.blit(self.__silhouette_bulbizarre, self.__silhouette_bulbizarre_rect)
        pygame.display.flip()

test = Ajouter_pokemon()
test.afficher_menu()
print(test.choisir_silhouette())

    
