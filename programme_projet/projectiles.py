import pygame
from game_config import *
from math import pi, cos, sin
from map import *

class Projectile (pygame.sprite.Sprite):
    LEFT=-1
    RIGHT=1
    UP = 1
    DOWN = -1
    #Constructeur
    def __init__(self,x,y,v,angle,arme=0,degat=0) :
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect( x , y, GameConfig.PROJECTILE_W, GameConfig.PROJECTILE_H)
        if angle < -pi:
            angle = -pi
        elif angle > pi:
            angle = pi

        stats = GameConfig.STAT_ARME[arme]
        self.angle = angle
        self.sprite_count=0
        self.degat = stats['degat']+degat
        self.degat_supp = degat
        self.distance = 20 *stats['distance']
        self.vitesse = stats['vitesse_projectile']*v
        self.arme = arme
        self.direction = [0,0]

        

        
        if 0 <= abs(angle) < pi/2:
            self.direction[0] = Projectile.RIGHT
        elif pi/2 < abs(angle) <= pi :
            self.direction[0] = Projectile.LEFT

        if -pi < angle < 0 :
            self.direction[1] = Projectile.UP
        elif 0 < angle < pi :
            self.direction[1] = Projectile.DOWN

        self.image = Projectile.IMAGES[self.arme][(self.direction[0],self.direction[1])]
        self.mask = Projectile.MASKS[1][0]
    
    def advance_state(self):
        self.distance-=1
        self.sprite_count+=1
        if self.sprite_count>= GameConfig.NB_FRAMES_PER_SPRITE_PROJECTILE*len(Projectile.IMAGES[self.direction[0]]) :
            self.sprite_count = 0
        self.image = self.teinter(Projectile.IMAGES[self.arme][(self.direction[0],self.direction[1])])
        self.mask = Projectile.MASKS[1][0]
        
        
        
        self.rect = self.rect.move(cos(self.angle)*self.vitesse*GameConfig.DT,sin(self.angle)*self.vitesse*GameConfig.DT)
         

    def init_sprites():
        Projectile.IMAGES = GameConfig.PROJECTILES
        Projectile.MASKS = {Projectile.LEFT : GameConfig.FLYING_FROM_LEFT_MASK,Projectile.RIGHT : GameConfig.FLYING_FROM_RIGHT_MASK}

    def teinter(self,surface):
        tinted_surface = surface.copy()
        red_overlay = pygame.Surface(surface.get_size(),pygame.SRCALPHA)   
        red_overlay.fill((255, 255-self.degat_supp*30, 255-self.degat*30))  # Ajouter de la transparence avec alpha
        tinted_surface.blit(red_overlay, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return tinted_surface

    def draw(self,window):
        window.blit(self.image,self.rect.topleft)
    
    def is_dead(self):
        for mur in Map.Mur :
            if self.rect.colliderect(mur):
                return True
        return False
        #return (self.rect.left>GameConfig.WINDOW_W) or (self.rect.right<0) or (self.rect.bottom < 0) or (self.rect.top>GameConfig.WINDOW_H)
    
