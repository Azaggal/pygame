import pygame
from player import *
from game_config import *

class Mort(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.sprite_count=0

        self.fin = GameConfig.NB_FRAMES_PER_SPRITE_MORT*len(Mort.IMAGES)

        self.image = Mort.IMAGES[0]




    def advance_state(self):
        self.sprite_count+=1

        self.image = Mort.IMAGES[self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_MORT]

    def init_sprites():
        Mort.IMAGES = GameConfig.MORT


    def draw(self,window):
        window.blit(self.image,(self.x,self.y))
