import pygame
import time

# Initialisation de pygame
pygame.init()

# Paramètres de la fenêtre
LARGEUR= 1300
HAUTEUR = 900
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("The Cave")

# Changer l'icône de la fenêtre
icone = pygame.image.load("logo.png")  
pygame.display.set_icon(icone)  

# Police de texte
font = pygame.font.Font("KiwiSoda.ttf", 100)

# Définition des variables des couleurs à utiliser dans le programme
color = (0, 0, 0)
bleu = (116, 208, 241)
textcolor = (255, 255, 255)

# Charger une image et la redimensionner 
image1 = pygame.image.load("logo.png")
image1 = pygame.transform.scale(image1, (LARGEUR, HAUTEUR))

# Variables du jeu
level = "menu"
nb_level = 0
lives = 2
objects = ("dynamite", "boots", "pickaxe", "4", "5")
inventory = ()

def afficher_texte(texte, x, y, couleur):
    """
    Cette fonction permet d'afficher du texte dans une fenêtre Pygame à partir d'une position donnée (x, y). Si une ligne de texte dépasse
    la largeur de la fenêtre, elle est automatiquement coupée et continuée à la ligne suivante.

    Paramètres :
    -----------
        texte(str) : Le texte à afficher.
        x(int) : La position en pixels sur l'axe des abscisses (horizontal) où le texte commence à être affiché.
        y(int) : La position en pixels sur l'axe des ordonnées (vertical) où le texte commence à être affiché.
        couleur(tuple): Une couleur définie sous forme de tuple (R, G, B) pour la couleur du texte.
    """
    mots = texte.split(' ')
    ligne_actuelle = ''
    y_offset = 0  

    for mot in mots:
        # Vérifie si on peut ajouter le mot à la ligne actuelle
        if font.size(ligne_actuelle + mot)[0] <= LARGEUR - x:
            ligne_actuelle += mot + ' '
        else:
            # Dessine la ligne actuelle et réinitialise pour la nouvelle ligne
            fenetre.blit(font.render(ligne_actuelle.strip(), True, couleur), (x, y + y_offset))
            ligne_actuelle = mot + ' '
            y_offset += font.get_height()  # Augmente l'offset pour la prochaine ligne

    # Dessine la dernière ligne si elle n'est pas vide
    if ligne_actuelle:
        fenetre.blit(font.render(ligne_actuelle.strip(), True, couleur), (x, y + y_offset))

