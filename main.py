# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents

#importation de Pygame
import pygame, Classes, random, time, eztext, string, operator
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

# musique du menu
# musique du menu
pygame.mixer.music.load("Musiques/mainMusic.mp3")
pygame.mixer.music.play()

pygame.mixer.init()
channel1 = pygame.mixer.Channel(0) # argument must be int
sounda= pygame.mixer.Sound("Musiques/mainplay.ogg")

# création de la fenêtre
fenetre  = pygame.display.set_mode((700,700), RESIZABLE)
pygame.display.set_caption('KoudBoul')
score = 0
nomDuJoueur = ""

#définition des polices
font = pygame.font.Font(None, 24)       # Création de la font
font1 = pygame.font.Font(None, 40)       # Création de la font
font2 = pygame.font.Font(None, 75)       # Création de la font2
font3 = pygame.font.Font(None, 125)       # Création de la font3

#################### DEBUT DU JEU ####################
def Jeu(score,nomDuJoueur):
#################### VARIABLES GLOBALES DU JEU ####################
    print nomDuJoueur
    fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()     # Image de fond

    # Création du timer
    temps = 30
    pygame.time.set_timer(USEREVENT+1, 1000) # 1 seconde c'est 1000 millisecondes

    # Création des variables globales des Scores
    multiplicateur = 1
    combo = 0
    score = 0
    # variable globale fixe longueur combo
    longueur_combo = 3

    pygame.mixer.music.load("Musiques/ScalesOfJustice.wav")
    pygame.mixer.music.play()

    time.sleep(2)


    # Création perso
    zizou_normal = pygame.image.load("Images/Zizou_transparent.png").convert_alpha()
    zizou_qui_casse = pygame.image.load("Images/zizou_casse_fail.png").convert_alpha()
    zizou_qui_casse_vraiment = pygame.image.load("Images/zizou_casse_pasteque.png").convert_alpha()
    zizou_qui_casse_pourris = pygame.image.load("Images/zizou_casse_pasteque_pourrie.png").convert_alpha()
    zizou_explose = pygame.image.load("Images/zizou_explose.png").convert_alpha()

    class Button:
        pygame.mixer.stop()

        def __init__(self):
            self.main()

        #Create a display
        def display(self):
            self.screen = fenetre

        #Update the display and show the button
        def update_display(self):
            #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
            self.Button1.create_button(self.screen, (127,51,6), 475, 625, 200,    50,    0,        "Quitter", (255,255,255))
            pygame.display.flip()

        def pressed(self):
            return self.Button1.pressed(pygame.mouse.get_pos())

        #Run the loop
        def main(self):
            self.Button1 = Buttons.Button()
            self.display()
            self.update_display()


#################### METHODES UTILES DU JEU ####################
    def getObjet():
        # Charge l'image des pastèques et définit leur vitesse
        # chareg de façon aléatoire avec plus de pastèque normales
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
    			 liste_images.append("Images/fleche_gauche_noire.png")
    		 if(liste_temp[v] == 1):
    			 liste_images.append("Images/fleche_droite_noire.png")
    		 if(liste_temp[v] == 2):
    			 liste_images.append("Images/fleche_haut_noire.png")
    		 if(liste_temp[v] == 3):
    			 liste_images.append("Images/fleche_bas_noire.png")
    		 v = v + 1
    	return liste_images

    soundTabFail = ["Musiques/rentrecheztamere.mp3" , "Musiques/ohleboulet.mp3", "Musiques/tulavaispasvuvenir.mp3"]
    soundTabFail2 = ["Musiques/coin.wav", "Musiques/buzzer.mp3"]
    soundTabPasteque = ["Musiques/FirePunchImpact.wav", "Musiques/FirePunchImpact.wav", "Musiques/FirePunchImpact.wav", "Musiques/FirePunchImpact.wav", "Musiques/FirePunchImpact.wav", "Musiques/FirePunchImpact.wav" ,"Musiques/ronaldo.mp3", "Musiques/FirePunchImpact.wav","Musiques/FirePunchImpact.wav","Musiques/FirePunchImpact.wav",]

