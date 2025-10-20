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

    dessiner_bouton("Play", 525, 625, 200, 50, color, color, textcolor, afficher_texte)

    # Mise à jour de l'affichage
    pygame.display.flip()