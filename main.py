# Coding UTF-8

# imports
import pygame
from game import Game


pygame.init()
# Creer la classe du jeu


#Générer la fenêtre
pygame.display.set_caption("Comet Fall Game")

screen = pygame.display.set_mode((1080,720))

background = pygame.image.load("assets/bg.jpg")

# Charger le joueur

# player = Player()
game = Game()
running = True

# Boucle tant que running est vrai

while running:

    # Appliquer l'arrire plan
    screen.blit(background,(0,-200))

    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # Vérifier si le joueur va a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.moveRight()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.moveLeft()


    # Mettre a jour la fenetre
    pygame.display.flip()

    # Si le joueur ferme la fenetre
    for event in pygame.event.get():
        # Vérifier l'event de fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        # Si un joueur appuie sur une touche du clavier
        elif event.type == pygame.KEYDOWN:
            # On détecte une touche enfoncé
           game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            # on détecte quand la touche est relaché
            game.pressed[event.key] = False