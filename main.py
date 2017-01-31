# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents

#importation de Pygame
import pygame, Classes, random
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


def Jeu():
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
        pasteque1 = Classes.Pasteque(0, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        pasteque2 = Classes.Pasteque(0, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        pasteque3 = Classes.Pasteque(0, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        pasteque4 = Classes.Pasteque(0, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        pasteque5 = Classes.Pasteque(0, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        pasteque6 = Classes.Pasteque(0, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        pasteque7 = Classes.Pasteque(0, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        pasteque8 = Classes.Pasteque(0, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        bombe1 = Classes.Bombe(0, 305, "Images/bombe.png", 100, 100, speed, 0)
        bombe2 = Classes.Bombe(0, 305, "Images/bombe.png", 100, 100, speed, 0)
        pastequeDoree = Classes.PastequeDoree(0, 305, "Images/Pasteque_Doréé.png", 100, 100, speed, 100, 5, 0, 2)
        pastequePourrie1 = Classes.PastequePourrie(0, 305, "Images/Pasteque_Pourris.png", 100, 100, speed, 100, 5, 0)
        pastequePourrie2 = Classes.PastequePourrie(0, 305, "Images/Pasteque_Pourris.png", 100, 100, speed, 100, 5, 0)
        listeObjets = [pasteque1, pasteque2, pasteque3, pasteque4, pasteque5, pasteque6, pasteque7, pasteque8, bombe1, bombe2, pastequeDoree, pastequePourrie1, pastequePourrie2]
        numObjet = random.randint(0,12)
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
                        if multiplicateur < 4:
                            multiplicateur = multiplicateur * 2
                        time += 5
                        pygame.display.flip()
                    elif isinstance(monObjet, Classes.Pasteque):        # Si l'objet est une Pasteque
                        points += 100 * multiplicateur
                        time += 2
                        pygame.display.flip()
                    elif isinstance(monObjet, Classes.Bombe) or time ==0:           # Si l'objet est une Bombe
                        #import GameOver
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

def menuMain(): #procedure qui affiche le menu

    # musique du menu
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
                        Jeu()
                    if self.Button2.pressed(pygame.mouse.get_pos()):
                        Credit()








#boucle infinie pour affichage permanent de la fenêtre
while 1:
    #boucle sur les différents événements reçus
    for event in pygame.event.get():
        if event.type == QUIT:      #si l'utilisateur clique sur la croix
            sys.exit()          #on ferme la fenêtre

    menuMain()
