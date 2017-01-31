# -*- coding:Utf-8 -*-
# Ligne permettant l'utilisation des accents

# Importation de pygame
import pygame
from pygame.locals import *

# Importation de la bibliothèque system
import sys
sys.path.insert(0, 'Buttons.py')
# Initialisation de pygame
pygame.init()

import Buttons

# Création de la fenêtre
# Fenêtre de 900 pixels de largeur et de 899 pixels de hauteur
# Resizable permet à la fenêtre d'être redimensionnée durant l'exécution
fenetre = pygame.display.set_mode((700,700), RESIZABLE)

# Création fond d'écran
fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()


# Création du texte du score
fenetre.blit(fond_e,(0,0))
font = pygame.font.Font(None, 24)

pygame.display.flip()

class Button:
    def __init__(self):
        self.main()

    #Create a display
    def display(self):
        self.screen = fenetre

    #Update the display and show the button
    def update_display(self):
        #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
        self.Button1.create_button(self.screen, (127,51,6), 50, 600, 250,    75,    0,        "Retour", (255,255,255))
        pygame.display.flip()


    #Run the loop
    def main(self):
        self.Button1 = Buttons.Button()
        self.display()
        while True:
            self.update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        import main

def menu(): #procedure qui affiche le menu

    # musique du menu
    pygame.mixer.music.load("Transforyou.mp3")
    pygame.mixer.music.play()

    #création fond d'écran menu
    fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()
    fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"
    pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements


    boutonJouer = Button()

while 1:
    # Boucle sur les différents évènement reçut
    for event in pygame.event.get():    # Ferme la fenetre si appuie sur la croix rouge
        if event.type == QUIT:
            sys.exit()
    fenetre.blit(fond_e, (0,0))


    #On refresh l'affichage
    pygame.display.flip()


    # Limite le nombre d'image par secondes
    pygame.time.wait(10)
    menu()
