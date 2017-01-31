# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents

#importation de Pygame
import pygame
from pygame.locals import *


#importation de la bibliothèque system
import sys;
sys.path.insert(0, 'Buttons.py')

import Buttons

#importation du mixer pour gérer la musique
import pygame.mixer

#initialisation de Pygame

pygame.init()

# création de la fenêtre
fenetre  = pygame.display.set_mode((700,700), RESIZABLE)
pygame.display.set_caption('KoudBoul')

def menuMain(): #procedure qui affiche le menu

    # musique du menu
    pygame.mixer.music.load("Transforyou.mp3")
    pygame.mixer.music.play()

    #création fond d'écran menu
    fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()
    fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"
    pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements


    boutonJouer = Button()


def jeu(): #procedure qui affiche le jeu
    print "ICI LE JEU"

def Credit():
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
                            menuMain()

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


class Button:
    def __init__(self):
        self.main()

    #Create a display
    def display(self):
        self.screen = fenetre

    #Update the display and show the button
    def update_display(self):
        #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
        self.Button1.create_button(self.screen, (127,51,6), 100, 465, 500,    75,    0,        "Jouer", (255,255,255))
        pygame.display.flip()
        self.Button2.create_button(self.screen,(127,51,6),100,570,500,75,0,"Credit",(255,255,255))

    #Run the loop
    def main(self):
        self.Button1 = Buttons.Button()
        self.Button2 = Buttons.Button()
        self.display()
        while True:
            self.update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        import Jeu
                    if self.Button2.pressed(pygame.mouse.get_pos()):
                        Credit()





<<<<<<< HEAD
    # musique du menu
    pygame.mixer.music.load("Transforyou.mp3")
    pygame.mixer.music.play()

    #création fond d'écran menu
    fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()
    fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"

    logo = pygame.image.load("Images/logo.png")
    fenetre.blit(logo,(200,100))             #affiche l'image "logo" aux coordonnées "(0,0)" de la fenêtre "fenetre"

    pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements


    boutonJouer = Button()
=======
>>>>>>> ef364794f17bd11b1563a2c5163a1dacdb83e7bd



#boucle infinie pour affichage permanent de la fenêtre
while 1:
    #boucle sur les différents événements reçus
    for event in pygame.event.get():
        if event.type == QUIT:      #si l'utilisateur clique sur la croix
            sys.exit()          #on ferme la fenêtre

    menuMain()
