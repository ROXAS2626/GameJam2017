# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents

#importation de Pygame
import pygame, Classes, random
from pygame.locals import *


#importation de la bibliothèque system
import sys;
sys.path.insert(0, 'Buttons.py')

#import time pour gestion du temps
import time

import Buttons

#importation du mixer pour gérer la musique
import pygame.mixer

#initialisation de Pygame

pygame.init()

# création de la fenêtre
fenetre  = pygame.display.set_mode((700,700), RESIZABLE)
pygame.display.set_caption('KoudBoul')



def Jeu():
#################### VARIABLES GLOBALES ####################
    fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()     # Image de fond
    font = pygame.font.Font(None, 24)       # Création de la font

    # Création du timer
    time = 30
    pygame.time.set_timer(USEREVENT+1, 1000) # 1 seconde c'est 1000 millisecondes

    # Création des variables globales des Scores
    points = 0
    multiplicateur = 1
    combo = 0
    # variable globale fixe longueur combo
    longueur_combo = 3


    # Création perso
    zizou_normal = pygame.image.load("Images/Zizou_transparent.png").convert_alpha()
    zizou_qui_casse = pygame.image.load("Images/zizou_casse_fail.png").convert_alpha()
    zizou_qui_casse_vraiment = pygame.image.load("Images/zizou_casse_pasteque.png").convert_alpha()
    zizou_qui_casse_pourris = pygame.image.load("Images/zizou_casse_pasteque_pourrie.png").convert_alpha()

