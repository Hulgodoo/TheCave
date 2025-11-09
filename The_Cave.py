import pygame
import time
import random

# Initialisation de pygame
pygame.init()

# Paramètres de la fenêtre
LARGEUR= 1000
HAUTEUR = 1000
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
lives = 3
objects = ("dynamite", "boots", "pickaxe")
inventory = ()
random_object = "vide"
random_monster = "vide"
input_active = False
prenom_joueur = ""


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

def afficher_texte_boss(texte, x, y, couleur):
    """
    Cette fonction permet d'afficher du texte pour le boss dans une fenêtre Pygame à partir d'une position donnée (x, y). Si une ligne de texte dépasse
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

    font = pygame.font.Font("KiwiSoda.ttf", 50)

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
    global random_object
    global inventory
    global lives

    if level == "menu":
        level = "choices"
    elif level == "choices" and (nb_level == 1 or nb_level == 3):
        level = "monstres"
    elif level == "choices" and (nb_level == 0 or nb_level == 2 or nb_level == 4):
        level = "mineur"
    elif level == "monstres":
        level = "choices"
        nb_level = nb_level + 1
    elif level == "mineur":
        level = "choices"
        nb_level = nb_level + 1
        inventory = inventory + (random_object,)
        random_object = "vide"
    

def choix_droite():
    """
    Cette fonction permet de changer de scene lorsqu'on a choisi le bouton de droite. 

    """
    global level
    global nb_level
    global lives

    if level == "menu":
        level = "choices"
    elif level == "choices" and (nb_level == 0 or nb_level == 2 or nb_level == 4):
        level = "monstres"
    elif level == "choices" and (nb_level == 1 or nb_level == 3):
        level = "mineur"
    elif level == "monstres":
        level = "choices"
        nb_level = nb_level + 1
    elif level == "mineur":
        level = "choices"
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
    afficher_texte("The Cave", 325, 500, textcolor)

    dessiner_bouton("Play", 400, 750, 200, 50, color, color, textcolor, choix_droite)

def choices():

    """
    Cette fonction permet d'afficher les choix.

    """
    global level
    global fin

    level = "choices"
    # Charger une image et la redimensionner 
    image = pygame.image.load("choices.png")
    image = pygame.transform.scale(image, (1000, 1000))
    fenetre.blit(image, (0, 0))

    #Afficher du texte
    afficher_texte("Choose.", 350, 500, textcolor)

    dessiner_bouton("^", 150, 700, 200, 50, color, color, textcolor, choix_gauche)
    dessiner_bouton("^", 600, 700, 200, 50, color, color, textcolor, choix_droite)
    

def monstres():
    
    """
    Cette fonction permet d'afficher les monstres.

    """
    global level

    level = "monstres"
    # Charger une image et la redimensionner
    
    image = pygame.image.load("dragon.png")
    image = pygame.transform.scale(image, (LARGEUR, HAUTEUR))
    fenetre.blit(image, (0, 0))

    #Afficher du texte
    afficher_texte("Run !", 375, 100, textcolor)
    dessiner_bouton("Throw something", 140, 650, 200, 50, color, color, textcolor, vider_inventaire)
    dessiner_bouton("-1 live", 350, 850, 200, 50, color, color, textcolor, perte_vie)

def vider_inventaire():
    """
    Cette fonction permet de vider l'inventaire.

    """
    global inventory
    global level

    if len(inventory) > 0:
        inventory = inventory[:-1]
        choix_droite()
    else:
        perte_vie()

def perte_vie():
    """
    Cette fonction permet de faire perdre une vie au joueur.

    """
    global lives
    global level

    lives = lives - 1
    if level == "monstres":
        choix_droite()

def mineur():
    
    """
    Cette fonction permet d'afficher le mineur.

    """
    global level
    global random_object

    # Charger une image et la redimensionner 
    image = pygame.image.load("mineur.png")
    image = pygame.transform.scale(image, (LARGEUR, HAUTEUR))
    fenetre.blit(image, (0, 0))

    # Sélectionner un objet seulement la première fois
    if random_object == "vide":
        random_object = random.choice(objects)
        
    # Afficher texte et objet
    afficher_texte("Take this", 325, 500, textcolor)
    afficher_objet(random_object)
    dessiner_bouton("^", 400, 900, 200, 50, color, color, textcolor, choix_gauche)
    

def boss():
       
    """
    Cette fonction permet d'afficher le boss du jeu.

    """ 
    global nb_level
    global level

    level = "bossfight"

    image = pygame.image.load("final_entrance2.png")
    image = pygame.transform.scale(image, (LARGEUR, HAUTEUR))
    fenetre.blit(image, (0, 0))
    pygame.display.flip()
    pygame.time.wait(1500)
    
    fenetre.fill(color)
    pygame.display.flip()
    pygame.time.wait(400)

    image1 = pygame.image.load("boss-tonnerre.png")
    image1 = pygame.transform.scale(image1, (LARGEUR, HAUTEUR))
    fenetre.blit(image1, (0, 0))
    pygame.display.flip()
    pygame.time.wait(800)

    fenetre.fill(color)
    pygame.display.flip()
    pygame.time.wait(400)
    

    nb_level = 99
    level = "bossfight"

def next_boss_level():
    """
    Cette fonction permet de passer au niveau suivant après le boss.

    """ 
    global level


    if level == "bossfight":
        level = "dynamite"
    elif level == "dynamite":
        level = "pickaxe"
    elif level == "pickaxe":
        level = "boots"
    elif level == "boots":
        level = "escape"

def boss_fail():
    
    """
    Cette fonction permet de faire les conséquences si on n'a pas l'objet voulu au boss.

    """
    perte_vie()
    next_boss_level()

def bossfight():

    """
    Cette fonction permet d'afficher le boss du jeu.

    """

    image2 = pygame.image.load("boss1.png")
    image2 = pygame.transform.scale(image2, (LARGEUR, HAUTEUR))
    fenetre.blit(image2, (0, 0))

    afficher_texte_boss("You have made it this far...", 200, 50, (255, 0, 0))
    afficher_texte_boss("But this is where your journey ends!", 150, 150, (255, 0, 0))
    afficher_texte_boss("My monsters will love a kid sandwich.", 125, 750, (255, 0, 0))

    dessiner_bouton("Try to run :D >>", 150, 850, 200, 50, color, color, (255, 0, 0), next_boss_level)

def dynamite():

    """
    Cette fonction permet d'afficher la scène de fin de la dynamite.

    """
    global inventory

    # Charger une image et la redimensionner
    if "dynamite" in inventory:
        image = pygame.image.load("dynamite_scene.png")
        image = pygame.transform.scale(image, (LARGEUR, HAUTEUR))
        fenetre.blit(image, (0, 0))
        afficher_texte_boss("bla blz boum", 125, 750, textcolor)
        dessiner_bouton(">>>", 140, 650, 200, 50, color, color, textcolor, next_boss_level)
    else:
        image = pygame.image.load("attack_boss.png")
        image = pygame.transform.scale(image, (LARGEUR, HAUTEUR))
        fenetre.blit(image, (0, 0))
        afficher_texte_boss("bla blz zut", 125, 750, textcolor)
        dessiner_bouton(">>>", 140, 650, 200, 50, color, color, textcolor, boss_fail)


def afficher_objet(objet):

    """
    Cette fonction permet d'afficher un objet.

    Paramètre:
        objet: signifie l'objet à afficher.

    """ 
    if objet == "dynamite":
        image = pygame.image.load("dynamite.png")
    elif objet == "boots":
        image = pygame.image.load("boots.png")
    elif objet == "pickaxe":
        image = pygame.image.load("pickaxe.png")
    image = pygame.transform.scale(image, (200, 200))
    fenetre.blit(image, (400, 600))

def afficher_inventory():
    """
    Cette fonction permet d'afficher l'inventaire du joueur.

    """
    global inventory

    y_position = 50

    for objet in inventory:
        if objet == "dynamite":
            image = pygame.image.load("dynamite.png")
        elif objet == "boots":
            image = pygame.image.load("boots.png")
        elif objet == "pickaxe":
            image = pygame.image.load("pickaxe.png")
        
        image = pygame.transform.scale(image, (50, 50))
        fenetre.blit(image, (925, y_position))
        y_position += 60  

def dead():
    """
    Cette fonction permet d'afficher l'écran de fin lorsque le joueur n'a plus de vie.

    """
    global level
    global fin

    fenetre.fill(color)
    pygame.display.flip()

    if level == "choices" or level == "mineur" or level == "monstres":
        afficher_texte("Dead", 200, 450, textcolor)
    elif level == "boss":
        afficher_texte_boss("You are a dumb sandwich", 200, 450, textcolor)

    level = "dead"
    fin = True


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
    # Vérifier si le joueur est mort
    if lives <= 0:
        dead()
    if nb_level == 5:
        level = "boss"
    
    # Afficher le niveau
    if level == "menu":
        menu()
    elif level == "choices":
        choices()
        afficher_vies()
        afficher_inventory()
    elif level == "monstres":
        monstres()
        afficher_vies()
        afficher_inventory()
    elif level == "mineur":
        mineur()
        afficher_vies()
        afficher_inventory()
    elif level == "boss":
        boss()
        afficher_vies()
        afficher_inventory()
    elif level == "bossfight":
        bossfight()
        afficher_vies()
        afficher_inventory()
    elif level == "dynamite":
        dynamite()
        afficher_vies()
    elif level == "pickaxe":
        pickaxe()
        afficher_vies()
    elif level == "boots":
        boots()
        afficher_vies()
    elif level == "escape":
        escape()
        afficher_vies()
    # Mise à jour de l'affichage
    pygame.display.flip()
time.sleep(5)
pygame.quit()