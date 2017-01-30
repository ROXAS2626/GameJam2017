# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents

#importation de pygame
import pygame, Classes
from pygame.locals import *

#importation de la bibliothèque system
import sys

#initialisation de pygame
pygame.init()

# création de la fenêtre
# Fenêtre de 700 pixels de largeur et de 530 pixels de hauteur
# Resizable permet à la fenêtre d'être redimensionnée durant l'exécution
fenetre = pygame.display.set_mode((700,530), RESIZABLE)

# Création fond d'écran
#fond_e = pygame.image.load("Image/floor.png").convert()

# Charge l'image de la pastèque et définit sa vitesse
speed = [1, 0]
pasteque = Classes.Pasteque(50, 50, "Images/Pasteque.png", 100, 100, speed, 100, 5, 0)

# boucle infinie pour affichage permanent de la fenêtre
while 1:
    #boucle sur les différents évènement reçut
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    # Deplacement de la pasteque
    pasteque.movement()

    # On affiche les différentes images
    #fenetre.blit(fond_e, (0,0))
    fenetre.blit(pasteque.get_img(), pasteque.get_rect())

    #On refresh l'affichage
    pygame.display.flip()

    # Limite le nombre d'image par secondes
    pygame.time.wait(10)