#################### METHODES ####################
    def getObjet():
        # Charge l'image des pastèques et définit leur vitesse
        x = -100
        speed = [15, 0]
        pasteque1 = Classes.Pasteque(x, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        pasteque2 = Classes.Pasteque(x, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        pasteque3 = Classes.Pasteque(x, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        pasteque4 = Classes.Pasteque(x, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        pasteque5 = Classes.Pasteque(x, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        pasteque6 = Classes.Pasteque(x, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        pasteque7 = Classes.Pasteque(x, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        pasteque8 = Classes.Pasteque(x, 305, "Images/pasteque.png", 100, 100, speed, 100, 5, 0)
        bombe1 = Classes.Bombe(x, 305, "Images/bombe.png", 100, 100, speed, 0)
        bombe2 = Classes.Bombe(x, 305, "Images/bombe.png", 100, 100, speed, 0)
        pastequePourrie1 = Classes.PastequePourrie(x, 305, "Images/Pasteque_Pourris.png", 100, 100, speed, 100, 5, 0)
        pastequePourrie2 = Classes.PastequePourrie(x, 305, "Images/Pasteque_Pourris.png", 100, 100, speed, 100, 5, 0)
        listeObjets = [pasteque1, pasteque2, pasteque3, pasteque4, pasteque5, pasteque6, pasteque7, pasteque8, bombe1, bombe2, pastequePourrie1, pastequePourrie2]
        numObjet = random.randint(0,11)
        return listeObjets[numObjet]


    def combo_random(longueur_combo): # choix au hasard de la combinaison
    	i = 0
    	liste_temp = []
    	liste_images = []

    	while i < longueur_combo:
    		liste_temp.append(random.randint(0, 3))
    		i = i + 1

    	v = 0
    	while v < len(liste_temp):
    		 if(liste_temp[v] == 0):
    			 liste_images.append("../GameJam2017/Images/fleche_gauche_noire.png")
    		 if(liste_temp[v] == 1):
    			 liste_images.append("../GameJam2017/Images/fleche_droite_noire.png")
    		 if(liste_temp[v] == 2):
    			 liste_images.append("../GameJam2017/Images/fleche_haut_noire.png")
    		 if(liste_temp[v] == 3):
    			 liste_images.append("../GameJam2017/Images/fleche_bas_noire.png")
    		 v = v + 1


    	return liste_images

    liste_fleches = combo_random(longueur_combo);

    numFlecheCour = 0
    monObjet = getObjet()
    # Boucle infinie pour affichage permanent de la fenêtre
    while 1:
        #accès a l'élément courant de la liste de fleches
        flecheCour = liste_fleches[numFlecheCour]

        # On affiche les différentes images
        fenetre.blit(fond_e, (0,0))
        fenetre.blit(zizou_normal, (230,130))
        monObjet.movement()
        fenetre.blit(monObjet.get_img(), monObjet.get_rect())
        # Boucle sur les différents évènement reçut
        for event in pygame.event.get():
            if event.type == USEREVENT+1:
                time -=1
            if event.type == QUIT:          # Ferme la fenetre si appuie sur la croix rouge
                sys.exit()
            if event.type == KEYDOWN:       # Evenement sur le clavier
                #if event.key == K_SPACE:    # Si appuie sur espace, on change l'image de zizou
                #    fenetre.blit(zizou_qui_casse, (0,0))
                #    pygame.display.flip()
                if isinstance(monObjet, Classes.Bombe):     # Si l'objet est une bombe
                    if event.key == K_SPACE:
                        monObjet = getObjet()
                        liste_fleches = combo_random(longueur_combo);
                        numFlecheCour = 0
                    else:
                        Game_Over()
                        pygame.display.flip()
                else:                                       # Sinon
                    #on test si le bouton correspond au bouton
                    if flecheCour=="../GameJam2017/Images/fleche_gauche_noire.png" and event.key == K_LEFT:
                        liste_fleches[numFlecheCour]="../GameJam2017/Images/fleche_gauche_verte.png"
                        numFlecheCour = numFlecheCour + 1
                    elif flecheCour=="../GameJam2017/Images/fleche_haut_noire.png" and event.key == K_UP:
                        liste_fleches[numFlecheCour]="../GameJam2017/Images/fleche_haut_verte.png"
                        numFlecheCour = numFlecheCour + 1
                    elif flecheCour=="../GameJam2017/Images/fleche_droite_noire.png" and event.key == K_RIGHT:
                        liste_fleches[numFlecheCour]="../GameJam2017/Images/fleche_droite_verte.png"
                        numFlecheCour = numFlecheCour + 1
                    elif flecheCour=="../GameJam2017/Images/fleche_bas_noire.png" and event.key == K_DOWN:
                        liste_fleches[numFlecheCour]="../GameJam2017/Images/fleche_bas_verte.png"
                        numFlecheCour = numFlecheCour + 1
                    #sinon c'est que la touche pressées ne correspond pas
                    else:
                        # Si le joueur se trompe de fleche alors il perd 5 secondes, perd son combo et la longueur redescend à 3
                        time -= 5
                        combo = 0
                        longueur_combo = 3
                        # Passage a l'objet suivant
                        monObjet = getObjet()
                        liste_fleches = combo_random(longueur_combo);
                        numFlecheCour = 0

                    # Si on arrive à la derniere flèche il faut passer à l'objet suivant
                    if numFlecheCour == longueur_combo:
                        # Le joueur à rentrer la bonne suite de fleche
                        # Il faut donc : changer l'image, ajouter les points, ajouter du temps, passer à un autre objet

                        # Deplacement de la pasteque
                        if isinstance(monObjet, Classes.PastequeDoree):     # Si l'objet est une Pasteque Doree
                            points += 400
                            if multiplicateur < 4:
                                multiplicateur = multiplicateur * 2
                            time += 5
                            pasteque_doree_defoncee = pygame.image.load("../GameJam2017/Images/pasteque_doree_defoncee.png").convert_alpha()
                            monObjet.image = pasteque_doree_defoncee
                            fenetre.blit(fond_e, (0,0))
                            fenetre.blit(zizou_qui_casse_vraiment, (170,76))
                            fenetre.blit(monObjet.get_img(), monObjet.get_rect())
                            pygame.display.flip()
                            pygame.time.delay(200)
                        elif isinstance(monObjet, Classes.Pasteque):        # Si l'objet est une Pasteque
                            points += 100 * multiplicateur
                            time += 1
                            pasteque_defoncee = pygame.image.load("../GameJam2017/Images/pasteque_defoncee.png").convert_alpha()
                            monObjet.image = pasteque_defoncee
                            fenetre.blit(fond_e, (0,0))
                            fenetre.blit(zizou_qui_casse_vraiment, (170,76))
                            fenetre.blit(monObjet.get_img(), monObjet.get_rect())
                            pygame.display.flip()
                            pygame.time.delay(200)

                        # Incrémentation du combo
                        combo += 1

                        # Création d'une nouvelle instance d'un objet (Pasteque, PastequeDoree, PastequePourrie ou Bombe)
                        if (combo % 10) == 0:       # Si le combo est un multiple de 10 alors le prochain objet sera une pastequeDoree
                            pastequeDoree = Classes.PastequeDoree(-100, 305, "Images/Pasteque_Doréé.png", 100, 100, [15,0], 100, 5, 0, 2)
                            monObjet = pastequeDoree
                        else:
                            if combo < 10:
                                longueur_combo = 3
                            elif combo > 10 and combo < 20:
                                longueur_combo = 4
                            else:
                                longueur_combo = 5
                            monObjet = getObjet()

                        # Change les fleches de façon aléatoire
                        liste_fleches = combo_random(longueur_combo);
                        numFlecheCour= 0

        # Si le temps est inférieur ou égal à 0 alors le joueur a perdu
        if time <= 0:
            Game_Over()
            pygame.display.flip()

        # On affiche le temps restant
        if time > 3:
            timer_text = font.render("Temps : {0}".format(time), 1, (255,255,255))
            fenetre.blit(timer_text, (500, 30))
        else:
            timer_text = font.render("Temps : {0}".format(time), 1, (240, 10, 10))
            fenetre.blit(timer_text, (500, 30))

        # On affiche les scores
        points_text = font.render("Points : {0}".format(points), 1, (255,255,255))
        multiplicateur_text = font.render("Multiplicateur : {0}".format(multiplicateur), 1, (255,255,255))
        combo_text = font.render("Combo : {0}".format(combo), 1, (255,255,255))
        fenetre.blit(points_text, (30,30))
        fenetre.blit(multiplicateur_text, (30,50))
        fenetre.blit(combo_text, (30,70))

        # On affiche les différentes images

        i = 0
        posPrem = 0
        if longueur_combo == 3:
            posPrem = 175
        elif longueur_combo == 4:
            posPrem = 110
        else: posPrem = 50

        while i < longueur_combo:
            fle_n = pygame.image.load(liste_fleches[i])
            fenetre.blit(fle_n, (posPrem + (125*i),500))
            i = i+1




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
    fenetre.blit(logo,(200,45))             #affiche l'image "logo" aux coordonnées "(0,0)" de la fenêtre "fenetre"

    pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements


    boutonJouer = Button()
def leaderBoard():

    fenetre = pygame.display.set_mode((700,700), RESIZABLE)

    # Création fond d'écran
    fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()
    fenetre.blit(fond_e,(0,0))

    font = pygame.font.Font(None, 33)
    titre = font.render("Leader Board",1,(255,0,0))
    fenetre.blit(titre,(230,150))

    while 1:
        # Boucle sur les différents évènement reçut
        for event in pygame.event.get():    # Ferme la fenetre si appuie sur la croix rouge
            if event.type == QUIT:
                sys.exit()


        #On refresh l'affichage
        pygame.display.flip()

def Game_Over():
    fenetre = pygame.display.set_mode((700,700), RESIZABLE)

    # Création fond d'écran
    fond_e = pygame.image.load("Images/gameOver.png").convert()


    # Création du texte du score
    fenetre.blit(fond_e,(0,0))
    font = pygame.font.Font(None, 24)


    pygame.display.flip()

    time.sleep(2)
    leaderBoard()


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

        Nom = font.render("Bastien : Notre roi",1,(255,255,255))
        Nom2 = font.render("Nathan : Notre Guide",1,(255,255,255))
        Nom3 = font.render("Esteban : Notre Sauveur",1,(255,255,255))
        Nom4 = font.render("Lucas  : Notre Force",1,(255,255,255))
        Nom5 = font.render("Kirill : Notre Fierte",1,(255,255,255))

        PDR = font.render("Nous vous remercions d'avoir joue a notre jeu.",1,(255,255,255))
        PDR2 = font.render("Nous esperons que cela vous a procure un plaisir malsain de casser les pasteques.",1,(255,255,255))
        PDR3 = font.render("NB : Aucune pasteque n'a ete maltraitee pendant la creation du jeu.",1,(255,255,255))
        PDR4 = font.render("Nous ne sommes pas sponsorises par Zizou.",1,(255,255,255))
        PDR5 = font.render("Copyright @Les Jager-Masters.",1,(255,255,255))

        fenetre.blit(Nom,(250,175))
        fenetre.blit(Nom2,(250,200))
        fenetre.blit(Nom3,(250,225))
        fenetre.blit(Nom4,(250,250))
        fenetre.blit(Nom5,(250,275))

        fenetre.blit(PDR,(150,375))
        fenetre.blit(PDR2,(25,400))
        fenetre.blit(PDR3,(100,450))
        fenetre.blit(PDR4,(140,475))
        fenetre.blit(PDR5,(200,500))

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
                        Jeu()
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
