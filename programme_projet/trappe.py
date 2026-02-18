import pygame
from game_config import *
from map import *

class Trappe(pygame.sprite.Sprite) :
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect( x, y, GameConfig.TRAPPE_W, GameConfig.TRAPPE_H)

        self.status = GameConfig.TRAPPE

        self.ouverte = False

    def draw(self,window):
        if Map.SALLE_COURANTE != 4 :
            window.blit(self.status[self.ouverte],self.rect.topleft)