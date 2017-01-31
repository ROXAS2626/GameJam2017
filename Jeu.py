# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents

#importation de pygame
import pygame, Classes, random
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

points = 0
multiplicateur = 1

# Création du texte du score
font = pygame.font.Font(None, 24)
points_text = font.render("Points : " + str(points), 1, (255,255,255))
multiplicateur_text = font.render("Multiplicateur : " + str(multiplicateur), 1, (255,255,255))

# Création perso
zizou_normal = pygame.image.load("Images/Zizou_transparent.png").convert_alpha()
zizou_qui_casse = pygame.image.load("Images/zizou_casse_fail.png").convert_alpha()
zizou_qui_casse_vraiment = pygame.image.load("Images/zizou_casse_pasteque.png").convert_alpha()
zizou_qui_casse_pourris = pygame.image.load("Images/zizou_casse_pasteque_pourrie.png").convert_alpha()

def getObjet():
    # Charge l'image des pastèques et définit leur vitesse
    speed = [5, 0]
    pasteque = Classes.Pasteque(0, 305, "Images/pasteque200.png", 100, 100, speed, 100, 5, 0)
    bombe = Classes.Bombe(0, 305, "Images/bombe150.png", 100, 100, speed, 0)
    pastequeDoree = Classes.PastequeDoree(0, 305, "Images/Pasteque_Doréé.png", 100, 100, speed, 100, 5, 0, 2)
    pastequePourrie = Classes.PastequePourrie(0, 305, "Images/Pasteque_Pourris.png", 100, 100, speed, 100, 5, 0)
    listeObjets = [pasteque, bombe, pastequeDoree, pastequePourrie]
    numObjet = random.randint(0,3)
    return listeObjets[numObjet]


# boucle infinie pour affichage permanent de la fenêtre
while 1:
    #boucle sur les différents évènement reçut
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                fenetre.blit(zizou_qui_casse, (0,0))
                pygame.display.flip()
            if event.key == K_UP:
                pasteque.etat = True
                print pasteque.estCassee()
                points = points + 100
                print points
                pygame.display.flip()


    monObjet = getObjet()

    # Deplacement de la pasteque
    monObjet.movement()

    # On affiche les différentes images
    fenetre.blit(fond_e, (0,0))
    fenetre.blit(zizou_normal, (230,130))
    fenetre.blit(monObjet.get_img(), monObjet.get_rect())

    fenetre.blit(points_text, (30,30))
    fenetre.blit(multiplicateur_text, (30,50))

    #On refresh l'affichage
    pygame.display.flip()


    # Limite le nombre d'image par secondes
    pygame.time.wait(10)
