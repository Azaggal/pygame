import pygame
from game_config import *
from random import *
from projectiles import *
from math import atan2


class Enemy_Distance_Rapide (pygame.sprite.Sprite) :
    LEFT = -1
    RIGHT = 1

    UP = -1
    DOWN = 1

    NONE = 0
    #Constructeur
    def __init__(self,x,y) :
        pygame.sprite.Sprite.__init__(self)
        self.direction = [Enemy_Distance_Rapide.NONE,Enemy_Distance_Rapide.NONE]
        self.sprite_count=0
        self.f_b_r = 0
        self.direction_mouv = 0
        self.f_b_fire = 0
        self.projectile = []
        self.max_vie = 5
        self.vie = self.max_vie
        

        self.rect = pygame.Rect( x , 
            y,
            GameConfig.ENEMY_DISTANCE_RAPIDE_W,
            GameConfig.ENEMY_DISTANCE_RAPIDE_H)
        
        self.collision = pygame.Rect( self.rect.bottomleft[0]+35, self.rect.bottomleft[1],GameConfig.PLAYER_COLISSION_W,GameConfig.PLAYER_COLISSION_H)
        
        
        self.image = Enemy_Distance_Rapide.IMAGES[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_DISTANCE_RAPIDE]
        self.mask = Enemy_Distance_Rapide.MASKS[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_DISTANCE_RAPIDE]

        self.vx = 0
        self.vy = 0
        
        

    def init_sprites():
        Enemy_Distance_Rapide.IMAGES = {Enemy_Distance_Rapide.LEFT : GameConfig.WALK_LEFT_IMG_ENEMY_RAPIDE,Enemy_Distance_Rapide.RIGHT : GameConfig.WALK_RIGHT_IMG_ENEMY_RAPIDE,Enemy_Distance_Rapide.NONE : GameConfig.IMG_ENEMY_RAPIDE}
        Enemy_Distance_Rapide.MASKS = {Enemy_Distance_Rapide.LEFT : GameConfig.WALK_LEFT_MASKS_ENEMY_RAPIDE,Enemy_Distance_Rapide.RIGHT : GameConfig.WALK_RIGHT_MASKS_ENEMY_RAPIDE,Enemy_Distance_Rapide.NONE : GameConfig.MASK_ENEMY_RAPIDE}
    
    
    def advance_state(self,x_player,y_player):
        fx=0
        fy=0
        for el in self.projectile:
            el.advance_state()
            if el.is_dead():
                self.projectile.remove(el)
        
        if (self.f_b_r==0):
            self.f_b_r = randint(30,50)
            self.direction_mouv=randint(0,4)
            if self.direction_mouv == 4:
                self.direction_mouv = 0
        if (self.f_b_r>20):
            if self.direction_mouv == 0:
                self.direction[1] = Enemy_Distance_Rapide.UP
                self.direction[0] = Enemy_Distance_Rapide.NONE
                fy= GameConfig.VITESSE_DEPLACEMENT_ENEMY_RAPIDE*Enemy_Distance_Rapide.UP
            elif self.direction_mouv == 2:
                self.direction[1] = Enemy_Distance_Rapide.DOWN
                self.direction[0] = Enemy_Distance_Rapide.NONE
                fy= GameConfig.VITESSE_DEPLACEMENT_ENEMY_RAPIDE*Enemy_Distance_Rapide.DOWN
            elif self.direction_mouv == 3:
                self.direction[1] = Enemy_Distance_Rapide.NONE
                self.direction[0] = Enemy_Distance_Rapide.LEFT
                fx= GameConfig.VITESSE_DEPLACEMENT_ENEMY_RAPIDE*Enemy_Distance_Rapide.LEFT
            elif self.direction_mouv == 1:
                self.direction[1] = Enemy_Distance_Rapide.NONE
                self.direction[0] = Enemy_Distance_Rapide.RIGHT
                fx= GameConfig.VITESSE_DEPLACEMENT_ENEMY_RAPIDE*Enemy_Distance_Rapide.RIGHT

        self.f_b_r=max(self.f_b_r-1,0)
            
        self.sprite_count+=1
        if self.sprite_count>= GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_DISTANCE_RAPIDE*len(Enemy_Distance_Rapide.IMAGES[self.direction[0]]) :
            self.sprite_count = 0

        self.image = Enemy_Distance_Rapide.IMAGES[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_DISTANCE_RAPIDE]
        self.mask = Enemy_Distance_Rapide.MASKS[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_DISTANCE_RAPIDE]

        self.vy = fy*GameConfig.DT
        self.vx = fx*GameConfig.DT

        
        x,y=self.rect.center
        vx_min=-x/GameConfig.DT
        vx_max= (GameConfig.WINDOW_W-GameConfig.ENEMY_DISTANCE_RAPIDE_W-x)/GameConfig.DT
        vy_min=-y/GameConfig.DT
        vy_max = (GameConfig.WINDOW_H-GameConfig.ENEMY_DISTANCE_RAPIDE_H-y)/GameConfig.DT
        
        
        if self.f_b_fire == 0 and (self.direction != [0,0]) and (abs(x-x_player)<=400) and (abs(y-y_player)<=400):
            self.f_b_fire=GameConfig.COULDOWN_ENEMY
            angle = atan2(y_player-y,x_player-x)
            self.projectile.append(Projectile(x,y+30,GameConfig.VITESSE_PROJECTILE,angle))

        self.f_b_fire=max(self.f_b_fire-1,0)


        self.vy=min(self.vy,vy_max)
        self.vy=max(self.vy,vy_min)
        self.vx=min(self.vx,vx_max)
        self.vx=max(self.vx,vx_min)
        
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
        for el in self.projectile :
            el.draw(window)
        x,y=self.rect.center
        pygame.draw.rect(window, "green", (x-30, y-30, 50 * (self.vie/self.max_vie), 5))
    
    def degat(self,degat):
        if self.vie > 0:
            self.vie-=degat
    
    def is_touching(self,bat):
        return pygame.sprite.collide_mask(self,bat)
    