#################### AFFICHAGE DE LA FENETRE DU JEU ####################
    liste_fleches = combo_random(longueur_combo);   # Création d'une liste de fleches aléatoires
    numFlecheCour = 0                               # La première fleche est la fleche 0
    monObjet = getObjet()                           # Création d'un objet

    boutonQuitter = Button()

    saveObjet = Classes.Pasteque(450, 305, "Images/pasteque.png", 100, 100, 5, 100, 5, 0);
    pygame.mixer.music.stop()
    channel1.play(sounda)

    # Boucle infinie pour affichage permanent de la fenêtre
    while 1:
        #accès a l'élément courant de la liste de fleches
        flecheCour = liste_fleches[numFlecheCour]


        # On affiche les différentes images
        fenetre.blit(fond_e, (0,0))
        fenetre.blit(zizou_normal, (230,130))

        multi_x1 = pygame.image.load("Images/x1.png")
        multi_x2 = pygame.image.load("Images/x2.png")
        multi_x4 = pygame.image.load("Images/x4.png")

        if multiplicateur == 1:
            fenetre.blit(multi_x1,(410,105))
        elif multiplicateur == 2:
            fenetre.blit(multi_x2,(410,105))
        elif multiplicateur == 4:
            fenetre.blit(multi_x4,(410,105))

        monObjet.movement()
        fenetre.blit(monObjet.get_img(), monObjet.get_rect())
        pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(250,100,7*30,10))
        load_bar = pygame.draw.rect(fenetre, (255,255,0), pygame.Rect(250+(7*(30-temps)),100,7*temps,10))
        # Boucle sur les différents évènement reçut
        for event in pygame.event.get():
            if event.type == USEREVENT+1:
                temps -=1
            if event.type == QUIT:          # Ferme la fenetre si appuie sur la croix rouge
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if boutonQuitter.pressed():
                    menuMain()
            if event.type == KEYDOWN:       # Evenement sur le clavier
                #if event.key == K_SPACE:    # Si appuie sur espace, on change l'image de zizou
                #    fenetre.blit(zizou_qui_casse, (0,0))
                #    pygame.display.flip()
                if isinstance(monObjet, Classes.Bombe):     # Si l'objet est une bombe
                    if event.key == K_SPACE:
                        saveObjet = monObjet;
                        pygame.mixer.music.load("Musiques/bombequipart.WAV")
                        pygame.mixer.music.play()
                        monObjet = getObjet()       # Passage à l'objet suivant
                        liste_fleches = combo_random(longueur_combo);       # Passage aux fleches suivantes
                        numFlecheCour = 0
                    else:
                        pygame.mixer.music.load("Musiques/Explosion1.wav")
                        pygame.mixer.music.play()
                        time.sleep(1.5)
                        numsound = random.randint(0,2)
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(soundTabFail[numsound])
                        pygame.mixer.music.play()
                        fenetre.blit(fond_e, (0,0))
                        fenetre.blit(zizou_explose, (170,76))
                        fenetre.blit(monObjet.get_img(), monObjet.get_rect())
                        affiche_score(nomDuJoueur)
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        Game_Over(score,nomDuJoueur)
                        pygame.display.flip()
                else:
                    #on test si le bouton correspond au bouton
                    if (flecheCour=="Images/fleche_gauche_noire.png" or flecheCour=="Images/fleche_droite_jaune.png") and event.key == K_LEFT:
                        liste_fleches[numFlecheCour]="Images/fleche_gauche_verte.png"
                        numFlecheCour = numFlecheCour + 1
                    elif (flecheCour=="Images/fleche_haut_noire.png" or flecheCour=="Images/fleche_bas_jaune.png") and event.key == K_UP:
                        liste_fleches[numFlecheCour]="Images/fleche_haut_verte.png"
                        numFlecheCour = numFlecheCour + 1
                    elif (flecheCour=="Images/fleche_droite_noire.png" or flecheCour=="Images/fleche_gauche_jaune.png") and event.key == K_RIGHT:
                        liste_fleches[numFlecheCour]="Images/fleche_droite_verte.png"
                        numFlecheCour = numFlecheCour + 1
                    elif (flecheCour=="Images/fleche_bas_noire.png" or flecheCour=="Images/fleche_haut_jaune.png") and event.key == K_DOWN:
                        liste_fleches[numFlecheCour]="Images/fleche_bas_verte.png"
                        numFlecheCour = numFlecheCour + 1
                    #sinon c'est que la touche pressées ne correspond pas
                    else:

                        numsound1 = random.randint(0,1)
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(soundTabFail2[numsound1])
                        pygame.mixer.music.play()


                        temps -= 5                   # Le joueur perd 5 secondes
                        multiplicateur = 1          # Le multiplicateur retombe à 1
                        combo = 0                   # Le joueur retombe à 0 de combo
                        fenetre.blit(fond_e, (0,0))
                        fenetre.blit(zizou_qui_casse, (143,50))

                        #Affichage du temps perdu
                        temps1 = font3.render("-5s",1,(240, 10, 10))
                        fenetre.blit(temps1, (450,75))

                        fenetre.blit(monObjet.get_img(), monObjet.get_rect())
                        affiche_score(nomDuJoueur)


                        #-----------fleche roucge debut
                        if flecheCour=="Images/fleche_gauche_noire.png" or flecheCour=="Images/fleche_gauche_jaune.png":
                            liste_fleches[numFlecheCour]="Images/fleche_gauche_rouge.png"
                        elif flecheCour=="Images/fleche_haut_noire.png" or flecheCour=="Images/fleche_haut_jaune.png":
                            liste_fleches[numFlecheCour]="Images/fleche_haut_rouge.png"
                        elif flecheCour=="Images/fleche_droite_noire.png" or flecheCour=="Images/fleche_droite_jaune.png":
                            liste_fleches[numFlecheCour]="Images/fleche_droite_rouge.png"
                        elif flecheCour=="Images/fleche_bas_noire.png" or flecheCour=="Images/fleche_bas_jaune.png":
                            liste_fleches[numFlecheCour]="Images/fleche_bas_rouge.png"

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

                        longueur_combo = 3          # Le nombre de fleche retombe à 3
                        #On refresh l'affichage
                        pygame.display.flip()


                        time.sleep(0.75)
                        #-----------fleche rouge fin

                        saveObjet = monObjet;
                        monObjet = getObjet()       # Passage a l'objet suivant
                        liste_fleches = combo_random(longueur_combo);       # Passage aux fleches suivantes
                        numFlecheCour = 0

                    # Si on arrive à la derniere flèche il faut passer à l'objet suivant
                    if numFlecheCour == longueur_combo:
                        # Le joueur à rentrer la bonne suite de fleche
                        # Il faut donc : changer l'image, ajouter les points, ajouter du temps, passer à un autre objet

                        # Deplacement de la pasteque
                        if isinstance(monObjet, Classes.PastequeDoree):     # Si l'objet est une Pasteque Doree
                            score += 200 * multiplicateur
                            if multiplicateur < 4:
                                multiplicateur = multiplicateur * 2
                            temps += 2

                            #afficher l'image du combo
                            combo_image = pygame.image.load("Images/combo.png")
                            #afficher les images des multiplicateurs
                            combo_x2 = pygame.image.load("Images/x2_explosion.png")
                            combo_x4 = pygame.image.load("Images/x4_explosion.png")

                            pygame.mixer.music.load("Musiques/combo.mp3")
                            pygame.mixer.music.play()

                            pasteque_doree_defoncee = pygame.image.load("Images/pasteque_doree_defoncee.png").convert_alpha()
                            pasteque = pygame.image.load("Images/pasteque.png")
                            pasteque_defoncer = pygame.image.load("Images/pasteque_defoncee.png")
                            monObjet.image = pasteque_doree_defoncee
                            fenetre.blit(fond_e, (0,0))
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(250,100,7*30,10))
                            load_bar = pygame.draw.rect(fenetre, (255,255,0), pygame.Rect(250+(7*(30-temps)),100,7*temps,10))
                            fenetre.blit(combo_image, (250,475))
                            fenetre.blit(zizou_qui_casse_vraiment, (170,76))
                            if multiplicateur == 2:

                                #Affichage des points
                                points1 = font3.render("+500",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(combo_x2, (410,105))
                            elif multiplicateur == 4:

                                #Affichage des points
                                points1 = font3.render("+1000",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(combo_x4, (410,105))
                            fenetre.blit(monObjet.get_img(), monObjet.get_rect())
                            affiche_score(nomDuJoueur)
                            pygame.display.flip()
                            time.sleep(.250)
                            monObjet.image = pasteque
                            fenetre.blit(fond_e, (0,0))
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(250,100,7*30,10))
                            load_bar = pygame.draw.rect(fenetre, (255,255,0), pygame.Rect(250+(7*(30-temps)),100,7*temps,10))
                            fenetre.blit(combo_image, (253,478))
                            fenetre.blit(zizou_normal, (230,130))
                            if multiplicateur == 2:

                                #Affichage des points
                                points1 = font3.render("+500",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(combo_x2, (407,108))
                            elif multiplicateur == 4:

                                #Affichage des points
                                points1 = font3.render("+1000",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(combo_x4, (407,108))
                            fenetre.blit(monObjet.get_img(), monObjet.get_rect())
                            affiche_score(nomDuJoueur)
                            pygame.display.flip()
                            time.sleep(.250)
                            monObjet.image = pasteque_defoncer
                            fenetre.blit(fond_e, (0,0))
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(250,100,7*30,10))
                            load_bar = pygame.draw.rect(fenetre, (255,255,0), pygame.Rect(250+(7*(30-temps)),100,7*temps,10))
                            fenetre.blit(combo_image, (250,475))
                            fenetre.blit(zizou_qui_casse_vraiment, (170,76))
                            pygame.mixer.music.load("Musiques/FirePunchImpact.wav")
                            pygame.mixer.music.play()
                            if multiplicateur == 2:

                                #Affichage des points
                                points1 = font3.render("+500",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(combo_x2, (410,105))
                            elif multiplicateur == 4:

                                #Affichage des points
                                points1 = font3.render("+1000",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(combo_x4, (410,105))
                            fenetre.blit(monObjet.get_img(), monObjet.get_rect())
                            temps += 1
                            score += 100
                            affiche_score(nomDuJoueur)
                            pygame.display.flip()
                            time.sleep(.250)
                            monObjet.image = pasteque
                            fenetre.blit(fond_e, (0,0))
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(250,100,7*30,10))
                            load_bar = pygame.draw.rect(fenetre, (255,255,0), pygame.Rect(250+(7*(30-temps)),100,7*temps,10))
                            fenetre.blit(combo_image, (253,478))
                            fenetre.blit(zizou_normal, (230,130))
                            if multiplicateur == 2:

                                #Affichage des points
                                points1 = font3.render("+500",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(combo_x2, (407,108))
                            elif multiplicateur == 4:

                                #Affichage des points
                                points1 = font3.render("+1000",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(combo_x4, (407,108))
                            fenetre.blit(monObjet.get_img(), monObjet.get_rect())
                            affiche_score(nomDuJoueur)
                            pygame.display.flip()
                            time.sleep(.250)
                            monObjet.image = pasteque_defoncer
                            fenetre.blit(fond_e, (0,0))
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(250,100,7*30,10))
                            load_bar = pygame.draw.rect(fenetre, (255,255,0), pygame.Rect(250+(7*(30-temps)),100,7*temps,10))
                            fenetre.blit(combo_image, (250,475))
                            fenetre.blit(zizou_qui_casse_vraiment, (170,76))
                            pygame.mixer.music.load("Musiques/FirePunchImpact.wav")
                            pygame.mixer.music.play()
                            if multiplicateur == 2:

                                #Affichage des points
                                points1 = font3.render("+500",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(combo_x2, (410,105))
                            elif multiplicateur == 4:

                                #Affichage des points
                                points1 = font3.render("+1000",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(combo_x4, (410,105))
                            fenetre.blit(monObjet.get_img(), monObjet.get_rect())
                            temps += 1
                            score += 100
                            affiche_score(nomDuJoueur)
                            pygame.display.flip()
                            time.sleep(.250)
                            monObjet.image = pasteque
                            fenetre.blit(fond_e, (0,0))
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(250,100,7*30,10))
                            load_bar = pygame.draw.rect(fenetre, (255,255,0), pygame.Rect(250+(7*(30-temps)),100,7*temps,10))
                            fenetre.blit(combo_image, (253,478))
                            fenetre.blit(zizou_normal, (230,130))
                            if multiplicateur == 2:

                                #Affichage des points
                                points1 = font3.render("+500",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(combo_x2, (407,108))
                            elif multiplicateur == 4:

                                #Affichage des points
                                points1 = font3.render("+1000",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(combo_x4, (407,108))
                            fenetre.blit(monObjet.get_img(), monObjet.get_rect())
                            affiche_score(nomDuJoueur)
                            pygame.display.flip()
                            time.sleep(.250)
                            monObjet.image = pasteque_defoncer
                            fenetre.blit(fond_e, (0,0))
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(250,100,7*30,10))
                            load_bar = pygame.draw.rect(fenetre, (255,255,0), pygame.Rect(250+(7*(30-temps)),100,7*temps,10))
                            fenetre.blit(combo_image, (250,475))
                            fenetre.blit(zizou_qui_casse_vraiment, (170,76))
                            pygame.mixer.music.load("Musiques/FirePunchImpact.wav")
                            pygame.mixer.music.play()
                            if multiplicateur == 2:

                                #Affichage des points
                                points1 = font3.render("+500",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(combo_x2, (410,105))
                            elif multiplicateur == 4:

                                #Affichage des points
                                points1 = font3.render("+1000",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(combo_x4, (410,105))
                            fenetre.blit(monObjet.get_img(), monObjet.get_rect())
                            temps += 1
                            score += 100
                            affiche_score(nomDuJoueur)
                            pygame.display.flip()
                            time.sleep(.250)
                            pygame.time.delay(200)

                        elif isinstance(monObjet, Classes.PastequePourrie):
                            pygame.mixer.music.load("Musiques/Splish.wav")
                            pygame.mixer.music.play()
                            score += 200 * multiplicateur
                            temps += 1
                            pasteque_pourrie_defoncee = pygame.image.load("Images/pasteque_pourrie_defoncee.png").convert_alpha()
                            monObjet.image = pasteque_pourrie_defoncee
                            fenetre.blit(fond_e, (0,0))
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(250,100,7*30,10))
                            load_bar = pygame.draw.rect(fenetre, (255,255,0), pygame.Rect(250+(7*(30-temps)),100,7*temps,10))
                            fenetre.blit(zizou_qui_casse_pourris, (170,76))
                            if multiplicateur == 1:

                                #Affichage des points
                                points1 = font2.render("+200",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(multi_x1,(410,105))
                            elif multiplicateur == 2:

                                #Affichage des points
                                points1 = font2.render("+400",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(multi_x2,(410,105))
                            elif multiplicateur == 4:

                                #Affichage des points
                                points1 = font2.render("+800",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(multi_x4,(410,105))
                            fenetre.blit(monObjet.get_img(), monObjet.get_rect())
                            affiche_score(nomDuJoueur)
                            pygame.display.flip()
                            pygame.time.delay(200)

                        elif isinstance(monObjet, Classes.Pasteque):        # Si l'objet est une Pasteque
                            numsound1 = random.randint(0,9)
                            pygame.mixer.music.load(soundTabPasteque[numsound1])
                            pygame.mixer.music.play()
                            score += 100 * multiplicateur
                            temps += 1
                            pasteque_defoncee = pygame.image.load("Images/pasteque_defoncee.png").convert_alpha()
                            monObjet.image = pasteque_defoncee
                            fenetre.blit(fond_e, (0,0))
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(250,100,7*30,10))
                            load_bar = pygame.draw.rect(fenetre, (255,255,0), pygame.Rect(250+(7*(30-temps)),100,7*temps,10))
                            fenetre.blit(zizou_qui_casse_vraiment, (170,76))
                            if multiplicateur == 1:

                                #Affichage des points
                                points1 = font2.render("+100",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(multi_x1,(410,105))
                            elif multiplicateur == 2:

                                #Affichage des points
                                points1 = font2.render("+200",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(multi_x2,(410,105))
                            elif multiplicateur == 4:

                                #Affichage des points
                                points1 = font2.render("+400",1,(255,255,255))
                                fenetre.blit(points1, (175,150))

                                fenetre.blit(multi_x4,(410,105))
                            fenetre.blit(monObjet.get_img(), monObjet.get_rect())

                            affiche_score(nomDuJoueur)
                            pygame.display.flip()
                            pygame.time.delay(200)
                            time.sleep(0.2)
                        # Incrémentation du combo
                        combo += 1

                        # Création d'une nouvelle instance d'un objet (Pasteque, PastequeDoree, PastequePourrie ou Bombe)
                        if (combo % 10) == 0:       # Si le combo est un multiple de 10 alors le prochain objet sera une pastequeDoree
                            pastequeDoree = Classes.PastequeDoree(-100, 305, "Images/Pasteque_Doréé.png", 100, 100, [15,0], 100, 5, 0, 2)
                            pygame.mixer.music.load("Musiques/pastequesdorees.mp3")
                            pygame.mixer.music.play()
                            saveObjet = monObjet;
                            monObjet = pastequeDoree
                        else:
                            if combo < 10:
                                longueur_combo = 3
                            elif combo > 10 and combo < 20:
                                longueur_combo = 4
                            else:
                                longueur_combo = 5
                            saveObjet = monObjet;
                            monObjet = getObjet()

                        # Change les fleches de façon aléatoire
                        liste_fleches = combo_random(longueur_combo);
                        numFlecheCour= 0

        def affiche_score(nomDuJoueur):
            # Si le temps est inférieur ou égal à 0 alors le joueur a perdu
            if temps <= 0:
                Game_Over(score,nomDuJoueur)
                pygame.display.flip()

            # On affiche le temps restant
            if temps > 3:
                timer_text = font.render("Temps : {0}".format(temps), 1, (255,255,255))
                fenetre.blit(timer_text, (315, 60))
            else:
                timer_text = font.render("Temps : {0}".format(temps), 1, (240, 10, 10))
                fenetre.blit(timer_text, (315, 60))

            # On affiche les scores
            points_text = font.render("Points : {0}".format(score), 1, (255,255,255))
            #multiplicateur_text = font.render("Multiplicateur : {0}".format(multiplicateur), 1, (255,255,255))
            combo_text = font.render("Combo : {0}".format(combo), 1, (255,255,255))
            fenetre.blit(points_text, (30,30))
            #fenetre.blit(multiplicateur_text, (30,50))
            fenetre.blit(combo_text, (30,70))

        affiche_score(nomDuJoueur)

        # On affiche les différentes images des flèches
        i = 0
        posPrem = 0
        if longueur_combo == 3:
            posPrem = 175
        elif longueur_combo == 4:
            posPrem = 110
        else: posPrem = 50

        while i < longueur_combo:
            #si c'est la derniere fleche de cette combinaison ET que l'ancien objet (saveObjet) est une pasteque pourrit alors on ecrit la fleche en jaune
            if i==(longueur_combo-1) and isinstance(saveObjet, Classes.PastequePourrie):
                if liste_fleches[i]=="Images/fleche_haut_noire.png":
                    liste_fleches[i]="Images/fleche_bas_jaune.png"
                elif liste_fleches[i]=="Images/fleche_bas_noire.png":
                    liste_fleches[i]="Images/fleche_haut_jaune.png"
                elif liste_fleches[i]=="Images/fleche_gauche_noire.png":
                    liste_fleches[i]="Images/fleche_droite_jaune.png"
                elif liste_fleches[i]=="Images/fleche_droite_noire.png":
                    liste_fleches[i]="Images/fleche_gauche_jaune.png"
            fle_n = pygame.image.load(liste_fleches[i])
            fenetre.blit(fle_n, (posPrem + (125*i),500))
            i = i+1

        boutonQuitter.update_display()

        #On refresh l'affichage
        pygame.display.flip()

        # Limite le nombre d'image par secondes
        pygame.time.wait(10)
#################### FIN DU JEU ####################

#################### MENU ####################
def menuMain(): #procedure qui affiche le menu



    #création fond d'écran menu
    fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()
    fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"

    logo = pygame.image.load("Images/logo.png")
    fenetre.blit(logo,(200,45))             #affiche l'image "logo" aux coordonnées "(0,0)" de la fenêtre "fenetre"

    pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements


    boutonJouer = Button()
#################### FIN DU MENU ####################

#################### TABLEAU DES SCORES ####################
def leaderBoard(score, nomDuJoueur):

    class Button:
        def __init__(self):
            self.main()

        #Create a display
        def display(self):
            self.screen = fenetre

        #Update the display and show the button
        def update_display(self):
            #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
            self.Button1.create_button(self.screen, (127,51,6), 50, 600, 250,    75,    0,        "Rejouer", (255,255,255))
            self.Button2.create_button(self.screen, (127,51,6), 400, 600, 250,    75,    0,        "Quitter", (255,255,255))
            pygame.display.flip()


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
                            Jeu(score, nomDuJoueur)
                        elif self.Button2.pressed(pygame.mouse.get_pos()):
                            menuMain()


    ##gestion de score grâce au fichier#######################
    #insertion de valeur dans le fichier########################""
    fichier = open("testfile.txt","a")

    fichier.write("%d|%s\n" % (score, nomDuJoueur))

    fichier.close()

#tri du fichier############
    #ouverture du fichier en mode lecture
    fichier = open("testfile.txt","r")

    #sauvegarde du contenu du fichier
    str_temp = fichier.read()

    #fermeture du fichier initial de score et ouverture en mode écriture
    fichier.close()

    #table intermédiaire supprimant \n
    temp_tab1 = str_temp.split('\n')

    #tableau contenant des tableaux de la forme [michel, 3200]
    temp_tab2=[]
    i=0
    while i <= (len(temp_tab1)-2):
        tab = temp_tab1[i].split('|')
        temp_tab2.append( (int(tab[0]), tab[1]) )
        i = i+1



    #tri des scores
    def getKey(item):
        return item[0]

    tabScoreTriee = sorted(temp_tab2, key = operator.itemgetter(0), reverse = True)


    #insertion score trié dans fichier
    fichier = open("testfile.txt","w")

    for k in range(0, len(tabScoreTriee)):
        fichier.write("%d|%s\n" % (int(tabScoreTriee[k][0]), tabScoreTriee[k][1]))

    fichier.close()
#fin tri fichier######################

    poscourante=-1
    for k in range(0, len(tabScoreTriee)):
        if tabScoreTriee[k][1]==nomDuJoueur and tabScoreTriee[k][0]==score:
            poscourante = k


    def parcoursAffiche(bornInf, bornSup, tab):
        tabRet = []
        for k in range(bornInf, bornSup):
            tabRet.append(tab[k])
        return tabRet


    #haut du tableau
    if poscourante < 5:
        tabAfficher = parcoursAffiche(0,11, tabScoreTriee)
    #bas du tableau
    elif poscourante > (len(tabScoreTriee)-5):
        tabAfficher = parcoursAffiche(len(tabScoreTriee)-11,len(tabScoreTriee), tabScoreTriee)
    #au milieu
    else:
        tabAfficher = parcoursAffiche(poscourante-6, poscourante+5, tabScoreTriee)


    fenetre = pygame.display.set_mode((700,700), RESIZABLE)

    # Création fond d'écran
    fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()
    fenetre.blit(fond_e,(0,0))


    pygame.draw.rect(fenetre, (127,51,6), pygame.Rect(175,50,350,500))

    font = pygame.font.Font(None, 50)
    titre = font.render("Leader Board",1,(255,255,255))

    fontRes = pygame.font.Font(None, 25)
    fontResJoueurCour = pygame.font.Font(None, 35)
    fenetre.blit(titre,(240,70))
    nbResultat = len(tabAfficher)


    i=0
    while i < nbResultat:
        if tabAfficher[i][1]==nomDuJoueur and tabAfficher[i][0]==score:
            name = fontResJoueurCour.render(tabAfficher[i][1],1,(240,10,10))
            scoreaf = fontResJoueurCour.render(str(tabAfficher[i][0]),1,(240,10,10))
        else:
            name = fontRes.render(tabAfficher[i][1],1,(255,255,255))
            scoreaf = fontRes.render(str(tabAfficher[i][0]),1,(255,255,255))
        fenetre.blit(name,(200,120+i*40))
        fenetre.blit(scoreaf,(380,120+i*40))
        i = i + 1





    boutonRejouer = Button()
    while 1:
        # Boucle sur les différents évènement reçut
        for event in pygame.event.get():    # Ferme la fenetre si appuie sur la croix rouge
            if event.type == QUIT:
                sys.exit()

        #On refresh l'affichage
        pygame.display.flip()

#################### FIN DU TABLEAU DES SCORES ####################

#################### AFFICHAGE GAME OVER ####################
def Game_Over(score,nomDuJoueur):
    fenetre = pygame.display.set_mode((700,700), RESIZABLE)

    # Création fond d'écran
    fond_e = pygame.image.load("Images/gameOver.png").convert()


    # Création du texte du score
    fenetre.blit(fond_e,(0,0))
    font = pygame.font.Font(None, 24)
    pygame.mixer.music.load("Musiques/gameover.mp3")
    pygame.mixer.music.play()

    font = pygame.font.Font(None, 35)
    points = font.render("Score : {0}".format(score) ,1,(0,0,0))
    fenetre.blit(points,(400,590))

    class Button:
        def __init__(self):
            self.main()

        #Create a display
        def display(self):
            self.screen = fenetre

        #Update the display and show the button
        def update_display(self):
            #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
            self.Button1.create_button(self.screen, (127,51,6), 400, 639, 250,    37,    0,        "Suivant", (255,255,255))
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
                            leaderBoard(score, nomDuJoueur)

    def menu(): #procedure qui affiche le menu


        #création fond d'écran menu
        fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()
        fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"
        pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements

        boutonJouer = Button()
    boutonSuivant = Button()

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

#################### FIN GAME OVER ####################

#################### AFFICHAGE CREDIT ####################
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
            self.Button1.create_button(self.screen, (127,51,6), 100, 570, 500,    75,    0,        "Retour", (255,255,255))
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



        #création fond d'écran menu
        fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()
        titre_credits = pygame.image.load("Images/credits_351_100.png")
        fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"
        fenetre.blit(titre_credits,(200,50))    #affiche l'image "titre_credits" aux coordonnées "(200,50)" de la fenêtre "fenetre"
        pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements

        Nom = font.render("Bastien : Notre Roi",1,(255,255,255))
        Nom2 = font.render("Nathan : Notre Guide",1,(255,255,255))
        Nom3 = font.render("Esteban : Notre Sauveur",1,(255,255,255))
        Nom4 = font.render("Lucas  : Notre Force",1,(255,255,255))
        Nom5 = font.render("Kirill : Notre Fierte",1,(255,255,255))

        PDR = font.render("Nous vous remercions d'avoir joue a notre jeu.",1,(255,255,255))
        PDR2 = font.render("Nous esperons que cela vous a procure un plaisir malsain de casser les pasteques.",1,(255,255,255))
        PDR3 = font.render("NB : Aucune pasteque n'a ete maltraitee pendant la creation du jeu.",1,(255,255,255))
        PDR4 = font.render("Nous ne sommes pas sponsorises par Zizou.",1,(255,255,255))
        PDR5 = font.render("Sources : Youtube, StackOverFlow, OpenClassroom, Pygame, Gimp",1,(255,255,255))

        fenetre.blit(Nom,(250,195))
        fenetre.blit(Nom2,(250,225))
        fenetre.blit(Nom3,(250,255))
        fenetre.blit(Nom4,(250,285))
        fenetre.blit(Nom5,(250,315))

        fenetre.blit(PDR,(150,375))
        fenetre.blit(PDR2,(25,400))
        fenetre.blit(PDR3,(100,460))
        fenetre.blit(PDR4,(136,485))
        fenetre.blit(PDR5,(90,530))

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

#################### AFFICHAGE DU TUTORIEL ####################
#################### PAGE 1 ####################
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
            self.Button1.create_button(self.screen, (127,51,6), 100, 570, 500,    75,    0,        "Retour", (255,255,255))
            self.Button2.create_button(self.screen, (127,51,6), 100, 465, 500,    75,    0,        "Suivant", (255,255,255))
            pygame.display.flip()


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
                            menuMain()
                        elif self.Button2.pressed(pygame.mouse.get_pos()):
                            Tutoriel2()

    def menu(): #procedure qui affiche le menu



        #création fond d'écran menu
        fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()
        titre_tutos = pygame.image.load("Images/Tuto.png")

        fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"
        fenetre.blit(titre_tutos,(200,50))    #affiche l'image "titre_tutos" aux coordonnées "(200,50)" de la fenêtre "fenetre"

        pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements
        but1 = font.render("But du jeu :",1,(255,255,255))
        but2 = font.render("Realisez le maximum de combinaisons",1,(255,255,255))
        but3 = font.render("de touches en 30 secondes pour",1,(255,255,255))
        but4 = font.render("casser le maximum de pasteques !",1,(255,255,255))

        combo1 = font.render("Combo :",1,(255,255,255))
        combo2 = font.render("Combo < 10 : Score X1 et 3 touches",1,(255,255,255))
        combo3 = font.render("Combo entre 10 et 20 : Score X2 et 4 touches",1,(255,255,255))
        combo4 = font.render("Combo > 30 : Score X4 et 5 touches",1,(255,255,255))

        regle1 = font.render("Pasteque cassee : +1s",1,(255,255,255))
        regle2 = font.render("Pasteque ratee  : -5s",1,(255,255,255))

        fenetre.blit(but1,(290,140))
        fenetre.blit(but2,(210,178))
        fenetre.blit(but3,(210,203))
        fenetre.blit(but4,(210,228))

        fenetre.blit(regle1,(210,260))
        fenetre.blit(regle2,(210,285))

        fenetre.blit(combo1,(300,325))
        fenetre.blit(combo2,(180,360))
        fenetre.blit(combo3,(180,385))
        fenetre.blit(combo4,(180,410))

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
#################### PAGE 2 ####################
def Tutoriel2():
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
            self.Button1.create_button(self.screen, (127,51,6), 100, 570, 500,    75,    0,        "Retour", (255,255,255))
            self.Button2.create_button(self.screen, (127,51,6), 100, 465, 225,    75,    0,        "Precedent", (255,255,255))
            self.Button3.create_button(self.screen, (127,51,6), 375, 465, 225,    75,    0,        "Suivant", (255,255,255))
            pygame.display.flip()


        #Run the loop
        def main(self):
            self.Button1 = Buttons.Button()
            self.Button2 = Buttons.Button()
            self.Button3 = Buttons.Button()
            self.display()
            while True:
                self.update_display()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == MOUSEBUTTONDOWN:
                        if self.Button1.pressed(pygame.mouse.get_pos()):
                            menuMain()
                        elif self.Button2.pressed(pygame.mouse.get_pos()):
                            Tutoriel()
                        elif self.Button3.pressed(pygame.mouse.get_pos()):
                            Tutoriel3()

    def menu(): #procedure qui affiche le menu



        #création fond d'écran menu
        fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()
        titre_tutos = pygame.image.load("Images/Tuto.png")
        pasteque_normale = pygame.image.load("Images/pasteque.png")
        pasteque_pourrie = pygame.image.load("Images/Pasteque_Pourris.png")
        pasteque_doree = pygame.image.load("Images/Pasteque_Doréé.png")

        fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"
        fenetre.blit(titre_tutos,(200,50))    #affiche l'image "titre_tutos" aux coordonnées "(200,50)" de la fenêtre "fenetre"
        fenetre.blit(pasteque_normale,(150,90))    #affiche l'image "pasteque_normale" aux coordonnées "(270,50)" de la fenêtre "fenetre"
        fenetre.blit(pasteque_pourrie,(150,190))    #affiche l'image "pasteque_pourrie" aux coordonnées "(370,50)" de la fenêtre "fenetre"
        fenetre.blit(pasteque_doree,(150,290))    #affiche l'image "pasteque_doree" aux coordonnées "(470,50)" de la fenêtre "fenetre"

        pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements

        points2 = font.render("Pasteque normale",1,(255,255,255))
        points3 = font.render("100 points",1,(255,255,255))
        points4 = font.render("Pasteque pourrie",1,(255,255,255))
        points5 = font.render("200 points",1,(255,255,255))
        points6 = font.render("Pasteque doree",1,(255,255,255))
        points7 = font.render("500 points",1,(255,255,255))

        fenetre.blit(points2,(300,165))
        fenetre.blit(points3,(300,195))
        fenetre.blit(points4,(300,265))
        fenetre.blit(points5,(300,295))
        fenetre.blit(points6,(300,365))
        fenetre.blit(points7,(300,395))

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
#################### PAGE 3 ####################
def Tutoriel3():
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
            self.Button1.create_button(self.screen, (127,51,6), 100, 570, 500,    75,    0,        "Retour", (255,255,255))
            self.Button2.create_button(self.screen, (127,51,6), 100, 465, 500,    75,    0,        "Precedent", (255,255,255))
            pygame.display.flip()


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
                            menuMain()
                        elif self.Button2.pressed(pygame.mouse.get_pos()):
                            Tutoriel2()

    def menu(): #procedure qui affiche le menu



        #création fond d'écran menu
        fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()
        titre_tutos = pygame.image.load("Images/Tuto.png")
        bombe = pygame.image.load("Images/bombe.png")
        fleche_noire = pygame.image.load("Images/fleche_droite_noire.png")
        fleche_jaune = pygame.image.load("Images/fleche_droite_jaune.png")

        fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"
        fenetre.blit(titre_tutos,(200,50))    #affiche l'image "titre_tutos" aux coordonnées "(200,50)" de la fenêtre "fenetre"
        fenetre.blit(bombe,(140,95))    #affiche l'image "bombe" aux coordonnées "(270,50)" de la fenêtre "fenetre"
        fenetre.blit(fleche_noire,(180,243))    #affiche l'image "fleche_noire" aux coordonnées "(370,50)" de la fenêtre "fenetre"
        fenetre.blit(fleche_jaune,(180,345))    #affiche l'image "fleche_jaune" aux coordonnées "(470,50)" de la fenêtre "fenetre"

        pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements

        points2 = font.render("Bombes",1,(255,255,255))
        points3 = font.render("Appuyez sur espace",1,(255,255,255))
        points4 = font.render("Fleche noire",1,(255,255,255))
        points5 = font.render("Appuyez sur la fleche",1,(255,255,255))
        points6 = font.render("correspondante",1,(255,255,255))
        points7 = font.render("Fleche jaune",1,(255,255,255))
        points8 = font.render("Appuyez sur l'inverse de",1,(255,255,255))
        points9 = font.render("la fleche correspondante",1,(255,255,255))

        fenetre.blit(points2,(300,165))
        fenetre.blit(points3,(300,195))
        fenetre.blit(points4,(300,255))
        fenetre.blit(points5,(300,285))
        fenetre.blit(points6,(300,305))
        fenetre.blit(points7,(300,355))
        fenetre.blit(points8,(300,385))
        fenetre.blit(points9,(300,405))

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
#################### FIN DU TUTORIEL ####################

################### Fenetre nom joueur ####################
def Nom_Joueur(nomDuJoueur):
    fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()

    # Création du texte du score
    fenetre.blit(fond_e,(0,0))

    tnom = font.render("Rentrez votre nom",1,(240, 10, 10))
    tconf = font.render("Validez avec Entree",1,(240, 10, 10))

    class Button:
            def __init__(self):
                self.main()

            #Create a display
            def display(self):
                self.screen = fenetre

            #Update the display and show the button
            def update_display(self):
                #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
                self.Button1.create_button(self.screen, (127,51,6), 200, 500, 300,    100,    0,        "Jouer", (255,255,255))
                pygame.display.flip()


            def pressed(self):
                return self.Button1.pressed(pygame.mouse.get_pos())

            #Run the loop
            def main(self):
                self.Button1 = Buttons.Button()
                self.display()
                self.update_display()


    #name = ""

    def name(nomDuJoueur):
        fond_e = pygame.image.load("Images/fond_cuisine.jpg").convert()


        b=True
        while b:
            for evt in pygame.event.get():
                if evt.type == KEYDOWN:
                    if evt.unicode.isalpha():
                        nomDuJoueur += evt.unicode
                    elif evt.key == K_BACKSPACE:
                        nomDuJoueur = nomDuJoueur[:-1]
                    elif evt.key == K_RETURN:
                        b= False
                        return nomDuJoueur
            fenetre.blit(fond_e,(0,0))
            tnom = font1.render("Entrez votre nom",1,(255, 255, 255))
            tconf = font1.render("Validez avec Entree",1,(255, 255, 255))
            fenetre.blit(tnom,(225,175))
            fenetre.blit(tconf,(220,205))
            nomDJ = font.render(nomDuJoueur,True,(255,255,255))
            rect = nomDJ.get_rect()
            rect.center = fenetre.get_rect().center
            fenetre.blit(nomDJ,rect)
            pygame.display.flip()
    nomDuJoueur = name(nomDuJoueur)
    boutonValider = Button()
    boutonValider.update_display()

    while 1:
            # Boucle sur les différents évènement reçut
            for event in pygame.event.get():    # Ferme la fenetre si appuie sur la croix rouge
                if event.type == QUIT:
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN: # Commence le jeu si appuie sur le bouton "Valider"
                    if boutonValider.pressed():
                        Jeu(score,nomDuJoueur)
            # update txtbx


            #On refresh l'affichage
            pygame.display.flip()



################## FIN Fenetre nom joueur ################
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
        self.Button2.create_button(self.screen,(127,51,6),100,570,500,75,0,"Credit",(255,255,255))
        pygame.display.flip()

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
                        Nom_Joueur(nomDuJoueur)
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
