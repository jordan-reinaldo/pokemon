import pygame
import pygame.time
from classes.Menu_principal import *




class Combat:
    XP_PAR_VICTOIRE = 20

    def __init__(self):
        self.running = True
        self.tour_mon_pokemon = True
        self.mon_pokemon = None
        self.adversaire = None
        self.derniere_attaque = 0  # Temps de la dernière attaque en millisecondes

    @staticmethod
    def calculer_degats(attaquant, attaque, defenseur):
        coefficient_eff = 1.0 
        if attaque.type.nom in defenseur.type.faiblesses:
            coefficient_eff = 2
        elif attaque.type.nom in defenseur.type.forces:
            coefficient_eff = 0.5
        elif attaque.type.nom in defenseur.type.nulle_defense:
            coefficient_eff = 0.0

        degats = int((((attaquant.lvl * 0.4 + 2) * attaquant.attaque * attaque.puissance / (defenseur.defense * 50)) + 2)) * coefficient_eff
        return degats

    @staticmethod
    def appliquer_degats(defenseur, degats):
        defenseur.pv -= int(degats)
        if defenseur.pv < 0:
            defenseur.pv = 0
        return defenseur.pv

    def dessiner_bouton(self, ecran, message, x, y, largeur, hauteur, couleur_inactive, couleur_active, border_radius=10):
        souris = pygame.mouse.get_pos()
        
        if x + largeur > souris[0] > x and y + hauteur > souris[1] > y:
            pygame.draw.rect(ecran, couleur_active, (x, y, largeur, hauteur), border_radius=border_radius)
        else:
            pygame.draw.rect(ecran, couleur_inactive, (x, y, largeur, hauteur), border_radius=border_radius)

            font = pygame.font.Font("police/Retro_Gaming.ttf", 15)
            text = font.render(message, True, (0, 0, 0))
            ecran.blit(text, (x + (largeur / 2 - text.get_width() / 2), y + (hauteur / 2 - text.get_height() / 2)))


    def afficher_message(self, ecran, message):
        font = pygame.font.Font("police/Retro_Gaming.ttf", 17)
    # Dessiner un rectangle de fond pour effacer le vieux message
        message_background = pygame.Rect(0, 550, 800, 50)  # Ajustez la taille au besoin
        pygame.draw.rect(ecran, (0, 0, 0), message_background)  
        texte = font.render(message, True, (255, 255, 255))
        ecran.blit(texte, (400 - texte.get_width() // 2, 550))
        pygame.display.flip()
        pygame.time.delay(1000)  # Délai pour que le message soit visible

    def effacer_message(self, ecran):
        message_background = pygame.Rect(0, 550, 800, 50)  # Ajustez la taille au besoin
        pygame.draw.rect(ecran, (0, 0, 0), message_background)  # Utilisez la couleur de l'arrière-plan
        pygame.display.flip()

    def lancer_combat(self, mon_pokemon, adversaire):
        self.mon_pokemon = mon_pokemon
        self.adversaire = adversaire
        if adversaire is None:
            print("erreur: adversaire est None")
            return
        self.running = True
        self.tour_mon_pokemon = True
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('musique/ostbattle.mp3')  
        pygame.mixer.music.play(-1) # -1 signifie que la musique va boucler
        ecran = pygame.display.set_mode((800, 600))
        sprite_mon_pokemon = pygame.image.load(f"images/pokemon_de_dos/{mon_pokemon.nom}1.png")
        sprite_adversaire = pygame.image.load(f"images/pokemon/{adversaire.nom}1.png")
        arriere_plan = pygame.image.load('images/background/bg_areneCombat.png') 
        font = pygame.font.Font("police/Retro_Gaming.ttf", 18)
        clock = pygame.time.Clock()
        taille_sprite_mon_pokemon = (190, 190)
        taille_sprite_adversaire = (160, 160)
        sprite_mon_pokemon = pygame.transform.scale(sprite_mon_pokemon, taille_sprite_mon_pokemon)
        sprite_adversaire = pygame.transform.scale(sprite_adversaire, taille_sprite_adversaire)

    # Définir les rectangles pour les boutons
        bouton_attaque_rect = pygame.Rect(50, 500, 100, 50)
        bouton_fuite_rect = pygame.Rect(650, 500, 100, 50)

        while self.running:
            self.effacer_message(ecran)
            ecran.blit(arriere_plan, (0, 0))  # Dessiner l'arrière-plan
            ecran.blit(sprite_mon_pokemon, (50, 280))
            ecran.blit(sprite_adversaire, (600, 100))
            self.dessiner_bouton(ecran, "Attaquer", 50, 500, 100, 50, (255, 0, 0), (255, 100, 100))
            self.dessiner_bouton(ecran, "Fuite", 650, 500, 100, 50, (255, 0, 0), (255, 100, 100))

            # Mettre à jour l'affichage des PV
            info_mon_pokemon = font.render(f"{self.mon_pokemon.nom} PV: {self.mon_pokemon.pv}", True, (0, 0, 0))
            info_adversaire = font.render(f"{self.adversaire.nom} PV: {self.adversaire.pv}", True, (0, 0, 0))
            cadre_texte = pygame.image.load("images/cadre_texte/cadre_texte_combat.png").convert_alpha()
            ecran.blit(cadre_texte, (30, 200))
            ecran.blit(cadre_texte, (500, 20))
            ecran.blit(info_mon_pokemon, (70, 215))
            ecran.blit(info_adversaire, (550, 40))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_attaque_rect.collidepoint(event.pos) and self.tour_mon_pokemon:
                        message = self.effectuer_attaque(self.mon_pokemon, self.adversaire)
                        self.afficher_message(ecran, message)
                        self.tour_mon_pokemon = False
                    elif bouton_fuite_rect.collidepoint(event.pos):
                        self.gerer_action_bouton_fuite(ecran)
                        menu = Menu_principal()
                        menu.afficher_menu()
                        if menu:
                            return "menu"
              # Redessiner les sprites et les informations à chaque itération
            


            pygame.display.flip()  # Met à jour l'écran
            if not self.tour_mon_pokemon:
                message = self.effectuer_attaque(self.adversaire, self.mon_pokemon)
                self.afficher_message(ecran, message)
                self.tour_mon_pokemon = True

          

            if self.mon_pokemon.pv <= 0 or self.adversaire.pv <= 0:
                self.running = False
                menu = Menu_principal()
                menu.afficher_menu()
                if menu:
                    pygame.mixer.music.stop() 
                    return "menu" 
        pygame.quit()

        if self.mon_pokemon.pv <= 0:
            return self.adversaire.nom
        else:
            return self.mon_pokemon.nom

    

    def gerer_action_bouton_attaque(self, ecran, attaquant, defenseur):
        message = self.effectuer_attaque(attaquant, defenseur)
        self.afficher_message(ecran, message)
        self.tour_mon_pokemon = False


    def gerer_action_bouton_fuite(self, ecran):
        print(f"{self.mon_pokemon.nom} a fui le combat.")
        pygame.mixer.music.stop() 
        self.running = False


    def gerer_attaque_adversaire(self, ecran):
        message = self.effectuer_attaque(self.adversaire, self.mon_pokemon)
        # Afficher le message sur l'écran
        self.tour_mon_pokemon = True

    def effectuer_attaque(self, attaquant, defenseur):
        degats = self.calculer_degats(attaquant, attaquant.attaque_de_base, defenseur)
        self.appliquer_degats(defenseur, degats)
        message = f"{attaquant.nom} attaque {attaquant.attaque_de_base.nom} et inflige {int(degats)} dégâts à {defenseur.nom}."
        return message