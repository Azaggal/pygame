import pygame
from player import *
from game_config import *
from math import sqrt

class Guide_Reprendre(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect( x, y, 50, 49)

        self.image = GameConfig.BOUTON_CONTINUER
        
        self.x = x
        self.y = y


        self.animation = 0
        
        self.pause = True

        self.page = ''

    def arrivee(self):
        self.animation = min(self.animation+1,10)
        self.x = self.rect.x + -100*(self.animation/10)**2

        
    def depart(self):
        self.animation = max(self.animation-1,0)
        self.x = self.rect.x + -100*(self.animation/10)**2


    def draw(self,window):
        if self.rect.collidepoint(pygame.mouse.get_pos()) :
            self.arrivee()
        else :
            self.depart()
        window.blit(self.image,(self.x,self.y))

    
    def clique(self):
        self.pause = False


class Guide_1(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect( x, y, 50, 49)
        self.image = GameConfig.BOUTON_1
        self.x = x
        self.y = y

        self.animation = 0
        self.page = 'Arme'

    def arrivee(self):
        self.animation = min(self.animation+1,10)
        self.x = self.rect.x + -90*(self.animation/10)**2-4

        
    def depart(self):
        self.animation = max(self.animation-1,0)
        self.x = self.rect.x + -90*(self.animation/10)**2-4


    def draw(self,window):
        if self.rect.collidepoint(pygame.mouse.get_pos()) :
            self.arrivee()
        else :
            self.depart()
        window.blit(self.image,(self.x,self.y))

class Guide_Deplacement(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect( x, y, 50, 49)
        self.image = GameConfig.BOUTON_DEPLACEMENT
        self.x = x
        self.y = y

        self.animation = 0
        self.page = 'Arme'

    def arrivee(self):
        self.animation = min(self.animation+1,10)
        self.x = self.rect.x + -97*(self.animation/10)**2-2

        
    def depart(self):
        self.animation = max(self.animation-1,0)
        self.x = self.rect.x + -97*(self.animation/10)**2-2


    def draw(self,window):
        if self.rect.collidepoint(pygame.mouse.get_pos()) :
            self.arrivee()
        else :
            self.depart()
        window.blit(self.image,(self.x,self.y))


class Guide_Commandes(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect( x, y, 50, 49)
        self.image = GameConfig.BOUTON_COMMANDES
        self.x = x
        self.y = y

        self.animation = 0
        self.page = 'Arme'

    def arrivee(self):
        self.animation = min(self.animation+1,10)
        self.x = self.rect.x + -100*(self.animation/10)**2+2

        
    def depart(self):
        self.animation = max(self.animation-1,0)
        self.x = self.rect.x + -100*(self.animation/10)**2+2


    def draw(self,window):
        if self.rect.collidepoint(pygame.mouse.get_pos()) :
            self.arrivee()
        else :
            self.depart()
        window.blit(self.image,(self.x,self.y))


class Guide_Arme(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect( x, y, 50, 50)
        self.image = GameConfig.BOUTON_ARME
        self.x = x
        self.y = y

        self.animation = 0
        self.page = 'Arme'

    def arrivee(self):
        self.animation = min(self.animation+1,10)
        self.x = self.rect.x + 100*(self.animation/10)**2 -92

        
    def depart(self):
        self.animation = max(self.animation-1,0)
        self.x = self.rect.x + 100*(self.animation/10)**2 -92


    def draw(self,window):
        if self.rect.collidepoint(pygame.mouse.get_pos()) :
            self.arrivee()
        else :
            self.depart()
        window.blit(self.image,(self.x,self.y))


class Guide_Enemies(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect( x, y, 50, 49)
        self.image = GameConfig.BOUTON_ENEMIES
        self.x = x
        self.y = y

        self.animation = 0
        self.page = 'Arme'

    def arrivee(self):
        self.animation = min(self.animation+1,10)
        self.x = self.rect.x + 100*(self.animation/10)**2 -89

        
    def depart(self):
        self.animation = max(self.animation-1,0)
        self.x = self.rect.x + 100*(self.animation/10)**2 -89


    def draw(self,window):
        if self.rect.collidepoint(pygame.mouse.get_pos()) :
            self.arrivee()
        else :
            self.depart()
        window.blit(self.image,(self.x,self.y))

class Guide_Potions(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect( x, y, 50, 49)
        self.image = GameConfig.BOUTON_POTIONS
        self.x = x
        self.y = y

        self.animation = 0
        self.page = 'Arme'

    def arrivee(self):
        self.animation = min(self.animation+1,10)
        self.x = self.rect.x + 100*(self.animation/10)**2 -83

        
    def depart(self):
        self.animation = max(self.animation-1,0)
        self.x = self.rect.x + 100*(self.animation/10)**2 -83


    def draw(self,window):
        if self.rect.collidepoint(pygame.mouse.get_pos()) :
            self.arrivee()
        else :
            self.depart()
        window.blit(self.image,(self.x,self.y))

class Guide_Personnages(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect( x, y, 50, 49)
        self.image = GameConfig.BOUTON_PERSONNAGES
        self.x = x
        self.y = y

        self.animation = 0
        self.page = 'Arme'

    def arrivee(self):
        self.animation = min(self.animation+1,10)
        self.x = self.rect.x + 100*(self.animation/10)**2 -71

        
    def depart(self):
        self.animation = max(self.animation-1,0)
        self.x = self.rect.x + 100*(self.animation/10)**2 -71


    def draw(self,window):
        if self.rect.collidepoint(pygame.mouse.get_pos()) :
            self.arrivee()
        else :
            self.depart()
        window.blit(self.image,(self.x,self.y))
