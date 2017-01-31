# -*- coding:Utf-8 -*-
# Ligne permettant l'utilisation des accents

# Importation de pygame
import pygame, Classes, random
from pygame.locals import *

# Importation de la bibliothèque system
import sys

# Initialisation de pygame
pygame.init()

# Création de la fenêtre
# Fenêtre de 900 pixels de largeur et de 899 pixels de hauteur
# Resizable permet à la fenêtre d'être redimensionnée durant l'exécution
fenetre = pygame.display.set_mode((700,700), RESIZABLE)

# Création fond d'écran
fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()

# Création du timer
time = 100
pygame.time.set_timer(USEREVENT+1, 1000) # 1 seconde c'est 1000 millisecondes

# Création des variables des Scores
points = 0
multiplicateur = 1

# Création du texte du score
font = pygame.font.Font(None, 24)

# Création perso
zizou_normal = pygame.image.load("Images/Zizou_transparent.png").convert_alpha()
zizou_qui_casse = pygame.image.load("Images/zizou_casse_fail.png").convert_alpha()
zizou_qui_casse_vraiment = pygame.image.load("Images/zizou_casse_pasteque.png").convert_alpha()
zizou_qui_casse_pourris = pygame.image.load("Images/zizou_casse_pasteque_pourrie.png").convert_alpha()

def getObjet():
    # Charge l'image des pastèques et définit leur vitesse
    speed = [5, 0]
    pasteque = Classes.Pasteque(0, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
    bombe = Classes.Bombe(0, 305, "Images/bombe.png", 100, 100, speed, 0)
    pastequeDoree = Classes.PastequeDoree(0, 305, "Images/Pasteque_Doréé.png", 100, 100, speed, 100, 5, 0, 2)
    pastequePourrie = Classes.PastequePourrie(0, 305, "Images/Pasteque_Pourris.png", 100, 100, speed, 100, 5, 0)
    listeObjets = [pasteque, bombe, pastequeDoree, pastequePourrie]
    numObjet = random.randint(0,3)
    return listeObjets[numObjet]


# Boucle infinie pour affichage permanent de la fenêtre
while 1:
    # Boucle sur les différents évènement reçut
    for event in pygame.event.get():
        if event.type == USEREVENT+1:
            time -=1
        if event.type == QUIT:          # Ferme la fenetre si appuie sur la croix rouge
            sys.exit()
        if event.type == KEYDOWN:       # Evenement sur le clavier
            if event.key == K_SPACE:    # Si appuie sur espace, on change l'image de zizou
                fenetre.blit(zizou_qui_casse, (0,0))
                pygame.display.flip()
            if event.key == K_UP:       # Si appuie sur la fleche du haut
                if isinstance(monObjet, Classes.PastequeDoree):     # Si l'objet est une Pasteque Doree
                    points += 300
                    print points
                    pygame.display.flip()
                elif isinstance(monObjet, Classes.Pasteque):        # Si l'objet est une Pasteque
                    points += 100
                    print points
                    pygame.display.flip()
                elif isinstance(monObjet, Classes.Bombe):           # Si l'objet est une Bombe
                    points = 0
                    pygame.display.flip()

    # Création d'une instance d'un objet (Pasteque, PastequeDoree, PastequePourrie ou Bombe)
    monObjet = getObjet()

    # Deplacement de la pasteque
    monObjet.movement()

    # On affiche les différentes images
    fenetre.blit(fond_e, (0,0))
    fenetre.blit(zizou_normal, (230,130))
    fenetre.blit(monObjet.get_img(), monObjet.get_rect())
    # On affiche le temps restant
    timer_text = font.render("Temps : {0}".format(time), 1, (255,255,255))
    fenetre.blit(timer_text, (500, 30))
    # On affiche les scores
    points_text = font.render("Points : {0}".format(points), 1, (255,255,255))
    multiplicateur_text = font.render("Multiplicateur : {0}".format(multiplicateur), 1, (255,255,255))
    fenetre.blit(points_text, (30,30))
    fenetre.blit(multiplicateur_text, (30,50))

    #On refresh l'affichage
    pygame.display.flip()


    # Limite le nombre d'image par secondes
    pygame.time.wait(10)
