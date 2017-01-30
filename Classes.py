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

    # Méthode gérant les déplacements des pasteques
    def movement(self):
         # Déplacement de la pasteque
         self.rect = self.rect.move(self.speed)

         # On teste si la pasteque à atteint l'un des bords de l'écran
         # Si oui on change sa direction
         if self.rect.left < 0 or self.rect.right > 700:
             self.speed[0] = -self.speed[0]

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
