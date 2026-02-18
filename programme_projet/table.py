import pygame
from player import *
from game_config import *

class Table(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        

        self.rect = pygame.Rect( x, y, 96, 78)

        self.image = GameConfig.TABLE
        self.numero = 0

    def draw(self,window):
        window.blit(self.image,self.rect.topleft)
        

    def is_touching(self,player):
        return pygame.sprite.collide_mask(self,player)
