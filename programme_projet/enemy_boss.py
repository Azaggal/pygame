import pygame
from game_config import *
from random import *
from projectiles import *
from math import atan2
from enemy_corps_a_corps import *
from enemy_distance_lent import *
from enemy_distance_rapide import *


class Enemy_Boss (pygame.sprite.Sprite) :
    LEFT = -1
    RIGHT = 1

    UP = -1
    DOWN = 1

    NONE = 0
    #Constructeur
    def __init__(self,x,y) :
        pygame.sprite.Sprite.__init__(self)
        self.direction = [Enemy_Boss.NONE,Enemy_Boss.NONE]
        self.sprite_count=0
        self.f_b_r = 0
        self.direction_mouv = 0
        self.projectile = []
        self.max_vie = 40
        self.vie = 100
        self.couldown = 200
        self.attaque0_couldown = 400
        self.attaque1_couldown = 200
        self.attaque2_couldown = 200
        self.attaque2bis_couldown = 200
        self.attaque4_couldown = 100
        self.attaque = 4

        self.rect = pygame.Rect( x , 
            y,
            GameConfig.ENEMY_BOSS_W,
            GameConfig.ENEMY_BOSS_H)
        
        self.collision = pygame.Rect( self.rect.bottomleft[0]+GameConfig.PLAYER_W/2-GameConfig.PLAYER_COLISSION_W/2 , self.rect.bottomleft[1]-GameConfig.PLAYER_COLISSION_H,GameConfig.PLAYER_COLISSION_W,GameConfig.PLAYER_COLISSION_H)
        
        
        self.image = Enemy_Boss.IMAGES[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_CORPS_A_CORPS]
        self.mask = Enemy_Boss.MASKS[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_CORPS_A_CORPS]

        self.vx = 0
        self.vy = 0
        


    def init_sprites():
        Enemy_Boss.IMAGES = {Enemy_Boss.LEFT : GameConfig.WALK_LEFT_IMG_ENEMY_CORPS,Enemy_Boss.RIGHT : GameConfig.WALK_RIGHT_IMG_ENEMY_CORPS,Enemy_Boss.NONE : GameConfig.IMG_ENEMY_CORPS}
        Enemy_Boss.MASKS = {Enemy_Boss.LEFT : GameConfig.WALK_LEFT_MASKS_ENEMY_CORPS,Enemy_Boss.RIGHT : GameConfig.WALK_RIGHT_MASKS_ENEMY_CORPS,Enemy_Boss.NONE : GameConfig.MASK_ENEMY_CORPS}
  
    def advance_state(self,x_player,y_player,list_enemy):
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
                self.direction[1] = Enemy_Boss.UP
                self.direction[0] = Enemy_Boss.NONE
                fy= GameConfig.VITESSE_DEPLACEMENT_ENEMY_BOSS*Enemy_Boss.UP
            elif self.direction_mouv == 2:
                self.direction[1] = Enemy_Boss.DOWN
                self.direction[0] = Enemy_Boss.NONE
                fy= GameConfig.VITESSE_DEPLACEMENT_ENEMY_BOSS*Enemy_Boss.DOWN
            elif self.direction_mouv == 3:
                self.direction[1] = Enemy_Boss.NONE
                self.direction[0] = Enemy_Boss.LEFT
                fx= GameConfig.VITESSE_DEPLACEMENT_ENEMY_BOSS*Enemy_Boss.LEFT
            elif self.direction_mouv == 1:
                self.direction[1] = Enemy_Boss.NONE
                self.direction[0] = Enemy_Boss.RIGHT
                fx= GameConfig.VITESSE_DEPLACEMENT_ENEMY_BOSS*Enemy_Boss.RIGHT

        self.f_b_r=max(self.f_b_r-1,0)
            
        self.sprite_count+=1
        if self.sprite_count>= GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_BOSS*len(Enemy_Boss.IMAGES[self.direction[0]]) :
            self.sprite_count = 0

        self.image = Enemy_Boss.IMAGES[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_BOSS]
        self.mask = Enemy_Boss.MASKS[self.direction[0]][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_ENEMY_BOSS]

        self.vy = fy*GameConfig.DT
        self.vx = fx*GameConfig.DT

        
        x,y=self.rect.center
    
        self.angle = atan2(y_player-y,x_player-x)
        
        if self.couldown == 0:
            if self.attaque == 1:
                self.attaque = 2
                self.couldown = self.attaque2_couldown
            elif self.attaque == 2:
                self.attaque = 3
                self.couldown = self.attaque2bis_couldown
            elif self.attaque == 3:
                self.attaque = 4
                self.couldown = self.attaque4_couldown
            elif self.attaque == 4:
                self.attaque = 0
                self.couldown = self.attaque0_couldown
            elif self.attaque == 0:
                self.attaque = 1
                self.couldown = self.attaque1_couldown
        if self.attaque == 0:
            if self.couldown % 30 == 0:
                self.projectile.append(Projectile(x,y+30,GameConfig.VITESSE_PROJECTILE,self.angle))
        elif self.attaque == 1:
            if self.couldown % 80 == 0:
                self.attaque_1()
        elif self.attaque == 2:
            if self.couldown % 10 == 0:
                angle = -pi + 2*pi/self.attaque2_couldown*self.couldown
                self.attaque_2(angle)
        elif self.attaque == 3:
            if self.couldown % 10 == 0:
                angle = -pi + 2*pi/self.attaque2bis_couldown*self.couldown
                self.attaque_2(angle)
        elif self.attaque == 4:
            if self.couldown == self.attaque4_couldown :
                self.attaque_4(list_enemy)
        self.couldown -=1


        self.vx = cos(self.angle)*(GameConfig.VITESSE_DEPLACEMENT_ENEMY_BOSS)*fx
        self.vy = sin(self.angle)*(GameConfig.VITESSE_DEPLACEMENT_ENEMY_BOSS)*fy


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
    
    
    def attaque_1(self):
        x,y=self.rect.center
        self.projectile.append(Projectile(x,y+30,GameConfig.VITESSE_PROJECTILE,0))
        for i in range(1,9):
            self.projectile.append(Projectile(x,y+30,GameConfig.VITESSE_PROJECTILE,i*pi/8))
        for i in range(1,8):
            self.projectile.append(Projectile(x,y+30,GameConfig.VITESSE_PROJECTILE,-i*pi/8))

        
    def attaque_2(self,angle):
        x,y=self.rect.center
        self.projectile.append(Projectile(x,y+30,GameConfig.VITESSE_PROJECTILE,angle))

    def attaque_4(self,list_enemy):
        enemy1 = randint(0,3)
        enemy2 = randint(0,3)
        if enemy1 == 0:
            list_enemy.append(Enemy_Distance_Lent(self.rect.x-50,self.rect.y))
        elif enemy1 == 1:
            list_enemy.append(Enemy_Corps_A_Corps(self.rect.x-50,self.rect.y))
        else :
            list_enemy.append(Enemy_Distance_Rapide(self.rect.x-50,self.rect.y))

        if enemy2 == 0:
            list_enemy.append(Enemy_Distance_Lent(self.rect.x+50,self.rect.y))
        elif enemy2 == 1:
            list_enemy.append(Enemy_Corps_A_Corps(self.rect.x+50,self.rect.y))
        else :
            list_enemy.append(Enemy_Distance_Rapide(self.rect.x+50,self.rect.y))

        
        
        
    def draw(self,window) :
        window.blit(self.image,self.rect.topleft)
        for el in self.projectile :
            el.draw(window)

        pygame.draw.rect(window, "green", (GameConfig.WINDOW_W/2-380, 0, 300 * (self.vie/self.max_vie), 30))

    def degat(self,degat):
        if self.vie > 0:
            self.vie-=degat
        else : 
            self.mort()
    
    def is_touching(self,bat):
        return pygame.sprite.collide_mask(self,bat)
    