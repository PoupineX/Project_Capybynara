import pygame

# classe representant les portails (6)
class Portal(pygame.sprite.Sprite):

    pos = [(1600, 810), (1600, 450), (1600, 90), (1100, 810), (1100, 450), (1100, 90)]
    def __init__(self, x, y, bonne_reponse):
        super().__init__()
        self.image = pygame.image.load("assets_NSI/portal_s.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.reponse = bonne_reponse
