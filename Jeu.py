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
# Fenêtre de 900 pixels de largeur et de 899 pixels de hauteur
# Resizable permet à la fenêtre d'être redimensionnée durant l'exécution
fenetre = pygame.display.set_mode((700,700), RESIZABLE)

# Création fond d'écran
fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()

# Création d'un objet 'Score'
points = 0
multiplicateur = 1
score = Classes.Score(points, multiplicateur)

# Création du texte du score
font = pygame.font.Font(None, 24)

points_text = font.render("Points : " + str(score.get_pts()), 1, (255,255,255))
multiplicateur_text = font.render("Multiplicateur : " + str(score.get_mult()), 1, (255,255,255))

# Charge l'image de la pastèque et définit sa vitesse
speed = [5, 0]
pasteque = Classes.Pasteque(0, 305, "Images/pasteque200.png", 100, 100, speed, 100, 5, 0)

# boucle infinie pour affichage permanent de la fenêtre
while 1:
    #boucle sur les différents évènement reçut
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    # Deplacement de la pasteque
    pasteque.movement()

    # On affiche les différentes images
    fenetre.blit(fond_e, (0,0))
    fenetre.blit(pasteque.get_img(), pasteque.get_rect())
    fenetre.blit(points_text, (30,30))
    fenetre.blit(multiplicateur_text, (30,50))

    #On refresh l'affichage
    pygame.display.flip()

    # Limite le nombre d'image par secondes
    pygame.time.wait(10)
