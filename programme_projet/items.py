import pygame
from player import *
from game_config import *

class Items(pygame.sprite.Sprite) :
    def __init__(self, x, y, vitesse_player, vitesse_proj, cadence, vie, degats_proj) :
        

        self.rect = pygame.Rect( x, y, GameConfig.PROJECTILE_W, GameConfig.PROJECTILE_H)

        self.vitesse_player = vitesse_player
        self.vitesse_proj = vitesse_proj
        self.cadence = cadence
        self.vie = vie
        self.degats_proj = degats_proj
        self.etat = True

        if self.vitesse_player != 0:
            self.image = GameConfig.ITEM_VITESSE_PLAYER
        elif self.vitesse_proj != 0:
            self.image = GameConfig.ITEM_VITESSE_PROJ
        elif self.cadence != 0:
            self.image = GameConfig.ITEM_CADENCE
        elif self.vie != 0:
            self.image = GameConfig.ITEM_VIE
        elif self.degats_proj !=0:
            self.image = GameConfig.ITEM_DEGATS_PROJ

    def draw(self,window):
        window.blit(self.image,self.rect.topleft)
        

    def is_touching(self,player):
        return pygame.sprite.collide_mask(self,player)
