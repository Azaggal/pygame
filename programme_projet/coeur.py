import pygame
from game_config import GameConfig

class Coeur (pygame.sprite.Sprite) :
    def __init__(self,ordre) :
        self.x=0
        self.y=0
        self.ordre = ordre
        self.decalage_x =0

    def advance_state(self,Player):
        self.x, self.y = Player.rect.center[0] - self.decalage_x-GameConfig.COEUR_W/2, Player.rect.center[1] - 30

    def draw(self,window):
        window.blit(GameConfig.COEUR,(self.x,self.y))


    def ordonne(self,Player):
        self.decalage_x = ((Player.vie-1)/2-self.ordre)*GameConfig.COEUR_ESPACEMENT