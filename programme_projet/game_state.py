from player import *
from game_config import *
from random import *
from enemy_distance_lent import *
from enemy_distance_rapide import *
from items import * 
from enemy_corps_a_corps import *
from enemy_boss import *
import pytmx
from armes import *
from mort import *
from pause import *
from personnage import *
from trappe import *
from table import *
from mannequin import *
from map import *

class GameState :
    
    #Constructeur
    def __init__(self) :
        self.player=Player(428,480)
        self.enemy=[] 
        self.mort=[]
        self.menu=[]
        self.anim_mort = 0
        self.pages_images = {'Arme' : GameConfig.GUIDE_ARME,'Commandes' : GameConfig.GUIDE_COMMANDES,'Enemies' : GameConfig.GUIDE_ENEMIES,'Personnages' : GameConfig.GUIDE_PERSONNAGES,'Potions' : GameConfig.GUIDE_POTIONS,'Important' : GameConfig.GUIDE_IMPORTANT}
        self.page = 'Important'
        self.pause = False
        self.personnages = [Personnage(832,504,0),Personnage(832,350,2)]
        self.objet_depart=[Arme(128,480,1),Arme(128,328,2),Table(608,240)]
        self.items_tab = []
        
        self.trappe = Trappe(GameConfig.TRAPPE_X, GameConfig.TRAPPE_Y)
        self.table = Table(608,240)
        self.mannequin = [Mannequin(264,208)]
        self.f_b_r = 60
        self.list_items = [Items(GameConfig.ITEM_VITESSE_X,GameConfig.ITEM_VITESSE_Y,5,0,0,0,0),
                          Items(GameConfig.ITEM_VITESSE_PROJ_X,GameConfig.ITEM_VITESSE_PROJ_Y,0,5,0,0,0),
                          Items(GameConfig.ITEM_CADENCE_X,GameConfig.ITEM_CADENCE_Y,0,0,5,0,0),
                          Items(GameConfig.ITEM_VIE_X,GameConfig.ITEM_VIE_Y,0,0,0,2,0),
                          Items(GameConfig.ITEM_DEGATS_X,GameConfig.ITEM_DEGATS_Y,0,0,0,0,2)]

        #self.obstacles = [self.objet_depart[2]]

    def draw(self,window,tmx_data):
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):  # Vérifie si le calque est une couche de tuiles
                for x, y, gid in layer:  # Parcourt chaque tuile
                    tile = tmx_data.get_tile_image_by_gid(gid)  # Récupère l'image de la tuile
                    if tile:  # Si une tuile existe à cette position
                        # Dessiner la tuile sur la fenêtre
                        window.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))


        for objet in self.items_tab:
            objet.draw(window)

        for personnage in self.personnages :
            personnage.draw(window)
        
        for objet in self.objet_depart:
            objet.draw(window)
        
        self.trappe.draw(window)

        for corps in self.mort:
            corps.draw(window)
        
        for mannequin in self.mannequin:
            mannequin.draw(window)

        for objet in self.items_tab:
            objet.draw(window)

        self.player.draw(window)

        for enemy in self.enemy:
            enemy.draw(window)

        if self.pause:
            window.blit(GameConfig.GUIDE_BACKGROUND,(GameConfig.WINDOW_W/2-400,GameConfig.WINDOW_H/2-243))
            for objet in self.menu :
                objet.draw(window)
            window.blit(self.pages_images[self.page],(GameConfig.WINDOW_W/2-400,GameConfig.WINDOW_H/2-243))

        if self.player.vie <= 0 or (self.anim_mort >=40 and self.anim_mort <=100) :
            s = pygame.Surface((GameConfig.WINDOW_W,GameConfig.WINDOW_H), pygame.SRCALPHA)
            if self.anim_mort <= 40:
                s.fill((0,0,0,255/40*(self.anim_mort)))
            else :
                s.fill((0,0,0,255/60*(100-self.anim_mort)))
            window.blit(s, (0,0))
            

        if self.player.saut >= 30 and self.player.saut !=90 :
            s = pygame.Surface((GameConfig.WINDOW_W,GameConfig.WINDOW_H), pygame.SRCALPHA)  
            if 70 >= self.player.saut : 
                s.fill((0,0,0,255/40*(self.player.saut-30)))                         
            elif self.player.saut >= 72:
                s.fill((0,0,0,255/19*(90-self.player.saut))) 
            else :
                self.trappe.ouverte=False
                self.player.text_surface=False
                Map.SALLE_COURANTE += 1
                self.remplir_salle()
                Map.advance_state()
                s.fill((0,0,0,255))  
            window.blit(s, (0,0))
                


        

        



    def advance_state(self,next_move):
        self.pause = self.player.pause
        if self.player.vie <= 0 or (self.anim_mort >=40 and self.anim_mort <=100) :
            self.anim_mort = min(self.anim_mort+1,101)
            if self.anim_mort == 40:
                Map.SALLE_COURANTE=0
                self.player.f_b_touch = 0
                self.remplir_salle()
                Map.advance_state()
                self.player.soinXfois(GameConfig.STAT_PERSONNAGE[self.player.role][0])
                self.player.ordonne()
                for coeur in self.player.coeur:
                    coeur.advance_state(self.player)
        elif self.pause :
            if self.menu == []:
                self.menu = [Guide_Reprendre(95,172),Guide_1(95,228),Guide_Deplacement(95,295),Guide_Commandes(95,367)
                             ,Guide_Arme(800,157),Guide_Potions(800,254),Guide_Enemies(800,325),Guide_Personnages(800,414)]
            self.pause = self.menu[0].pause
            self.player.pause = self.pause
            self.menu[0].pause = True
        else :
            for objet in self.menu :
                if objet.animation == 0:
                    self.menu=[]
                objet.depart()
                
            self.player.advance_state(next_move)

            if self.player.saut == 70:
                self.remplir_salle()

            for personnage in self.personnages :
                personnage.advance_state()
                self.joueur_proche(personnage)

            for corps in self.mort:
                corps.advance_state()
                if corps.sprite_count+1 >= corps.fin :
                    self.mort.remove(corps)

            for objet in self.objet_depart :
                self.joueur_proche(objet)

            if self.trappe.ouverte:
                self.joueur_proche(self.trappe)

            for mannequin in self.mannequin:
                for projectile in self.player.projectile :
                    if mannequin.is_touching(projectile):
                        mannequin.degat(projectile.degat)
                        if mannequin.vie <= 0:
                            x,y = mannequin.rect.topleft
                            self.mort.append(Mort(x+15,y+30))
                            self.mannequin.remove(mannequin)
                        self.player.projectile.remove(projectile)
                    elif projectile.distance <= 0 :
                        self.player.projectile.remove(projectile)    
            if Map.SALLE_COURANTE == 0:
                if len(self.mannequin) == 0:
                    if self.f_b_r == 0:
                        self.f_b_r = 60
                        self.mannequin =  [Mannequin(264,208)]
                    self.f_b_r = max(self.f_b_r-1,0)  

            for projectile in self.player.projectile :
                if projectile.distance <= 0 :
                        self.player.projectile.remove(projectile)

            for enemy in self.enemy:

                for projectile in self.player.projectile :
                    if enemy.is_touching(projectile):
                        enemy.degat(projectile.degat)
                        if enemy.vie <= 0:
                            x,y = enemy.rect.topleft
                            self.mort.append(Mort(x+30,y+40))
                            self.enemy.remove(enemy)
                            if self.enemy == [] :
                                if Map.SALLE_COURANTE < 3:
                                    self.items_tab.append(self.list_items[randint(0,len(self.list_items))])
                                self.trappe.ouverte = True
                        self.player.projectile.remove(projectile)
                        
                for projectile in enemy.projectile:
                    if self.player.is_touching(projectile):
                        enemy.projectile.remove(projectile)
                    elif projectile.distance <= 0 :
                        enemy.projectile.remove(projectile)
                        
                    


                x,y=self.player.rect.center
                if isinstance(enemy,Enemy_Distance_Lent) or isinstance(enemy,Enemy_Distance_Rapide) or isinstance(enemy,Enemy_Corps_A_Corps):
                    enemy.advance_state(x,y)
                elif isinstance(enemy,Enemy_Boss) :
                    enemy.advance_state(x,y,self.enemy)
                else :
                    enemy.advance_state()
                
                self.player.is_touching(enemy)


            for objet in self.items_tab:
                self.joueur_proche(objet)
                if objet.etat == False:
                    self.player.text_surface = False
                    self.items_tab.remove(objet)

            if self.player.vie <= 0 :
                self.anim_mort = 0

                    

    def interaction(self):
        if self.player.text_surface :
            element = self.player.text_surface[1]

            if isinstance(element, Personnage) :               
                numero = self.player.role
                self.player.chg_stat(element)
                self.player.role = element.numero
                element.numero = numero

            elif isinstance(element, Items) :
                element.etat = False
                self.player.item_vitesse_player+=element.vitesse_player
                self.player.item_vitesse_proj+=element.vitesse_proj
                self.player.item_cadence+=element.cadence
                for i in range(element.vie):
                    self.player.soin()
                self.player.item_degats_proj+=element.degats_proj

            elif isinstance(element,Arme) :
                numero = self.player.arme
                self.player.arme = element.numero
                element.changer_arme(numero)
                self.player.cadence_arme = GameConfig.STAT_ARME[self.player.arme]['couldown']
            
            elif isinstance(element,Table):
                self.trappe.ouverte = True
                self.player.pause= self.pause == False

            elif isinstance(element,Trappe):
                if self.player.saut == 90 :
                    self.player.saut = 0


    def clique(self):
        for objet in self.menu:
            if objet.rect.collidepoint(pygame.mouse.get_pos()):
                if isinstance(objet,Guide_Arme) :
                    self.page = 'Arme'
                elif isinstance(objet,Guide_Enemies) :
                    self.page = 'Enemies'
                elif isinstance(objet,Guide_Commandes) :
                    self.page = 'Commandes'
                elif isinstance(objet,Guide_1) :
                    self.page = 'Important'
                elif isinstance(objet,Guide_Deplacement) :
                    self.page = 'Commandes'
                elif isinstance(objet,Guide_Potions) :
                    self.page = 'Potions'
                elif isinstance(objet,Guide_Personnages) :
                    self.page = 'Personnages'
                else :
                    objet.clique()

    def echap(self):
        self.pause = self.pause==False
        self.player.pause = self.pause

    def remplir_salle(self):
        if Map.SALLE_COURANTE == 0:
            self.trappe.ouverte = True
            self.enemy=[] 
            self.mort=[]
            self.menu=[]
            self.pages_images = {'Arme' : GameConfig.GUIDE_ARME,'Commandes' : GameConfig.GUIDE_COMMANDES,'Enemies' : GameConfig.GUIDE_ENEMIES,'Personnages' : GameConfig.GUIDE_PERSONNAGES,'Potions' : GameConfig.GUIDE_POTIONS,'Important' : GameConfig.GUIDE_IMPORTANT}
            self.page = 'Important'
            self.pause = False
            if self.player.role == 0:
                self.personnages = [Personnage(832,504,1),Personnage(832,350,2)]
            elif self.player.role == 1:
                self.personnages = [Personnage(832,504,0),Personnage(832,350,2)]
            else :
                self.personnages = [Personnage(832,504,0),Personnage(832,350,1)]

            self.objet_depart=[Arme(128,480,1),Arme(128,328,2),Table(608,240)]
            self.items_tab = []
            self.table = Table(608,240)
            self.mannequin = [Mannequin(264,208)]
            self.position_trappe(GameConfig.TRAPPE_X, GameConfig.TRAPPE_Y)
            self.player.position(428,480)

        if Map.SALLE_COURANTE == 1:
            self.enemy = [Enemy_Distance_Rapide(700,150),Enemy_Distance_Lent(100,100),Enemy_Distance_Lent(500,500),Enemy_Corps_A_Corps(600,120),Enemy_Corps_A_Corps(400,180)]
            self.trappe.ouverte = False
            self.items_tab = []
            self.objet_depart = []
            self.personnages = []
            self.obstacles = []
            self.mannequin = []

            self.position_trappe(700,500)
            self.player.position(100,500)
            
        elif Map.SALLE_COURANTE == 2:
            self.enemy = [Enemy_Distance_Rapide(100,100),Enemy_Distance_Rapide(600,150),Enemy_Distance_Rapide(100,500),Enemy_Distance_Rapide(120,80),Enemy_Corps_A_Corps(150,400),Enemy_Corps_A_Corps(300,100),Enemy_Corps_A_Corps(700,100)]
            self.trappe.ouverte = False
            self.items_tab = []
            self.position_trappe(700,200)           
            self.player.position(500,500)
        
        elif Map.SALLE_COURANTE == 3:
            self.enemy = [Enemy_Boss(400,100)]
            self.trappe.ouverte = False
            self.items_tab = []
            self.position_trappe(400,100)            
            self.player.position(500,500)
        elif Map.SALLE_COURANTE == 4:
            self.enemy = []
            self.trappe.ouverte = False
            self.items_tab = []            
            self.player.position(500,500)


    def joueur_proche(self,element):
        x,y = element.rect.center
        if isinstance(element, Personnage):
            y-=GameConfig.IDLE_H/2
        est_proche = (abs(self.player.rect.center[0]-x)<= 60) and (abs(self.player.rect.center[1]-y) <= 60)     
        if self.player.text_surface :
            if element.__class__ == self.player.text_surface[1].__class__ :
                if isinstance(element, Items):
                    if not (est_proche):
                        self.player.text_surface = False
                    
                elif isinstance(element, Table):
                    if not (est_proche):
                        self.player.text_surface = False

                elif isinstance(element, Trappe):
                    if not (est_proche):
                        self.player.text_surface = False

                elif element.numero == self.player.text_surface[1].numero:
                    if not (est_proche):   
                        self.player.text_surface = False
                    else :
                        self.player.text_surface[2]=self.player.icone(element)
                    
        else :
            if est_proche :
                self.player.text_surface = [(x,y),element,self.player.icone(element)]

        

    def position_trappe(self,x,y):
        self.trappe.rect.x = x
        self.trappe.rect.y = y
        x_trappe,y_trappe = self.trappe.rect.topleft
        self.player.trappe_x = x_trappe
        self.player.trappe_y = y_trappe