import pygame
from game_config import *
from projectiles import *
from math import atan2,cos,sin
from coeur import Coeur
from personnage import *
from map import *
from items import *
from armes import *
from table import Table
from trappe import Trappe

class Player (pygame.sprite.Sprite) :
    LEFT = -1
    RIGHT = 1

    UP = -1
    DOWN = 1

    NONE = 0
    #Constructeur
    def __init__(self,x,y) :
        pygame.sprite.Sprite.__init__(self)
        self.direction = [Player.RIGHT,Player.RIGHT]
        self.sprite_count=0
        self.projectile = []
        self.f_b_fire = 0
        self.f_b_touch = 0
        self.angle = 0
        self.attaque = 0
        self.text_surface = False
        self.saut = 90
        self.trappe_x,self.trappe_y = GameConfig.TRAPPE_X,GameConfig.TRAPPE_Y
        self.pause= False
        self.arme = 0
        self.cadence_arme = GameConfig.STAT_ARME[self.arme]['couldown']
        self.bouclier = 0
        self.vitesse = 1
        self.role = 1
        self.vie = GameConfig.STAT_PERSONNAGE[self.role][0]
        self.coeur = []
        self.direction_tire=[0,0]
        self.idle = True

        

        for i in range(self.vie): #A Changer, simplifiable
            self.coeur.append(Coeur(i))
            self.coeur[i].ordonne(self)

        self.rect = pygame.Rect( x , y,GameConfig.PLAYER_W,GameConfig.PLAYER_H)

        self.collision = pygame.Rect( self.rect.bottomleft[0]+GameConfig.PLAYER_W/2-GameConfig.PLAYER_COLISSION_W/2 , self.rect.bottomleft[1]-GameConfig.PLAYER_COLISSION_H,GameConfig.PLAYER_COLISSION_W,GameConfig.PLAYER_COLISSION_H)
        
        self.image = Player.IMAGES[self.idle][self.role][self.direction[0]]
        self.mask = Player.MASKS[self.idle][self.role][self.direction[0]]

        self.vx = 0
        self.vy = 0

        self.item_vitesse_player = 0
        self.item_vitesse_proj = 0
        self.item_cadence = 0
        self.item_degats_proj = 0
        
        
        self.mask=GameConfig.STANDING_MASK_MAGE

    def init_sprites():
        Player.IMAGES = {False : GameConfig.WALK_IMG,True : GameConfig.STANDING_IMG_MAIN}
        Player.MASKS = {False : GameConfig.WALK_MASK,True : GameConfig.STANDING_MASK_MAIN}
        Player.ICONES = GameConfig.ICONES
        Player.SAUT = GameConfig.MAIN_SAUT

    def advance_state(self,next_move):

        fx=0
        fy=0

        self.idle = True
        


        for el in self.projectile:
            el.advance_state()
            if el.is_dead():
                self.projectile.remove(el)

        if self.saut != 90 and 45 >= self.saut  :
            self.anim_saut = Player.SAUT[self.role][self.direction[0]][self.saut//3]

        else :
            if next_move.up :
                self.direction[1] = Player.UP
                fy= 1
                self.idle = False
            elif next_move.down :
                self.direction[1] = Player.DOWN
                fy= 1
                self.idle = False


            if next_move.left :
                self.direction[0] = Player.LEFT
                fx= 1
                self.idle = False
            elif next_move.right:
                self.direction[0] = Player.RIGHT
                fx= 1
                self.idle = False



        if next_move.fire_up :
            self.direction_tire[1] = Player.UP
        elif next_move.fire_down:
            self.direction_tire[1] = Player.DOWN
        else :
            self.direction_tire[1] = Player.NONE


        if next_move.fire_left :
            self.direction_tire[0] = Player.LEFT
        elif next_move.fire_right:
            self.direction_tire[0] = Player.RIGHT
        else :
            self.direction_tire[0] = Player.NONE

        
       
        self.angle=atan2(self.direction[1],self.direction[0])
        
        
        

        if self.idle==True :
            self.image = Player.IMAGES[self.idle][self.role][self.direction[0]]
            self.mask = Player.MASKS[self.idle][self.role][self.direction[0]]
            self.mask =Player.MASKS[True][0][1]
            self.sprite_count = 0
        else :
            self.sprite_count+=1
            if self.sprite_count>= GameConfig.NB_FRAMES_PER_SPRITE_PLAYER*len(Player.IMAGES[False][self.direction[0]][0])  :
                self.sprite_count = 0
            self.image = Player.IMAGES[self.idle][self.direction[0]][self.role][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]
            self.mask = Player.MASKS[self.idle][self.direction[0]][self.role][self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]

        x,y=self.rect.topleft

        if (self.f_b_fire==0) and (self.direction_tire != [0,0]) :
            self.attaque = 1 - self.attaque
            self.f_b_fire=(GameConfig.COULDOWN/self.cadence_arme + self.item_cadence)
             
            self.projectile.append(Projectile(x+30*self.direction_tire[0]+GameConfig.PLAYER_W/2+10*self.attaque*abs(self.direction_tire[1])-GameConfig.PROJECTILE_W/2
                                              ,y+35*self.direction_tire[1]+10*self.attaque*abs(self.direction_tire[0])+GameConfig.PROJECTILE_H/2+GameConfig.PLAYER_H/2
                                              ,(GameConfig.VITESSE_PROJECTILE + self.item_vitesse_proj),atan2(self.direction_tire[1],self.direction_tire[0]),self.arme,GameConfig.DEGAT_JOUEUR+self.item_degats_proj))

        self.f_b_fire=max(self.f_b_fire-1,0)
        self.saut = min(self.saut+1,90)


        vx_min=-x/GameConfig.DT
        vx_max= (GameConfig.WINDOW_W-GameConfig.PLAYER_W-x)/GameConfig.DT
        vy_min=-y/GameConfig.DT
        vy_max = (GameConfig.WINDOW_H-GameConfig.PLAYER_H-y)/GameConfig.DT


        
        self.vx = cos(self.angle)*(GameConfig.VITESSE_DEPLACEMENT_JOUEUR+self.item_vitesse_player+4*self.vitesse)*fx
        self.vy = sin(self.angle)*(GameConfig.VITESSE_DEPLACEMENT_JOUEUR+self.item_vitesse_player+self.vitesse)*fy

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
    


        self.f_b_touch=max(self.f_b_touch-1,0)

        for coeur in self.coeur:
            coeur.advance_state(self)

                
        

    def draw(self,window) :

        if 70 > self.saut  :
            x,y = self.rect.topleft
            x_fin = self.trappe_x - 34
            y_fin = self.trappe_y -71
            if self.role == 0 :
                y_fin -=9
                x_fin-=4
            if self.direction[0] == -1 :
                x_fin -=10
                x-=2
            if 9 >= self.saut  :      
                window.blit(self.anim_saut,(x+30,y+50))

            elif 24 >= self.saut  :
                vitesse = 2      
                window.blit(self.anim_saut,(x+30+(x_fin-x)/15**vitesse*(self.saut-9)**vitesse,y+50+(y_fin-y)/15**vitesse*(self.saut-9)**vitesse))

            elif 45 >= self.saut :
                window.blit(self.anim_saut,(30+x_fin,50+y_fin))

            
        else :
            window.blit(self.tint_red(self.image),self.rect.topleft)
        
        

            for el in self.projectile :
                el.draw(window)

            for coeur in self.coeur :
                coeur.draw(window)

            

            

            if self.direction[0]==1:
                x,y = self.rect.topleft
                x,y = x-2+GameConfig.PLAYER_W/2-GameConfig.MAIN_W, y+70
                x_main,y_main = x,y
                x_arme = x+12-GameConfig.TAILLE_ARME[self.arme][0]/2
                x_bouclier = x - GameConfig.TAILLE_BOUCLIER[self.bouclier][0]/2+ 45

            else :
                x,y = self.rect.topright 
                x,y = x+2-GameConfig.PLAYER_W/2, y+70
                x_main,y_main = x,y
                x_arme = x-12-GameConfig.TAILLE_ARME[self.arme][0]/2+GameConfig.MAIN_W
                x_bouclier = x - GameConfig.TAILLE_BOUCLIER[self.bouclier][0]/2 +GameConfig.MAIN_W- 45

            
            
            if self.direction_tire != [0,0] and self.f_b_fire == (GameConfig.COULDOWN/self.cadence_arme+ self.item_cadence)-1:
                self.direction_attaque = (self.direction_tire[0],self.direction_tire[1])



            x,y = self.rect.topleft
            if self.f_b_fire != 0 :
                if self.direction_attaque == (1,0):
                    x=x+60
                    y+=70 - GameConfig.TAILLE_ARME[self.arme][1]/2
                    
                elif self.direction_attaque == (-1,0):
                    x=x+20 - GameConfig.TAILLE_ARME[self.arme][1]
                    y+=70 - GameConfig.TAILLE_ARME[self.arme][1]/2

                elif self.direction_attaque == (0,-1):
                    x=x+60 - GameConfig.TAILLE_ARME[self.arme][1]
                    y+=40 - GameConfig.TAILLE_ARME[self.arme][1]

                elif self.direction_attaque == (0,1):
                    x=x+70 - GameConfig.TAILLE_ARME[self.arme][1]
                    y+=80

                elif self.direction_attaque == (1,-1):
                    x=x+30
                    y+= 20 - GameConfig.TAILLE_ARME[self.arme][1]/2

                elif self.direction_attaque == (-1,-1):
                    x+= 10 - GameConfig.TAILLE_ARME[self.arme][1]
                    y+=40 - GameConfig.TAILLE_ARME[self.arme][1]

                elif self.direction_attaque == (1,1):
                    x+=40
                    y+=55
                
                elif self.direction_attaque == (-1,1):
                    x+=30 - GameConfig.TAILLE_ARME[self.arme][1]
                    y+=70

            
            if (GameConfig.COULDOWN/self.cadence_arme + self.item_cadence)-self.f_b_fire <= 3 :
                
                window.blit(GameConfig.ATTAQUE[self.arme][self.direction_attaque][self.attaque][0],(x,y))

            elif 3 < (GameConfig.COULDOWN/self.cadence_arme + self.item_cadence)-self.f_b_fire <= 6 :

                window.blit(GameConfig.ATTAQUE[self.arme][self.direction_attaque][self.attaque][1],(x,y))
                
            else :
                

                frame = self.sprite_count//GameConfig.NB_FRAMES_PER_SPRITE_PLAYER
                if frame == 1 or frame == 4:
                    y_main-=4
                elif frame == 2 or frame == 5:
                    y_main-=2


                y_arme = y_main-GameConfig.TAILLE_ARME[self.arme][1]+25
                
                window.blit(self.teinter_arme(GameConfig.ARMES[self.arme][self.direction[0]]),(x_arme,y_arme))
                window.blit(GameConfig.MAINS[self.direction[0]],(x_main,y_main))

            window.blit(GameConfig.BOUCLIER[self.bouclier],(x_bouclier,y_main))    
                
            
                
            
            if self.text_surface :
                x,y = self.text_surface[0]
                
                if isinstance(self.text_surface[1],Table):
                    window.blit(GameConfig.INTERACTION,(x-50,y-50))

                elif isinstance(self.text_surface[1],Trappe):
                    window.blit(GameConfig.INTERACTION_TRAPPE,(x-50,y-70))

                else :
                    for i in range(len(self.text_surface[2])):
                        window.blit(self.text_surface[2][i],(x+(-20)*(1-i),y))
            

    def is_touching(self,projectile):
        if pygame.sprite.collide_mask(self,projectile) :
            if (self.f_b_touch==0):
                self.f_b_touch=GameConfig.TEMPS_INVULNERABLE
                self.degat()
            return True
        return False

    def soin(self):
        self.coeur.append(Coeur(self.vie))
        self.vie += 1
        self.ordonne()

    def degat(self):
        if self.vie > 0:
            self.vie-=1
            self.coeur.pop()
            self.ordonne()

    def soinXfois(self,x):
        for i in range(x):
            self.soin()
    
    def ordonne(self):
        for coeur in self.coeur:
            coeur.ordonne(self)

    def teinter_arme(self,surface):
        tinted_surface = surface.copy()
        red_overlay = pygame.Surface(surface.get_size(),pygame.SRCALPHA)   
        red_overlay.fill((255, 255-self.item_degats_proj*50, 255-self.item_degats_proj*50))  # Ajouter de la transparence avec alpha
        tinted_surface.blit(red_overlay, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return tinted_surface
    
    def tint_red(self,surface):
        if self.f_b_touch > 0:
            tinted_surface = surface.copy()
            red_overlay = pygame.Surface(surface.get_size(),pygame.SRCALPHA)   
            red_overlay.fill((255, 255-(self.f_b_touch*255/GameConfig.TEMPS_INVULNERABLE), 255-(self.f_b_touch*255/GameConfig.TEMPS_INVULNERABLE)))  # Ajouter de la transparence avec alpha
            tinted_surface.blit(red_overlay, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            return tinted_surface
        return surface
    
                
    
    def icone(self,element):
        icones = Player.ICONES
        if isinstance(element, Items):
            if element.vitesse_player != 0:
                return [icones['vert']['vitesse_joueur']]
            elif element.vitesse_proj != 0:
                return [icones['vert']['vitesse_projectile']]
            elif element.cadence != 0:
                return [icones['vert']['couldown']]
            elif element.vie != 0:
                return [icones['vert']['vie']]
            elif element.degats_proj !=0:
                return [icones['vert']['degat']]

        elif isinstance(element, Personnage):
            if element.numero == 0:
                return [icones['blanc']['vie'],icones['blanc']['vitesse_joueur']]
            elif element.numero == 1:
                return [icones['vert']['vie'],icones['rouge']['vitesse_joueur']]
            else :
                return [icones['rouge']['vie'],icones['vert']['vitesse_joueur']]

        elif isinstance(element, Arme) :  
            liste_icone = []
            basique = GameConfig.STAT_BASIQUE
            for cle,value in GameConfig.STAT_ARME[element.numero].items():
                if basique[cle] < value:
                    liste_icone.append(icones['vert'][cle])
                elif basique[cle] > value:
                    liste_icone.append(icones['rouge'][cle])
                else :
                    liste_icone.append(icones['blanc'][cle])
            return liste_icone

        
        else :
            return []
        

    def chg_stat(self,personnage):
        self.vie = GameConfig.STAT_PERSONNAGE[personnage.numero][0]
        self.coeur = []
        for i in range(self.vie): #A Changer, simplifiable
            self.coeur.append(Coeur(i))
            self.coeur[i].ordonne(self)

        self.vitesse = GameConfig.STAT_PERSONNAGE[personnage.numero][1]


    def position(self,x,y):
        self.rect.x = x
        self.rect.y = y
        self.collision.x = self.rect.bottomleft[0]+GameConfig.PLAYER_W/2-GameConfig.PLAYER_COLISSION_W/2
        self.collision.y = self.rect.bottomleft[1]-GameConfig.PLAYER_COLISSION_H

