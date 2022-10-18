import pygame
from player import Player
from portal import Portal
pygame.init() 


info = pygame.display.Info()
SIZE = WIDTH, HEIGHT = info.current_w - 60, info.current_h - 60
font2 = pygame.font.SysFont("Liberation", 500)
bravo = font2.render("BRAVO !!!", 1, pygame.Color("White"))
class Game:

    def __init__(self):   # permet de creer des rectangles des objets et 
        self.is_playing = False
        self.player = Player()
        #self.all_portals = Portal(1600, 750) #and Portal(1600, 400)
        self.portal_s1 = Portal(WIDTH - 300, HEIGHT - 250)
        self.portal_s2 = Portal(WIDTH - 300, HEIGHT - 600)
        self.portal_s3 = Portal(WIDTH - 300, HEIGHT - 950)
        self.portal_s4 = Portal(WIDTH - 800, HEIGHT - 250)
        self.portal_s5 = Portal(WIDTH - 800, HEIGHT - 600)
        self.portal_s6 = Portal(WIDTH - 800, HEIGHT - 950)
        self.pressed = {}


    def update(self, screen):

        # appliquer l'image du joueur a l'écran
        screen.blit(self.player.image, self.player.rect)

        # appliquer les images du groupe de portails
        #game.portal.draw(screen)

        screen.blit(self.portal_s1.image, self.portal_s1.rect)
        screen.blit(self.portal_s2.image, self.portal_s2.rect)
        screen.blit(self.portal_s3.image, self.portal_s3.rect)
        screen.blit(self.portal_s4.image, self.portal_s4.rect)
        screen.blit(self.portal_s5.image, self.portal_s5.rect)
        screen.blit(self.portal_s6.image, self.portal_s6.rect)

        # deplacement directionnel
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        if self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < screen.get_height():
            self.player.move_down()
        if self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
        # redémarrage du jeu
        if self.pressed.get(pygame.K_SPACE):
            self.is_playing = False

        # collisions entre joueur et portails
        if self.player.rect.colliderect(self.portal_s1.rect):
            pygame.draw.rect(screen, (255, 0, 0), self.player.rect, 1)
            pygame.draw.rect(screen, (255, 0, 0), self.portal_s1.rect, 1)
        if self.player.rect.colliderect(self.portal_s2.rect):
            pygame.draw.rect(screen, (255, 0, 0), self.player.rect, 1)
            pygame.draw.rect(screen, (255, 0, 0), self.portal_s2.rect, 1)
        if self.player.rect.colliderect(self.portal_s3.rect):
            pygame.draw.rect(screen, (255, 0, 0), self.player.rect, 1)
            pygame.draw.rect(screen, (255, 0, 0), self.portal_s3.rect, 1)
        if self.player.rect.colliderect(self.portal_s4.rect):
            pygame.draw.rect(screen, (255, 0, 0), self.player.rect, 1)
            pygame.draw.rect(screen, (255, 0, 0), self.portal_s4.rect, 1)
        if self.player.rect.colliderect(self.portal_s5.rect):
            pygame.draw.rect(screen, (255, 0, 0), self.player.rect, 1)
            pygame.draw.rect(screen, (255, 0, 0), self.portal_s5.rect, 1)
        if self.player.rect.colliderect(self.portal_s6.rect):
            pygame.draw.rect(screen, (255, 0, 0), self.player.rect, 1)
            pygame.draw.rect(screen, (255, 0, 0), self.portal_s6.rect, 1)
            screen.blit(bravo, (WIDTH // 2 - 850, 20))


        #self.portal_spawn()

    """def portal_spawn(self):
        portal_s1 = Portal()
        portal_s2 = Portal(1600, 400)
        portal_s3 = Portal(1600, 50)
        portal_s4 = Portal(1100, 750)
        portal_s5 = Portal(1100, 400)
        portal_s6 = Portal(1100, 50)"""
       # self.all_portals.add(portal_s1, portal_s2, portal_s3, portal_s4, portal_s5, portal_s6)
