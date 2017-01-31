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
    # musique du menu
    pygame.mixer.music.load("Transforyou.mp3")
    pygame.mixer.music.play()

    #création fond d'écran menu
    fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()
    fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"

    logo = pygame.image.load("Images/logo.png")
    fenetre.blit(logo,(200,45))             #affiche l'image "logo" aux coordonnées "(0,0)" de la fenêtre "fenetre"

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
            self.Button1.create_button(self.screen, (127,51,6), 100, 550, 500,    75,    0,        "Retour", (255,255,255))
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
        titre_credits = pygame.image.load("Images/credits_351_100.png")
        fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"
        fenetre.blit(titre_credits,(200,50))    #affiche l'image "titre_credits" aux coordonnées "(200,50)" de la fenêtre "fenetre"
        pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements
        Nom = font.render("Babouch : Notre roi",1,(255,255,255))
        Nom2 = font.render("Riki : Notre Guide",1,(255,255,255))
        Nom3 = font.render("Gaillard : Notre Sauveur",1,(255,255,255))
        Nom4 = font.render("Camarade : Notre Force",1,(255,255,255))
        Nom5 = font.render("Phantom : Notre Fierte",1,(255,255,255))
        fenetre.blit(Nom,(200,100))
        fenetre.blit(Nom2,(200,150))
        fenetre.blit(Nom3,(200,200))
        fenetre.blit(Nom4,(200,250))
        fenetre.blit(Nom5,(200,300))


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
        menu()

def Tutoriel():
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
            self.Button1.create_button(self.screen, (127,51,6), 100, 550, 500,    75,    0,        "Retour", (255,255,255))
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
        titre_tutos = pygame.image.load("Images/Tuto.png")
        fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"
        fenetre.blit(titre_tutos,(200,50))    #affiche l'image "titre_tutos" aux coordonnées "(200,50)" de la fenêtre "fenetre"
        pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements
        Nom = font.render("But du jeu :",1,(255,255,255))
        Nom2 = font.render("Realisez le plus vite possible",1,(255,255,255))
        Nom20 = font.render("les combinaisons de touches pour",1,(255,255,255))
        Nom21 = font.render("casser le maximum de pasteques !",1,(255,255,255))

        Nom22 = font.render("Nombres de points :",1,(255,255,255))
        Nom3 = font.render("Pasteques normales : 100 points",1,(255,255,255))
        Nom31 = font.render("Pasteques pourries : 200 points",1,(255,255,255))
        Nom32 = font.render("Pasteques dorees : 500 points",1,(255,255,255))

        Nom4 = font.render("Appuyer sur la touche espace pour eviter les bombes qui vont font perdre directement.",1,(255,255,255))
        Nom5 = font.render("A chaque pasteque cassee, vous gagnez 1s et a chaque erreur vous perdez 5s.",1,(255,255,255))

        fenetre.blit(Nom,(290,150))
        fenetre.blit(Nom2,(210,185))
        fenetre.blit(Nom20,(210,210))
        fenetre.blit(Nom21,(210,235))

        fenetre.blit(Nom22,(265,305))
        fenetre.blit(Nom3,(210,340))
        fenetre.blit(Nom31,(210,365))
        fenetre.blit(Nom32,(210,390))

        fenetre.blit(Nom4,(25,460))
        fenetre.blit(Nom5,(25,500))


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
        self.Button1.create_button(self.screen, (127,51,6), 100, 360, 500,    75,    0,        "Jouer", (255,255,255))
        self.Button3.create_button(self.screen, (127,51,6), 100, 465, 500,    75,    0,        "Tutoriel", (255,255,255))
        pygame.display.flip()
        self.Button2.create_button(self.screen,(127,51,6),100,570,500,75,0,"Credit",(255,255,255))

    #Run the loop
    def main(self):
        self.Button1 = Buttons.Button()
        self.Button3 = Buttons.Button()
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
                    if self.Button3.pressed(pygame.mouse.get_pos()):
                        Tutoriel()
                    if self.Button2.pressed(pygame.mouse.get_pos()):
                        Credit()








#boucle infinie pour affichage permanent de la fenêtre
while 1:
    #boucle sur les différents événements reçus
    for event in pygame.event.get():
        if event.type == QUIT:      #si l'utilisateur clique sur la croix
            sys.exit()          #on ferme la fenêtre

    menuMain()
