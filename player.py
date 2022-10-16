import pygame

# classe representant le joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets_NSI/capybara.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 390
        self.velocity = 30
        self.hp = 10

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity
