import pygame
from player import *
from game_config import *

class Personnage(pygame.sprite.Sprite) :
    def __init__(self,x,y,numero) :
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.numero = numero
        self.sprite_count = 0

        self.rect = pygame.Rect( x-GameConfig.IDLE_W/2 , y-GameConfig.IDLE_H ,GameConfig.IDLE_W,GameConfig.IDLE_H)

        self.image = GameConfig.PERSONNAGE[self.numero][0]

    def advance_state(self):
        self.sprite_count+=1
        if self.sprite_count>= GameConfig.NB_FRAMES_PER_SPRITE_IDLE*len(GameConfig.PERSONNAGE[0])  :
            self.sprite_count = 0

        self.image = GameConfig.PERSONNAGE[self.numero][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_IDLE]


    def draw(self,window):
        window.blit(self.image,self.rect.topleft)


    def changer(self,numero,player_x,player_y):
        self.x = player_x+GameConfig.PLAYER_W/2
        self.y = player_y
        self.rect = pygame.Rect( self.x-GameConfig.IDLE_W/2 , self.y-GameConfig.IDLE_H ,GameConfig.IDLE_W,GameConfig.IDLE_H)
        self.numero = numero
