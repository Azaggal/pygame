import pygame
from game_config import *
from random import *
from projectiles import *
from math import atan2,cos,sin


class Mannequin(pygame.sprite.Sprite) :
    LEFT = -1
    RIGHT = 1
    UP = -1
    DOWN = 1
    NONE = 0
    #Constructeur
    def __init__(self,x,y) :
        pygame.sprite.Sprite.__init__(self)
        self.direction = [Mannequin.NONE,Mannequin.NONE]
        self.sprite_count=0
        self.projectile = []
        self.max_vie = 15
        self.vie = self.max_vie

        self.rect = pygame.Rect( x , 
            y,
            GameConfig.ENEMY_CORPS_A_CORPS_W,
            GameConfig.ENEMY_CORPS_A_CORPS_H)
        
        self.image = Mannequin.IMAGES[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_CORPS_A_CORPS]
        self.mask = Mannequin.MASKS[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_CORPS_A_CORPS]

    def init_sprites():
        Mannequin.IMAGES = {Mannequin.LEFT : GameConfig.WALK_LEFT_IMG_ENEMY_CORPS,Mannequin.RIGHT : GameConfig.WALK_RIGHT_IMG_ENEMY_CORPS,Mannequin.NONE : GameConfig.IMG_MANNEQUIN}
        Mannequin.MASKS = {Mannequin.LEFT : GameConfig.WALK_LEFT_MASKS_ENEMY_CORPS,Mannequin.RIGHT : GameConfig.WALK_RIGHT_MASKS_ENEMY_CORPS,Mannequin.NONE : GameConfig.MASK_MANNEQUIN}
    
    def advance_state(self):
        self.sprite_count+=1
        if self.sprite_count>= GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_CORPS_A_CORPS*len(Mannequin.IMAGES[self.direction[0]]) :
            self.sprite_count = 0

        self.image = Mannequin.IMAGES[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_CORPS_A_CORPS]
        self.mask = Mannequin.MASKS[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_CORPS_A_CORPS]
        
    def draw(self,window) :
        window.blit(self.image,self.rect.topleft)
        x,y=self.rect.center
        pygame.draw.rect(window, "green", (x-25, y-25, 65 * (self.vie/self.max_vie), 5))
        
    def degat(self,degat):
        if self.vie > 0:
            self.vie-=degat
        elif self.vie < 0:
            self.vie = self.max_vie
    
    def is_touching(self,bat):
        return pygame.sprite.collide_mask(self,bat)
    