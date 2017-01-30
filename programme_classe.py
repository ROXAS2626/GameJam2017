# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents

#importation de pygame
import pygame
from pygame.locals import *

#importation des classes
import Classes

#importation de la bibliothèque system
import sys

#initialisation de pygame
pygame.init()

# création de la fenêtre
# Fenêtre de 700 pixels de largeur et de 530 pixels de hauteur
# Resizable permet à la fenêtre d'être redimensionnée durant l'exécution
fenetre = pygame.display.set_mode((700,530), RESIZABLE)

# Création fond d'écran
fond_e = pygame.image.load("image/floor.png").convert()

# Charge l'image de la pastèque et définit sa vitesse
pasteque = pygame.image.load("image/watermelon_400x400.png").convert_alpha()
speed = [1, 0]

# Charge le rectangle de la pasteque
pasteque_rect = pasteque.get_rect()

# boucle infinie pour affichage permanent de la fenêtre
while 1:
    #boucle sur les différents évènement reçut
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    # Deplacement de la pasteque
    pasteque_rect = pasteque_rect.move(speed)

    #On teste si le slim à atteint l'un des bords de l'écran
    if pasteque_rect.left < 0 or pasteque_rect.right > 700:
        speed[0] = -speed[0]
    if pasteque_rect.top < 0 or pasteque_rect.bottom > 530:
        speed[1] = -speed[1]

    # On affiche les différentes images
    fenetre.blit(fond_e, (0,0))
    fenetre.blit(pasteque, pasteque_rect)

    #On refresh l'affichage
    pygame.display.flip()

    # Limite le nombre d'image par secondes
    pygame.time.wait(10)
