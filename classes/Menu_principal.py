# importation des bibliothèques
import pygame
from pygame.locals import *
import sys

# classe Menu_principal
class Menu_principal:
    # constructeur de la classe
    def __init__(self):
        pygame.init()
        # Créer la fenêtre
        self.__fenetre = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Menu Principal")
        self.__bg = pygame.image.load("images/background/bg_menu_principal.png").convert()

        # cree titre du jeu
        self.__titre_principal = pygame.image.load("titre/Pokemon_titre.png").convert_alpha()
        self.__titre_principal_rect = self.__titre_principal.get_rect()
        self.__titre_principal_rect.x = 150
        self.__titre_principal_rect.y = -150

        # titre secondaire
        self.__titre_secondaire = pygame.image.load("titre/Arena1.png").convert_alpha()
        self.__titre_secondaire_rect = self.__titre_secondaire.get_rect()
        self.__titre_secondaire_rect.x = 243
        self.__titre_secondaire_rect.y = 165

        # Charger la police
        self.police = pygame.font.Font("police/pokemon Solid.ttf", 25)

        # Faire boutons
        self.bouton_lancer_jeu = self.police.render("Lancer la partie", True, (0, 0, 0))
        self.bouton_lancer_jeu_rect = self.bouton_lancer_jeu.get_rect() 
        self.bouton_lancer_jeu_rect.x = 300
        self.bouton_lancer_jeu_rect.y = 250

        self.bouton_ajouter_pokemon = self.police.render("Ajouter Pokémon", True, (0, 0, 0))
        self.bouton_ajouter_pokemon_rect = self.bouton_ajouter_pokemon.get_rect()
        self.bouton_ajouter_pokemon_rect.x = 300
        self.bouton_ajouter_pokemon_rect.y = 300

        self.bouton_acces_pokedex = self.police.render("Accès Pokédex", True, (0, 0, 0))
        self.bouton_acces_pokedex_rect = self.bouton_acces_pokedex.get_rect()
        self.bouton_acces_pokedex_rect.x = 300
        self.bouton_acces_pokedex_rect.y = 350

        self.bouton_quitter = self.police.render("Quitter", True, (0, 0, 0))
        self.bouton_quitter_rect = self.bouton_quitter.get_rect()
        self.bouton_quitter_rect.x = 300
        self.bouton_quitter_rect.y = 400

    # Méthode pour afficher le menu principal
    def afficher_menu_principal(self):
        self.__fenetre.blit(self.__bg, (0, 0))
        self.__fenetre.blit(self.__titre_principal, self.__titre_principal_rect)
        self.__fenetre.blit(self.__titre_secondaire, self.__titre_secondaire_rect)
        self.__fenetre.blit(self.bouton_lancer_jeu, self.bouton_lancer_jeu_rect)
        self.__fenetre.blit(self.bouton_ajouter_pokemon, self.bouton_ajouter_pokemon_rect)
        self.__fenetre.blit(self.bouton_acces_pokedex, self.bouton_acces_pokedex_rect)
        self.__fenetre.blit(self.bouton_quitter, self.bouton_quitter_rect)

        # dessiner les contours des boutons
        pygame.draw.rect(self.__fenetre, (0, 0, 0), self.bouton_lancer_jeu_rect, 3)
        pygame.draw.rect(self.__fenetre, (0, 0, 0), self.bouton_ajouter_pokemon_rect, 3)
        pygame.draw.rect(self.__fenetre, (0, 0, 0), self.bouton_acces_pokedex_rect, 2)
        pygame.draw.rect(self.__fenetre, (0, 0, 0), self.bouton_quitter_rect, 2)


        pygame.display.flip()


# Créer une instance de la classe Menu_principal
menu_principal = Menu_principal()

# Afficher le menu principal
menu_principal.afficher_menu_principal()

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

    pygame.display.update()
