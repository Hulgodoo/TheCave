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
color = (116, 208, 241)
textcolor = (255, 255, 255)

# Charger une image et la redimensionner 
image1 = pygame.image.load("logo.png")
image1 = pygame.transform.scale(image1, (LARGEUR, HAUTEUR))

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

fin = False

# Boucle principale du jeu, tant que le jeu n'est pas fini on continue
while fin == False:

    # Boucle de gestion des évènements dans la fenêtre 
    for event in pygame.event.get():
        
        # Si l'utilisateur appuie sur la croix en haut à droite, cela met fin au jeu et ferme pygame 
        if event.type == pygame.QUIT:
            fin = True
            pygame.quit()

    # Remplir l'écran de bleu
    #fenetre.fill(color)
    
    # Afficher l'image à l'écran, le coin en haut à gauche à la coordonnée 0,0
    fenetre.blit(image1, (0, 0))
    
    #Afficher du texte
    afficher_texte("The Cave", 425, 400, textcolor)

    # Mise à jour de l'affichage
    pygame.display.flip()