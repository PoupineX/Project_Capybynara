import pygame
from pygame import *
from pygame import key 
from moviepy.editor import *

pygame.init()
class Button():
    def __init__(self, x, y, image):
        self.image = image 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #affiche le bouton sur l'ecrant
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

largeur = 1080
hauteur = 720

screen = pygame.display.set_mode((largeur,hauteur))


start_img = pygame.image.load("assets_NSI/start_btn.png").convert_alpha() #### Image a trouver ####
exit_img = pygame.image.load("assets_NSI/exit_btn.png").convert_alpha() #### Image a trouver ####

exit_button = Button(400, 550, exit_img)
exit2_button = Button(750, 25, exit_img)
level1_button = Button(350, 100, start_img)
level2_button = Button(350, 250, start_img)
level3_button = Button(350, 400, start_img)
menu_button = Button(350, 100, start_img)
back_game = Button(350, 250, start_img)

fond = screen.fill((202, 228, 241))

play_state = "menu"
run = True
musique = True
pause = False

clip = VideoFileClip("assets_NSI/background.mp4") #### Video a trouver ####
clip = clip.resize((1080, 720))

pygame.mixer.music.load("assets_NSI/theme.mp3")

while run:

    if musique == True:
        pygame.mixer.music.play(100)
        musique = False

    if pause:
        print("test")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        if back_game.draw():
            pause = False
        if exit2_button.draw():
            run = False
    else:
        a = 0



    if play_state == "menu": 
        if level1_button.draw():
            play_state = "level_1"
            pygame.mixer.music.stop()
            clip.preview()
            display.update(screen.fill(0))

            print("c")

        elif level2_button.draw():
            play_state = "level_2"
            pygame.mixer.music.stop()
            clip.preview()
            display.update(screen.fill(0))

        elif level3_button.draw():
            play_state = "level_3"
            pygame.mixer.music.stop()
            clip.preview()
            display.update(screen.fill(0))

        elif exit_button.draw():
            run = False


    if play_state == "level_1":
        if pause == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        print("une_action()")
                        pause = True
            print("level 1")


    if play_state == "level_2":
        if pause == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        print("une_action()")
                        pause = True
            print("level 2")



    if play_state == "level_3":
        if pause == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        print("une_action()")
                        pause = True
            print("level 3")



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()