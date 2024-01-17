import pygame
from pygame.locals import *
import sys
from Ajouter_pokemon import *


def lancer_jeu():
    pygame.init()

    menu = Menu_principal()
    ajouter = Ajouter_pokemon()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menu.lancer_jeu_rect.collidepoint(event.pos): 
                        print("lancer le jeu")
                        menu.son_bouton.play()
                        # Ajoutez le code pour lancer le jeu ici
                    elif menu.ajouter_pokemon_rect.collidepoint(event.pos):
                        print("ajouter un pokemon")
                        menu.son_bouton.play()
                        ajouter.lancer()
                        
                    elif menu.pokedex_rect.collidepoint(event.pos):
                        print("pokedex")
                        menu.son_bouton.play()

        menu.afficher_menu()
        pygame.display.flip()
if __name__ == "__main__":
    lancer_jeu()
