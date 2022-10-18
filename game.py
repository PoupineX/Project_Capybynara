import pygame
import random
import math
from game import Game

pygame.init()
info = pygame.display.Info()
SIZE = WIDTH, HEIGHT = info.current_w - 60, info.current_h - 60
screen = pygame.display.set_mode(SIZE)
# generer la fenêtre de jeu
pygame.display.set_caption("Capybynara")

# importer l'arriere-plan
background1 = pygame.image.load("assets_NSI/bg1.png")

# charger le jeu
#if __name__ =="__main__":    

#game.run()


# mettre le nombre a traduire en haut de l'ecran
font = pygame.font.SysFont("Liberation", 100)

# creation les listes de propositions pour le QCM
nbin_f = [16, 2, 3, 10, 8, 12, 15, 7, 4, 5, 6, 9, 11, 13]       # QCM facile
nbin_m = [32, 40, 56, 17, 127, 64, 68]                          # QCM medium
nbin_d = [256, 175, 89, 243, 257, 512, 524, 532, 1024, 1064]    # QCM difficile

# nbin1 est choisit aleatoirement dans la liste ( facile pour l'instant ), c'est la "bonne reponse"
nbin1 = random.choice(nbin_f)

# la meme "bonne reponse" en binaire
nbin1_atr = bin(random.choice(nbin_f))
nbin2 = random.choice(nbin_m)
nbin3 = random.choice(nbin_d)

# Crée un affichage pour la bonne reponse a trouver en binaire
questions = font.render(str(nbin1), 1, pygame.Color("White"))

# Algorithme permettant de renvoyer les reponses du QCM
def nbs_atr(reponse,n_bin_):
    """Cette fonction renvoie une liste de 6 éléments dont un élément est la bonne reponse (nbin1)
      reponse : la réponse de type int
      n_bin : la liste du niveau, de type int

    sortie : la liste de 6 éléments de type int dont un seul qui est la bonne réponse, placée aléatoirement
             tous les éléments sont deux à deux différents"""

    lcal_nbin = list(n_bin_) # copie de la liste (en non le pointeur)
    L=[]
    L.append(reponse)
    lcal_nbin.remove(reponse)
    for _ in range(5):
        nombre = random.choice(lcal_nbin)
        print(nombre,L,lcal_nbin)       #### A ENLEVER ####
        L.append(nombre)
        lcal_nbin.remove(nombre)
    random.shuffle(L)
    return L

# liste des reponses QCM faciles
L1 = nbs_atr(nbin1, nbin_f)
print(nbin1, L1)    #### A ENLEVER ####

# liste des reponses QCM moyennes
# L2 = nbs_atr(nbin2, nbin_m)

# liste des reponses QCM difficiles
# L2 = nbs_atr(nbin3, nbin_d)

print(nbin1)       #### A ENLEVER ####
def i_nbin1(list):
    """Prends en argument une liste de 6 reponses et renvoie l'indice de la bonne reponse"""
    b_rep = 0
    for i in range(len(list)):
        if list[i] == nbin1:
            b_rep = i
    return b_rep

print(i_nbin1(L1))

# appliquer a l'écran les reponses pour le QCM
response1 = font.render(str(bin(L1[0])), 1, pygame.Color("Red"))    # Avant c'etait : response1 = font.render(str(nbin1_atr), 1, pygame.Color("Red"))
response2 = font.render(str(bin(L1[1])), 1, pygame.Color("Red"))    # response2 //
response3 = font.render(str(bin(L1[2])), 1, pygame.Color("Red"))    # response3 //
response4 = font.render(str(bin(L1[3])), 1, pygame.Color("Red"))    # ...4      //
response5 = font.render(str(bin(L1[4])), 1, pygame.Color("Red"))    # ...5      //
response6 = font.render(str(bin(L1[5])), 1, pygame.Color("Red"))    # ...6      //

######################################################### Essai ############################################################################
#rectreponse1 = response1.get_rect()

# ecran d'introduction au jeu
intro = pygame.image.load("assets_NSI/capy.png")
intro_rect = intro.get_rect()
intro_rect.x = 0
intro_rect.y = -140
intro_txt = font.render("Welcome !", 1, pygame.Color("Green"))
play_button = pygame.image.load("assets_NSI/start_btn.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(WIDTH / 3 + 100)
play_button_rect.y = math.ceil(HEIGHT / 2 - 100)

game = Game()
running = True
clock = pygame.time.Clock()

# boucle tant que cette condition est vraie
while running:
    
    # rafraichir a 60 images par seconde
    clock.tick(60)

    # appliquer l'arriere-plan
    screen.blit(background1, (0, -350))

    if game.is_playing:
        game.update(screen)

        # appliquer le nombre a trouver en haut de l'écran
        screen.blit(questions, (WIDTH // 2 - 60, 20))

        # appliquer le QCM
        screen.blit(response6, (game.portal_s6.rect))
        screen.blit(response5, (game.portal_s5.rect))
        screen.blit(response4, (game.portal_s4.rect))
        screen.blit(response3, (game.portal_s3.rect))
        screen.blit(response2, (game.portal_s2.rect))    
        screen.blit(response1, (game.portal_s1.rect))
    else:
        # afficher ecran d'intro
        screen.blit(intro, (intro_rect.x, intro_rect.y))
        screen.blit(play_button, (play_button_rect.x, play_button_rect.y))
        screen.blit(intro_txt, (WIDTH // 2 - 200, 20)) 


    # mettre a jour l'écran
    pygame.display.flip()
    #while not done:
# si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            running = False
            pygame.quit()
            print("Le jeu est fermé") # A ENLEVER !!!!!!!!!!
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                pygame.draw.rect(screen, (255, 0, 0), play_button_rect, 1)
                game.is_playing = True
