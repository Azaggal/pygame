import pygame
from game_config import *
from random import *
from projectiles import *
from math import atan2,cos,sin


class Enemy_Corps_A_Corps(pygame.sprite.Sprite) :
    LEFT = -1
    RIGHT = 1

    UP = -1
    DOWN = 1

    NONE = 0
    #Constructeur
    def __init__(self,x,y) :
        pygame.sprite.Sprite.__init__(self)
        self.direction = [Enemy_Corps_A_Corps.NONE,Enemy_Corps_A_Corps.NONE]
        self.sprite_count=0
        self.f_b_r = 0
        self.direction_mouv = 0
        self.projectile = []
        self.max_vie = 15
        self.vie = self.max_vie

        self.rect = pygame.Rect( x , 
            y,
            GameConfig.ENEMY_CORPS_A_CORPS_W,
            GameConfig.ENEMY_CORPS_A_CORPS_H)
        
        self.collision = pygame.Rect( self.rect.bottomleft[0]+35 , self.rect.bottomleft[1],GameConfig.PLAYER_COLISSION_W,GameConfig.PLAYER_COLISSION_H)
        
        
        self.image = Enemy_Corps_A_Corps.IMAGES[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_CORPS_A_CORPS]
        self.mask = Enemy_Corps_A_Corps.MASKS[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_CORPS_A_CORPS]

        self.vx = 0
        self.vy = 0
        

    def init_sprites():
        Enemy_Corps_A_Corps.IMAGES = {Enemy_Corps_A_Corps.LEFT : GameConfig.WALK_LEFT_IMG_ENEMY_CORPS,Enemy_Corps_A_Corps.RIGHT : GameConfig.WALK_RIGHT_IMG_ENEMY_CORPS,Enemy_Corps_A_Corps.NONE : GameConfig.IMG_ENEMY_CORPS}
        Enemy_Corps_A_Corps.MASKS = {Enemy_Corps_A_Corps.LEFT : GameConfig.WALK_LEFT_MASKS_ENEMY_CORPS,Enemy_Corps_A_Corps.RIGHT : GameConfig.WALK_RIGHT_MASKS_ENEMY_CORPS,Enemy_Corps_A_Corps.NONE : GameConfig.MASK_ENEMY_CORPS}
    
    def advance_state(self,x_player,y_player):
        fx=0
        fy=0
        x,y=self.rect.center
        angle = atan2(y_player-y,x_player-x)
        

        self.sprite_count+=1
        if self.sprite_count>= GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_CORPS_A_CORPS*len(Enemy_Corps_A_Corps.IMAGES[self.direction[0]]) :
            self.sprite_count = 0

        self.image = Enemy_Corps_A_Corps.IMAGES[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_CORPS_A_CORPS]
        self.mask = Enemy_Corps_A_Corps.MASKS[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_CORPS_A_CORPS]

        self.vx = cos(angle)*GameConfig.VITESSE_DEPLACEMENT_ENEMY_CORPS_A_CORPS
        self.vy = sin(angle)*GameConfig.VITESSE_DEPLACEMENT_ENEMY_CORPS_A_CORPS
        
        if (abs(x-x_player)<=400) and (abs(y-y_player)<=400) :
            self.collision = self.collision.move(self.vx*GameConfig.DT,0)
            touche = False

            for mur in Map.Mur :

                if self.collision.colliderect(mur):
                    touche = True
                    break
            if touche :
                self.collision = self.collision.move(-self.vx*GameConfig.DT,0)
                
            else :
                self.rect = self.rect.move(self.vx*GameConfig.DT,0)


            self.collision = self.collision.move(0,self.vy*GameConfig.DT)
            touche = False

            for mur in Map.Mur :

                if self.collision.colliderect(mur):
                    touche = True
                    break
            if touche :
                self.collision = self.collision.move(0,-self.vy*GameConfig.DT)
                
            else :
                self.rect = self.rect.move(0,self.vy*GameConfig.DT)
        
    def draw(self,window) :
        window.blit(self.image,self.rect.topleft)
        x,y=self.rect.center
        pygame.draw.rect(window, "green", (x-30, y-30, 50 * (self.vie/self.max_vie), 5))
        
    def degat(self,degat):
        if self.vie > 0:
            self.vie-=degat
    
    def is_touching(self,bat):
        return pygame.sprite.collide_mask(self,bat)
    