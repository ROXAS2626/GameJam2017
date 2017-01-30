# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents

#importation de pygame
import pygame
from pygame.locals import *

#Classe générique des sprites
class MySprite():
    # Constructeur
    def __init__(self, pos_x, pos_y, image, largeur, hauteur, speed):

        # Initialisation et affectation de l'attribut image
        self.image = pygame.load(image).convert_alpha()

        #Initialisation et affection de l'attribut rect
        self.rect = pygame.Rect(pos_x, pos_y, largeur, hauteur)

        #Initialisation et affection de l'attribut speed
        self.speed = speed

    # Retourne le rectangle (position)
    def get_rect(self):
        return self.rect

    # Retourne la surface
    def get_img(self):
        return self.image

    # Retourne la vitesse
    def get_speed(self):
        return self.speed
# Classe Bombe hérite de 'MySprite'
class Bombe(MySprite):
    def __init__(self, pos_x, pos_y, image1, largeur, hauteur, speed, etat):
        # appel du constructeur de la classe mere
        MySprite.__init__(self, pos_x, pos_y, image1, largeur, hauteur, speed)

        # Initialisation et affectation de l'attribut etat
        self.etat = 0

    # Retourne l'etat de la bombe (Entière= 0, Explosé= 1)
    def get_etat(self):
        return self.etat

# Classe Pasteque hérite de 'MySprite'
class Pasteque(MySprite):
    def __init__(self, pos_x, pos_y, image1, largeur, hauteur, speed, points, temps, etat):
        # appel du constructeur de la classe mere
        MySprite.__init__(self, pos_x, pos_y, image1, largeur, hauteur, speed)

        # Initialisation et affectation de l'attribut points
        self.points = 100

        # Initialisation et affectation de l'attribut temps
        self.temps = 5

        # Initialisation et affectation de l'attribut etat
        self.etat = 0

    # Retourne les points
    def get_pts(self):
        return self.points

    # Retourne le temps
    def get_tps(self):
        return self.temps

    # Retourne l'etat de la pasteque (Entière= 0, Cassée= 1)
    def get_etat(self):
        return self.etat

    def set_etat(self, etat):
        self.__etat = etat

# Classe PastequeDoree hérite de 'Pasteque'
class PastequeDoree(Pasteque):
    def __init__(self, pos_x, pos_y, image1, largeur, hauteur, speed, points, temps, etat, multiplicateur):
        # appel du constructeur de la classe mere
        Pasteque.__init__(self, pos_x, pos_y, image1, largeur, hauteur, speed, points, temps, etat)

        # Initialisation et affectation de l'attribut multiplicateur
        self.multiplicateur = 2

    # Retourne le multiplicateur
    def get_mult(self):
        return self.multiplicateur

#class PastequePourrie hérite de 'Pasteque'
class PastequePourrie(Pasteque):
    def __init__(self, pos_x, pos_y, image1, largeur, hauteur, speed, points, temps, etat):
        # appel du constructeur de la classe mere
        Pasteque.__init__(self, pos_x, pos_y, image1, largeur, hauteur, speed, points, temps, etat)

        # Initialisation et affectation de l'attribut points
        self.points = 50

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
