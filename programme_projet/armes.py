import pygame
from player import *
from game_config import *

class Arme(pygame.sprite.Sprite) :
    def __init__(self,x,y,numero) :
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.numero = numero

        self.rect = pygame.Rect( x-GameConfig.TAILLE_ARME[numero][0] , y-GameConfig.TAILLE_ARME[numero][1] ,GameConfig.TAILLE_ARME[numero][0],GameConfig.TAILLE_ARME[numero][1])

        self.image = GameConfig.ARMES[numero][1]


    def draw(self,window):
        window.blit(self.image,self.rect.center)

    def changer_arme(self,numero):
        self.numero = numero
        self.rect = pygame.Rect( self.x-GameConfig.TAILLE_ARME[numero][0] , self.y-GameConfig.TAILLE_ARME[numero][1],GameConfig.TAILLE_ARME[numero][0],GameConfig.TAILLE_ARME[numero][1])
        self.image = GameConfig.ARMES[numero][1]

    
