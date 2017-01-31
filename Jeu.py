# -*- coding:Utf-8 -*-
# Ligne permettant l'utilisation des accents

# Importation de pygame
import pygame, Classes, random, time
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
time = 10
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

# variable globale fixe longueur combo
longueur_combo = 5

liste_fleches = combo_random(longueur_combo);

numFlecheCour = 0

# Boucle infinie pour affichage permanent de la fenêtre
while 1:
    #accès a l'élément courant de la liste de fleches
    flecheCour = liste_fleches[numFlecheCour]

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
            if event.key == K_a:       # Si appuie sur la fleche du haut
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
                elif isinstance(monObjet, Classes.Bombe):           # Si l'objet est une Bombe
                    import game_over
                    pygame.display.flip()
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
                print "erreur"
                #passage a l'objet suivant
                liste_fleches = combo_random(longueur_combo);
                numFlecheCour = 0
            #si on arrive a la derniere fleche il faut passer a l'objet suivant
            if numFlecheCour == longueur_combo:
                #temps?
                liste_fleches = combo_random(longueur_combo);
                numFlecheCour= 0
    if time == 0:
        import game_over
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