def dessiner_bouton(texte, x, y, largeur, hauteur, couleur1, couleur2, couleurtexte, action=None):
    """
    Cette fonction dessine un bouton interactif dans une fenêtre Pygame. Le bouton change de couleur lorsque la souris le survole,
    et exécute une action si l'utilisateur clique dessus.

    Paramètres :
    -----------
        texte (str) : Le texte à afficher à l'intérieur du bouton.
        x (int) : La position en pixels sur l'axe des abscisses (horizontal) où le bouton commence à être dessiné.
        y (int) : La position en pixels sur l'axe des ordonnées (vertical) où le bouton commence à être dessiné.
        largeur (int) : La largeur souhaitée du bouton. La largeur réelle sera ajustée en fonction de la taille du texte.
        hauteur (int) : La hauteur souhaitée du bouton. La hauteur réelle sera ajustée en fonction de la taille du texte.
        couleur1 (tuple) : La couleur du bouton sous forme de tuple (R, G, B) lorsque la souris n'est pas dessus.
        couleur2 (tuple) : La couleur du bouton sous forme de tuple (R, G, B) lorsque la souris survole le bouton.
        couleurtexte (tuple) : La couleur du texte du bouton sous forme de tuple (R, G, B).
        action (fonction, optionnel) : Une fonction à exécuter lorsque le bouton est cliqué. Par défaut, aucune action n'est exécutée.
    """
    
    # Calculer la taille du texte
    largeur_texte, hauteur_texte = font.size(texte)
    largeur_bouton = max(largeur, largeur_texte + 20)  # Ajouter un peu de marge
    hauteur_bouton = max(hauteur, hauteur_texte + 10)  # Ajouter un peu de marge

    souris = pygame.mouse.get_pos()
    clic = pygame.mouse.get_pressed()

    # Détection de survol de la souris
    if x + largeur_bouton > souris[0] > x and y + hauteur_bouton > souris[1] > y:
        pygame.draw.rect(fenetre, couleur2, (x, y, largeur_bouton, hauteur_bouton))
        if clic[0] == 1 and action is not None:
            time.sleep(0.2)
            action()
    else:
        pygame.draw.rect(fenetre, couleur1, (x, y, largeur_bouton, hauteur_bouton))

    # Dessiner le texte centré dans le bouton
    texte_surface = font.render(texte, True, couleurtexte)
    texte_rect = texte_surface.get_rect(center=(x + largeur_bouton // 2, y + hauteur_bouton // 2))
    fenetre.blit(texte_surface, texte_rect)

def choix_gauche():
    """
    Cette fonction permet de changer de scene lorsqu'on a choisi le bouton de gauche. 

    """
    global level
    global nb_level

    if level == "menu":
        level = "choices"
    elif level == "choices":
        level = "mineur"
    elif level == "mineur":
        level = "choices"
        nb_level = nb_level + 1

def choix_droite():
    """
    Cette fonction permet de changer de scene lorsqu'on a choisi le bouton de droite. 

    """
    global level
    global nb_level
    global lives

    if level == "menu":
        level = "choices"
    elif level == "choices":
        level = "monstres"
    elif level == "monstres":
        level = "choices"
        lives = lives - 1
        nb_level = nb_level + 1
    
        


def afficher_vies():
    """
    Cette fonction permet d'afficher la vie que le joueur a. 

    """
    global lives

    afficher_texte(str(lives), 0, 0, textcolor)

def menu():
    """
    Cette fonction permet d'afficher le menu. 

    """
    global level
    # Afficher l'image à l'écran, le coin en haut à gauche à la coordonnée 0,0
    fenetre.blit(image1, (0, 0))
    
    #Afficher du texte
    afficher_texte("The Cave", 425, 400, textcolor)

    dessiner_bouton("Play", 525, 625, 200, 50, color, color, textcolor, choix_droite)

def choices():

    """
    Cette fonction permet d'afficher les choix.

    """
    global level
    global fin

    level == "choices"
    # Charger une image et la redimensionner 
    gauche = pygame.image.load("cart.png")
    gauche = pygame.transform.scale(gauche, (650, 900))
    fenetre.blit(gauche, (0, 0))

    droite = pygame.image.load("entrance.png")
    droite = pygame.transform.scale(droite, (650, 900))
    fenetre.blit(droite, (650, 0))

    #Afficher du texte
    afficher_texte("Choose.", 500, 400, textcolor)

    dessiner_bouton("^", 250, 550, 200, 50, color, color, textcolor, choix_gauche)
    dessiner_bouton("^", 900, 550, 200, 50, color, color, textcolor, choix_droite)
    

def monstres():
    
    """
    Cette fonction permet d'afficher les monstres.

    """
    global level

    level == "monstres"
    # Charger une image et la redimensionner 
    image = pygame.image.load("dragon.png")
    image = pygame.transform.scale(image, (LARGEUR, HAUTEUR))
    fenetre.blit(image, (0, 0))

    #Afficher du texte
    afficher_texte("Fight !", 500, 400, textcolor)

    dessiner_bouton("Taper", 500, 625, 200, 50, color, color, textcolor, choix_droite)

def mineur():
    
    """
    Cette fonction permet d'afficher les monstres.

    """
    global level

    level == "mineur"
    # Charger une image et la redimensionner 
    image = pygame.image.load("mineur.png")
    image = pygame.transform.scale(image, (LARGEUR, HAUTEUR))
    fenetre.blit(image, (0, 0))

    #Afficher du texte
    afficher_texte("Take this", 425, 400, textcolor)

    dessiner_bouton("^", 530, 825, 200, 50, color, color, textcolor, choix_gauche)

def boss():
       
    """
    Cette fonction permet d'afficher le boss du jeu.

    """ 
    global nb_level
    global level

    image = pygame.image.load("final_entrance(wip).png")
    image = pygame.transform.scale(image, (LARGEUR, HAUTEUR))
    fenetre.blit(image, (0, 0))
    pygame.display.flip()
    pygame.time.wait(2000)  # 2000 ms = 2 secondes
    
    fenetre.fill(color)
    pygame.display.flip()
    pygame.time.wait(1000)
    
    image2 = pygame.image.load("boss1.png")
    image2 = pygame.transform.scale(image2, (LARGEUR, HAUTEUR))
    fenetre.blit(image2, (0, 0))

    nb_level = 99
    level = "end"


fin = False

# Boucle principale du jeu, tant que le jeu n'est pas fini on continue
while fin == False:

    # Boucle de gestion des évènements dans la fenêtre 
    for event in pygame.event.get():
        
        # Si l'utilisateur appuie sur la croix en haut à droite, cela met fin au jeu et ferme pygame 
        if event.type == pygame.QUIT:
            fin = True
            pygame.quit()
    
    afficher_vies()
    if nb_level == 5:
        level = "boss"
    
    # Afficher le niveau
    if level == "menu":
        menu()
    elif level == "choices":
        choices()
        afficher_vies()    
    elif level == "monstres":
        monstres()
        afficher_vies() 
    elif level == "mineur":
        mineur()
        afficher_vies()
    elif level == "boss":
        boss()
        afficher_vies()
    if lives == 0:
        fenetre.fill(color)
        afficher_texte("Dead", 525, 400, textcolor)
        fin = True
    # Mise à jour de l'affichage
    pygame.display.flip()
time.sleep(5)
pygame.quit()