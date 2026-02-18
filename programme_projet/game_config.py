import pygame

class GameConfig :
    WINDOW_H=640
    WINDOW_W=960
    Y_PLATEFORM = 516
    PLAYER_W = 102
    PLAYER_H = 102
    ENEMY_DISTANCE_LENT_W = 64
    ENEMY_DISTANCE_LENT_H = 64
    ENEMY_DISTANCE_RAPIDE_W = 64
    ENEMY_DISTANCE_RAPIDE_H = 64
    ENEMY_CORPS_A_CORPS_W = 64
    ENEMY_CORPS_A_CORPS_H = 64
    ENEMY_BOSS_W = 100
    ENEMY_BOSS_H = 100
    DT =0.5

    VITESSE_DEPLACEMENT_JOUEUR=10
    VITESSE_DEPLACEMENT_ENEMY_LENT=10
    VITESSE_DEPLACEMENT_ENEMY_RAPIDE=30
    VITESSE_DEPLACEMENT_ENEMY_CORPS_A_CORPS = 8
    VITESSE_DEPLACEMENT_ENEMY_BOSS = 3

    NB_FRAMES_PER_SPRITE_PLAYER = 4
    NB_FRAMES_PER_SPRITE_ENEMY_DISTANCE_LENT = 4
    NB_FRAMES_PER_SPRITE_ENEMY_DISTANCE_RAPIDE = 2
    NB_FRAMES_PER_SPRITE_ENEMY_CORPS_A_CORPS = 2
    NB_FRAMES_PER_SPRITE_ENEMY_BOSS = 2
    NB_FRAMES_PER_SPRITE_PROJECTILE = 3
    NB_FRAMES_PER_SPRITE_MORT = 3
    NB_FRAMES_PER_SPRITE_IDLE = 6

    MORT_W = 48
    MORT_H = 48

    PROJECTILE_W = 32
    PROJECTILE_H = 32

    PROJECTILE_TAILLE = 2
    COULDOWN = 20
    COULDOWN_ENEMY = 50

    COEUR_H = 32
    COEUR_W = 32


    IDLE_H = 51
    IDLE_W = 51

    PLAYER_COLISSION_H = 32
    PLAYER_COLISSION_W = 32

    TEMPS_INVULNERABLE=45

    VITESSE_PROJECTILE = 15
    
    #Position des items:
    ## Position item up vitesse player:
    ITEM_VITESSE_X = 100
    ITEM_VITESSE_Y = 200
    ## Position item up vitesse proj:
    ITEM_VITESSE_PROJ_X=100
    ITEM_VITESSE_PROJ_Y=200
    ## Position item up cadence:
    ITEM_CADENCE_X= 100
    ITEM_CADENCE_Y= 200
    ## Position item up vie:
    ITEM_VIE_X=100
    ITEM_VIE_Y=200
    ## Position item up degat:
    ITEM_DEGATS_X=100
    ITEM_DEGATS_Y=200
  
    COEUR_ESPACEMENT=40

    TRAPPE_X = 464
    TRAPPE_Y = 208

    TRAPPE_W = 32
    TRAPPE_H = 32

    MAIN_W= 25
    MAIN_H= 26

    DEGAT_JOUEUR = 1

    STAT_BASIQUE= {'degat' : 2,'couldown' : 2,'vitesse_projectile' : 1,'distance' : 2}
    STAT_DAGUE={'degat' : 1,'couldown' : 3,'vitesse_projectile' : 2,'distance' : 1}
    STAT_EPEE={'degat' : 3,'couldown' : 1,'vitesse_projectile' : 1,'distance' : 5}
    STAT_FAUX={'degat' : 2,'couldown' : 3,'vitesse_projectile' : 2,'distance' : 1}
    STAT_PIOCHE={'degat' : 2,'couldown' : 3,'vitesse_projectile' : 2,'distance' : 1}
    
    STAT_ARME=[STAT_DAGUE,STAT_EPEE,STAT_FAUX,STAT_PIOCHE]

    STAT_PERSONNAGE = [(4,2),(5,1),(3,3)]



    def init():
        pygame.font.init()
        GameConfig.FONT = pygame.font.SysFont('Comic Sans MS', 15)
        GameConfig.FONT30 = pygame.font.SysFont('Comic Sans MS', 30)
        GameConfig.INTERACTION = pygame.image.load("Images/UI/Interaction_table.png")
        GameConfig.INTERACTION_TRAPPE = pygame.image.load("Images/UI/Interaction_trappe.png")

        GameConfig.ICONES_VERT = {'vie':pygame.image.load('Images/UI/Vert/vie.png'),'couldown':pygame.image.load('Images/UI/Vert/couldown.png'),'vitesse_joueur':pygame.image.load('Images/UI/Vert/vitesse_joueur.png'),'vitesse_projectile':pygame.image.load('Images/UI/Vert/vitesse_projectile.png'),'degat':pygame.image.load('Images/UI/Vert/degat.png'),'distance':pygame.image.load('Images/UI/Vert/degat.png')}
        GameConfig.ICONES_ROUGE = {'vie':pygame.image.load('Images/UI/Rouge/vie.png'),'couldown':pygame.image.load('Images/UI/Rouge/couldown.png'),'vitesse_joueur':pygame.image.load('Images/UI/Rouge/vitesse_joueur.png'),'vitesse_projectile':pygame.image.load('Images/UI/Rouge/vitesse_projectile.png'),'degat':pygame.image.load('Images/UI/Rouge/degat.png'),'distance':pygame.image.load('Images/UI/Vert/degat.png')}
        GameConfig.ICONES_BLANC = {'vie':pygame.image.load('Images/UI/Blanc/vie.png'),'couldown':pygame.image.load('Images/UI/Blanc/couldown.png'),'vitesse_joueur':pygame.image.load('Images/UI/Blanc/vitesse_joueur.png'),'vitesse_projectile':pygame.image.load('Images/UI/Blanc/vitesse_projectile.png'),'degat':pygame.image.load('Images/UI/Blanc/degat.png'),'distance':pygame.image.load('Images/UI/Vert/degat.png')}

        GameConfig.ICONES = {'vert' : GameConfig.ICONES_VERT, 'rouge':GameConfig.ICONES_ROUGE,'blanc': GameConfig.ICONES_BLANC}

        GameConfig.COEUR = pygame.image.load("Images/Personnage_principale/Coeur.png")

        GameConfig.CHEVALIER_SAUT_DROIT = []
        GameConfig.CHEVALIER_SAUT_GAUCHE = []

        for i in range(16):
            GameConfig.CHEVALIER_SAUT_DROIT.append(pygame.image.load("Images/Personnage_principale/Chevalier_Saut/tile0"+str(i)+".png"))
            GameConfig.CHEVALIER_SAUT_GAUCHE.append(pygame.transform.flip(pygame.image.load("Images/Personnage_principale/Chevalier_Saut/tile0"+str(i)+".png"),True,False))

        GameConfig.CHEVALIER_SAUT = {1 : GameConfig.CHEVALIER_SAUT_DROIT,-1 : GameConfig.CHEVALIER_SAUT_GAUCHE}
        

        GameConfig.MAGE_SAUT_DROIT = []
        GameConfig.MAGE_SAUT_GAUCHE = []

        for i in range(16):
            GameConfig.MAGE_SAUT_DROIT.append(pygame.image.load("Images/Personnage_principale/Mage_Saut/tile0"+str(i)+".png"))
            GameConfig.MAGE_SAUT_GAUCHE.append(pygame.transform.flip(pygame.image.load("Images/Personnage_principale/Mage_Saut/tile0"+str(i)+".png"),True,False))

        GameConfig.MAGE_SAUT = {1 : GameConfig.MAGE_SAUT_DROIT,-1 : GameConfig.MAGE_SAUT_GAUCHE}



        GameConfig.ARCHER_SAUT_DROIT = []
        GameConfig.ARCHER_SAUT_GAUCHE = []

        for i in range(16):
            GameConfig.ARCHER_SAUT_DROIT.append(pygame.image.load("Images/Personnage_principale/Archer_Saut/tile0"+str(i)+".png"))
            GameConfig.ARCHER_SAUT_GAUCHE.append(pygame.transform.flip(pygame.image.load("Images/Personnage_principale/Archer_Saut/tile0"+str(i)+".png"),True,False))

        GameConfig.ARCHER_SAUT = {1 : GameConfig.ARCHER_SAUT_DROIT,-1 : GameConfig.ARCHER_SAUT_GAUCHE}


        GameConfig.MAIN_SAUT = [GameConfig.MAGE_SAUT,GameConfig.CHEVALIER_SAUT,GameConfig.ARCHER_SAUT]



        GameConfig.GUIDE_BACKGROUND= pygame.image.load("Images/UI/pages/Page_base.png")
        GameConfig.GUIDE_FOREGROUND = pygame.image.load("Images/UI/pages/page_devant.png")
        GameConfig.GUIDE_ARME = pygame.image.load("Images/UI/pages/arme.png")
        GameConfig.GUIDE_ENEMIES = pygame.image.load("Images/UI/pages/enemies.png")
        GameConfig.GUIDE_COMMANDES = pygame.image.load("Images/UI/pages/commandes.png")
        GameConfig.GUIDE_PERSONNAGES = pygame.image.load("Images/UI/pages/personnages.png")
        GameConfig.GUIDE_POTIONS = pygame.image.load("Images/UI/pages/potions.png")
        GameConfig.GUIDE_IMPORTANT = pygame.image.load("Images/UI/pages/defaut.png")

        GameConfig.BOUTON_CONTINUER = pygame.image.load("Images/UI/Boutons/Btn_Continuer.png")
        GameConfig.BOUTON_ARME = pygame.image.load("Images/UI/Boutons/Btn_Arme.png")
        GameConfig.BOUTON_ENEMIES = pygame.image.load("Images/UI/Boutons/Btn_Enemies.png")
        GameConfig.BOUTON_COMMANDES = pygame.image.load("Images/UI/Boutons/Btn_Commandes.png")
        GameConfig.BOUTON_1 = pygame.image.load("Images/UI/Boutons/1.png")
        GameConfig.BOUTON_DEPLACEMENT = pygame.image.load("Images/UI/Boutons/Btn_Deplacement.png")
        GameConfig.BOUTON_POTIONS = pygame.image.load("Images/UI/Boutons/Btn_Potions.png")
        GameConfig.BOUTON_PERSONNAGES = pygame.image.load("Images/UI/Boutons/Btn_Personnages.png")

        GameConfig.TABLE = pygame.image.load("Images/UI/table.png")
        
        GameConfig.ITEM_VITESSE_PLAYER=pygame.image.load('Images/Potions/Vitesse_deplacement.png')
        GameConfig.ITEM_VITESSE_PROJ=pygame.image.load('Images/Potions/Vitesse_projectile.png')
        GameConfig.ITEM_CADENCE=pygame.image.load('Images/Potions/Cadence.png')
        GameConfig.ITEM_VIE=pygame.image.load('Images/Potions/Vie.png')
        GameConfig.ITEM_DEGATS_PROJ=pygame.image.load('Images/Potions/Degat.png')

        GameConfig.TRAPPE_OUVERTE=pygame.image.load('Images/trappe/trappe_ouverte.png')
        GameConfig.TRAPPE_FERMEE=pygame.image.load('Images/trappe/trappe_ferme.png')

        GameConfig.TRAPPE = {True:GameConfig.TRAPPE_OUVERTE,False:GameConfig.TRAPPE_FERMEE}

        GameConfig.STANDING_IMG_MAGE = {1: pygame.image.load('Images/Personnage_principale/Mage/idle.png')}
        GameConfig.STANDING_IMG_MAGE[-1] = pygame.transform.flip(GameConfig.STANDING_IMG_MAGE[1],True,False)

        GameConfig.STANDING_IMG_CHEVALIER = {1 : pygame.image.load('Images/Personnage_principale/Chevalier/idle.png')}
        GameConfig.STANDING_IMG_CHEVALIER[-1] = pygame.transform.flip(GameConfig.STANDING_IMG_CHEVALIER[1],True,False)

        GameConfig.STANDING_IMG_ARCHER = {1 : pygame.image.load('Images/Personnage_principale/Archer/idle.png')}
        GameConfig.STANDING_IMG_ARCHER[-1] = pygame.transform.flip(GameConfig.STANDING_IMG_ARCHER[1],True,False)

        GameConfig.STANDING_IMG_MAIN = [GameConfig.STANDING_IMG_MAGE,GameConfig.STANDING_IMG_CHEVALIER,GameConfig.STANDING_IMG_ARCHER]

        GameConfig.STANDING_IMG_BOSS = [pygame.image.load('Images/standing_boss.png')]
        GameConfig.STANDING_MASK_BOSS = [pygame.mask.from_surface(GameConfig.STANDING_IMG_BOSS[0])]


        GameConfig.FLYING_FROM_RIGHT = [pygame.image.load('Images/bat1.png').convert_alpha(),pygame.image.load('Images/bat2.png').convert_alpha(),pygame.image.load('Images/bat3.png').convert_alpha(),pygame.image.load('Images/bat4.png').convert_alpha(),pygame.image.load('Images/bat5.png').convert_alpha()]
        GameConfig.FLYING_FROM_LEFT=[]
        GameConfig.FLYING_FROM_RIGHT_MASK=[]
        GameConfig.FLYING_FROM_LEFT_MASK=[]
        for im in GameConfig.FLYING_FROM_RIGHT:
            GameConfig.FLYING_FROM_LEFT.append(pygame.transform.flip(im,True,False))

        for im in GameConfig.FLYING_FROM_RIGHT:
            GameConfig.FLYING_FROM_RIGHT_MASK.append(pygame.mask.from_surface(im))

        for im in GameConfig.FLYING_FROM_LEFT:
            GameConfig.FLYING_FROM_LEFT_MASK.append(pygame.mask.from_surface(im))
            
            
        GameConfig.IMG_MANNEQUIN = [pygame.image.load('Images/Enemy/Mannequin/tile001.png')]
        GameConfig.MASK_MANNEQUIN = [pygame.mask.from_surface(pygame.image.load('Images/Enemy/Mannequin/tile001.png'))]
        
        GameConfig.IMG_ENEMY_LENT = [pygame.image.load('Images/Enemy/Enemy_Distance_Lent/tile004.png')]
        GameConfig.MASK_ENEMY_LENT = [pygame.mask.from_surface(pygame.image.load('Images/Enemy/Enemy_Distance_Lent/tile004.png'))]
        
        GameConfig.WALK_RIGHT_IMG_ENEMY_LENT = [pygame.image.load('Images/Enemy/Enemy_Distance_Lent/tile000.png'),pygame.image.load('Images/Enemy/Enemy_Distance_Lent//tile001.png'),pygame.image.load('Images/Enemy/Enemy_Distance_Lent/tile002.png'),pygame.image.load('Images/Enemy/Enemy_Distance_Lent/tile003.png'),pygame.image.load('Images/Enemy/Enemy_Distance_Lent/tile004.png'),pygame.image.load('Images/Enemy/Enemy_Distance_Lent/tile005.png')]
        GameConfig.WALK_LEFT_IMG_ENEMY_LENT = []
        
        for img in GameConfig.WALK_RIGHT_IMG_ENEMY_LENT :
            GameConfig.WALK_LEFT_IMG_ENEMY_LENT.append(pygame.transform.flip(img,True,False))
            
        GameConfig.WALK_RIGHT_MASKS_ENEMY_LENT = []
        GameConfig.WALK_LEFT_MASKS_ENEMY_LENT = []
        for im in GameConfig.WALK_RIGHT_IMG_ENEMY_LENT :
            GameConfig.WALK_RIGHT_MASKS_ENEMY_LENT.append(pygame.mask.from_surface(im))
        for im in GameConfig.WALK_LEFT_IMG_ENEMY_LENT :
            GameConfig.WALK_LEFT_MASKS_ENEMY_LENT.append(pygame.mask.from_surface(im))
        
        GameConfig.IMG_ENEMY_RAPIDE = [pygame.image.load('Images/Enemy/Enemy_Distance_Rapide/tile004.png')]
        GameConfig.MASK_ENEMY_RAPIDE = [pygame.mask.from_surface(pygame.image.load('Images/Enemy/Enemy_Distance_Rapide/tile004.png'))]
        
        GameConfig.WALK_RIGHT_IMG_ENEMY_RAPIDE = [pygame.image.load('Images/Enemy/Enemy_Distance_Rapide/tile000.png'),pygame.image.load('Images/Enemy/Enemy_Distance_Rapide//tile001.png'),pygame.image.load('Images/Enemy/Enemy_Distance_Rapide/tile002.png'),pygame.image.load('Images/Enemy/Enemy_Distance_Rapide/tile003.png'),pygame.image.load('Images/Enemy/Enemy_Distance_Rapide/tile004.png'),pygame.image.load('Images/Enemy/Enemy_Distance_Rapide/tile005.png')]
        GameConfig.WALK_LEFT_IMG_ENEMY_RAPIDE = []
        
        for img in GameConfig.WALK_RIGHT_IMG_ENEMY_RAPIDE :
            GameConfig.WALK_LEFT_IMG_ENEMY_RAPIDE.append(pygame.transform.flip(img,True,False))
            
        GameConfig.WALK_RIGHT_MASKS_ENEMY_RAPIDE = []
        GameConfig.WALK_LEFT_MASKS_ENEMY_RAPIDE = []
        for im in GameConfig.WALK_RIGHT_IMG_ENEMY_RAPIDE :
            GameConfig.WALK_RIGHT_MASKS_ENEMY_RAPIDE.append(pygame.mask.from_surface(im))
        for im in GameConfig.WALK_LEFT_IMG_ENEMY_RAPIDE :
            GameConfig.WALK_LEFT_MASKS_ENEMY_RAPIDE.append(pygame.mask.from_surface(im))
        
        GameConfig.IMG_ENEMY_CORPS = [pygame.image.load('Images/Enemy/Enemy_Corps_A_Corps/tile003.png')]
        GameConfig.MASK_ENEMY_CORPS = [pygame.mask.from_surface(pygame.image.load('Images/Enemy/Enemy_Corps_A_Corps/tile003.png'))]
        
        GameConfig.WALK_RIGHT_IMG_ENEMY_CORPS = [pygame.image.load('Images/Enemy/Enemy_Corps_A_Corps/tile000.png'),pygame.image.load('Images/Enemy/Enemy_Corps_A_Corps//tile001.png'),pygame.image.load('Images/Enemy/Enemy_Corps_A_Corps/tile002.png'),pygame.image.load('Images/Enemy/Enemy_Corps_A_Corps/tile003.png'),pygame.image.load('Images/Enemy/Enemy_Corps_A_Corps/tile004.png'),pygame.image.load('Images/Enemy/Enemy_Corps_A_Corps/tile005.png')]
        GameConfig.WALK_LEFT_IMG_ENEMY_CORPS = []
        
        for img in GameConfig.WALK_RIGHT_IMG_ENEMY_CORPS :
            GameConfig.WALK_LEFT_IMG_ENEMY_CORPS.append(pygame.transform.flip(img,True,False))
            
        GameConfig.WALK_RIGHT_MASKS_ENEMY_CORPS = []
        GameConfig.WALK_LEFT_MASKS_ENEMY_CORPS = []
        for im in GameConfig.WALK_RIGHT_IMG_ENEMY_CORPS :
            GameConfig.WALK_RIGHT_MASKS_ENEMY_CORPS.append(pygame.mask.from_surface(im))
        for im in GameConfig.WALK_LEFT_IMG_ENEMY_CORPS :
            GameConfig.WALK_LEFT_MASKS_ENEMY_CORPS.append(pygame.mask.from_surface(im))
        
        
        
        
        GameConfig.WALK_RIGHT_IMG_CHEVALIER = [pygame.image.load('Images/Personnage_principale/Chevalier/tile000.png'),pygame.image.load('Images/Personnage_principale/Chevalier/tile001.png'),pygame.image.load('Images/Personnage_principale/Chevalier/tile002.png'),pygame.image.load('Images/Personnage_principale/Chevalier/tile003.png'),pygame.image.load('Images/Personnage_principale/Chevalier/tile004.png'),pygame.image.load('Images/Personnage_principale/Chevalier/tile005.png')]
        GameConfig.WALK_LEFT_IMG_CHEVALIER = []

        GameConfig.WALK_RIGHT_IMG_MAGE = [pygame.image.load('Images/Personnage_principale/Mage/tile000.png'),pygame.image.load('Images/Personnage_principale/Mage/tile001.png'),pygame.image.load('Images/Personnage_principale/Mage/tile002.png'),pygame.image.load('Images/Personnage_principale/Mage/tile003.png'),pygame.image.load('Images/Personnage_principale/Mage/tile004.png'),pygame.image.load('Images/Personnage_principale/Mage/tile005.png')]
        GameConfig.WALK_LEFT_IMG_MAGE = []

        GameConfig.WALK_RIGHT_IMG_ARCHER = [pygame.image.load('Images/Personnage_principale/Archer/tile000.png'),pygame.image.load('Images/Personnage_principale/Archer/tile001.png'),pygame.image.load('Images/Personnage_principale/Archer/tile002.png'),pygame.image.load('Images/Personnage_principale/Archer/tile003.png'),pygame.image.load('Images/Personnage_principale/Archer/tile004.png'),pygame.image.load('Images/Personnage_principale/Archer/tile005.png')]
        GameConfig.WALK_LEFT_IMG_ARCHER = []

        for img in GameConfig.WALK_RIGHT_IMG_MAGE :
            GameConfig.WALK_LEFT_IMG_MAGE.append(pygame.transform.flip(img,True,False))

        for img in GameConfig.WALK_RIGHT_IMG_CHEVALIER :
             GameConfig.WALK_LEFT_IMG_CHEVALIER.append(pygame.transform.flip(img,True,False))

        for img in GameConfig.WALK_RIGHT_IMG_ARCHER :
             GameConfig.WALK_LEFT_IMG_ARCHER.append(pygame.transform.flip(img,True,False))

        
        GameConfig.WALK_RIGHT_MASKS_MAGE = []
        GameConfig.WALK_LEFT_MASKS_MAGE = []
        for im in GameConfig.WALK_RIGHT_IMG_MAGE :
            GameConfig.WALK_RIGHT_MASKS_MAGE.append(pygame.mask.from_surface(im))
        for im in GameConfig.WALK_LEFT_IMG_MAGE :
            GameConfig.WALK_LEFT_MASKS_MAGE.append(pygame.mask.from_surface(im))


        GameConfig.WALK_RIGHT_MASKS_CHEVALIER = []
        GameConfig.WALK_LEFT_MASKS_CHEVALIER = []
        for im in GameConfig.WALK_RIGHT_IMG_CHEVALIER :
            GameConfig.WALK_RIGHT_MASKS_CHEVALIER.append(pygame.mask.from_surface(im))
        for im in GameConfig.WALK_LEFT_IMG_CHEVALIER :
            GameConfig.WALK_LEFT_MASKS_CHEVALIER.append(pygame.mask.from_surface(im))


        GameConfig.WALK_RIGHT_MASKS_ARCHER = []
        GameConfig.WALK_LEFT_MASKS_ARCHER = []
        for im in GameConfig.WALK_RIGHT_IMG_ARCHER :
            GameConfig.WALK_RIGHT_MASKS_ARCHER.append(pygame.mask.from_surface(im))
        for im in GameConfig.WALK_LEFT_IMG_ARCHER :
            GameConfig.WALK_LEFT_MASKS_ARCHER.append(pygame.mask.from_surface(im))


        GameConfig.WALK_RIGHT_IMG_MAIN = [GameConfig.WALK_RIGHT_IMG_MAGE,GameConfig.WALK_RIGHT_IMG_CHEVALIER,GameConfig.WALK_RIGHT_IMG_ARCHER]
        GameConfig.WALK_LEFT_IMG_MAIN = [GameConfig.WALK_LEFT_IMG_MAGE,GameConfig.WALK_LEFT_IMG_CHEVALIER,GameConfig.WALK_LEFT_IMG_ARCHER]

        GameConfig.WALK_IMG = {-1 : GameConfig.WALK_LEFT_IMG_MAIN, 1 : GameConfig.WALK_RIGHT_IMG_MAIN}


        GameConfig.WALK_RIGHT_MASKS_MAIN = [GameConfig.WALK_RIGHT_MASKS_MAGE,GameConfig.WALK_RIGHT_MASKS_CHEVALIER,GameConfig.WALK_RIGHT_MASKS_ARCHER]
        GameConfig.WALK_LEFT_MASKS_MAIN = [GameConfig.WALK_LEFT_MASKS_MAGE,GameConfig.WALK_LEFT_MASKS_CHEVALIER,GameConfig.WALK_LEFT_MASKS_ARCHER]

        GameConfig.WALK_MASK = {-1 : GameConfig.WALK_LEFT_MASKS_MAIN, 1 : GameConfig.WALK_RIGHT_MASKS_MAIN}
            

        GameConfig.STANDING_MASK_MAGE={1 : pygame.mask.from_surface(GameConfig.STANDING_IMG_MAGE[1]), -1 : pygame.mask.from_surface(GameConfig.STANDING_IMG_MAGE[-1])}
        GameConfig.STANDING_MASK_CHEVALIER={1 : pygame.mask.from_surface(GameConfig.STANDING_IMG_CHEVALIER[1]), -1 : pygame.mask.from_surface(GameConfig.STANDING_IMG_CHEVALIER[-1])}
        GameConfig.STANDING_MASK_ARCHER={1 : pygame.mask.from_surface(GameConfig.STANDING_IMG_ARCHER[1]), -1 : pygame.mask.from_surface(GameConfig.STANDING_IMG_ARCHER[-1])}

        GameConfig.STANDING_MASK_MAIN = [GameConfig.STANDING_MASK_MAGE,GameConfig.STANDING_MASK_CHEVALIER,GameConfig.STANDING_MASK_ARCHER]


        GameConfig.MAINS =  {1 : pygame.image.load('Images/Personnage_principale/Mains/main_g.png'), -1 : pygame.image.load('Images/Personnage_principale/Mains/main_d.png')}


        GameConfig.ARMES = [{1 : pygame.image.load('Images/Personnage_principale/Armes/Couteau.png')},{1 : pygame.image.load('Images/Personnage_principale/Armes/Epee.png')},{1 : pygame.image.load('Images/Personnage_principale/Armes/faux.png')},{1 : pygame.image.load('Images/Personnage_principale/Armes/pioche.png')}]
        for i in range (len(GameConfig.ARMES)):
            GameConfig.ARMES[i][-1] = pygame.transform.flip(GameConfig.ARMES[i][1],True,False)

        GameConfig.CHEVALIER_IDLE = [pygame.image.load('Images/Personnage_principale/Chevalier_Idle/tile000.png'),pygame.image.load('Images/Personnage_principale/Chevalier_Idle/tile001.png'),pygame.image.load('Images/Personnage_principale/Chevalier_Idle/tile002.png'),pygame.image.load('Images/Personnage_principale/Chevalier_Idle/tile003.png')]
        GameConfig.MAGE_IDLE = [pygame.image.load('Images/Personnage_principale/Mage_Idle/tile000.png'),pygame.image.load('Images/Personnage_principale/Mage_Idle/tile001.png'),pygame.image.load('Images/Personnage_principale/Mage_Idle/tile002.png'),pygame.image.load('Images/Personnage_principale/Mage_Idle/tile003.png')]
        GameConfig.ARCHER_IDLE = [pygame.image.load('Images/Personnage_principale/Archer_Idle/tile000.png'),pygame.image.load('Images/Personnage_principale/Archer_Idle/tile001.png'),pygame.image.load('Images/Personnage_principale/Archer_Idle/tile002.png'),pygame.image.load('Images/Personnage_principale/Archer_Idle/tile003.png')]

        GameConfig.PERSONNAGE = [GameConfig.MAGE_IDLE,GameConfig.CHEVALIER_IDLE,GameConfig.ARCHER_IDLE]


        GameConfig.PROJECTILES = []

        GameConfig.TAILLE_ARME = []
        for el in GameConfig.ARMES :
            image = el[1] 
            GameConfig.TAILLE_ARME.append((image.get_width(),image.get_height())) 
            GameConfig.PROJECTILES.append([[pygame.transform.rotate(pygame.transform.scale(image,(image.get_width()/GameConfig.PROJECTILE_TAILLE,image.get_height()/GameConfig.PROJECTILE_TAILLE)),270)]])

        

        for i in range(len(GameConfig.PROJECTILES)):
            objet = GameConfig.PROJECTILES[i][0][0]
            GameConfig.PROJECTILES[i] = { (1,0) : objet, (0,1) :pygame.transform.rotate(objet,90),(-1,0) :pygame.transform.rotate(objet,180),(0,-1) :pygame.transform.rotate(objet,270),(1,1) :pygame.transform.rotate(objet,45),(-1,1) :pygame.transform.rotate(objet,135),(-1,-1) :pygame.transform.rotate(objet,225),(1,-1) :pygame.transform.rotate(objet,315)}

        GameConfig.BOUCLIER = [pygame.image.load('Images/Personnage_principale/Armes/bouclier1.png'),pygame.image.load('Images/Personnage_principale/Armes/bouclier2.png'),pygame.image.load('Images/Personnage_principale/Armes/bouclier3.png')]
        GameConfig.TAILLE_BOUCLIER = []

        for el in GameConfig.BOUCLIER :
            GameConfig.TAILLE_BOUCLIER.append((el.get_width(),el.get_height())) 

        #(1,0) : objet, (0,1) :pygame.transform.rotate(objet,90),(-1,0) :pygame.transform.rotate(objet,180),(0,-1) :pygame.transform.rotate(objet,270),(1,1) :pygame.transform.rotate(objet,45),(-1,1) :pygame.transform.rotate(objet,135),(-1,-1) :pygame.transform.rotate(objet,225),(1,-1) :pygame.transform.rotate(objet,315)
        
        GameConfig.ATTAQUE = []
        attaque1 = pygame.image.load('Images/Personnage_principale/Attaque/1.png')
        attaque2 = pygame.image.load('Images/Personnage_principale/Attaque/2.png')
        attaque3 = pygame.image.load('Images/Personnage_principale/Attaque/3.png')
        attaque4 = pygame.image.load('Images/Personnage_principale/Attaque/4.png')

        for el in GameConfig.TAILLE_ARME:
            attaque1_scale = pygame.transform.scale(attaque1,(el[1]*1.5,el[1]*1.5))
            attaque2_scale = pygame.transform.scale(attaque2,(el[1]*1.5,el[1]*1.5))
            attaque3_scale = pygame.transform.scale(attaque3,(el[1]*1.5,el[1]*1.5))
            attaque4_scale = pygame.transform.scale(attaque4,(el[1]*1.5,el[1]*1.5))
            GameConfig.ATTAQUE.append({(0,-1) : [[attaque1_scale,attaque2_scale],[attaque3_scale,attaque4_scale]], (-1,0) : [[pygame.transform.rotate(attaque1_scale,90),pygame.transform.rotate(attaque2_scale,90)],[pygame.transform.rotate(attaque3_scale,90),pygame.transform.rotate(attaque4_scale,90)]],(0,1) :[[pygame.transform.rotate(attaque1_scale,180),pygame.transform.rotate(attaque2_scale,180)],[pygame.transform.rotate(attaque3_scale,180),pygame.transform.rotate(attaque4_scale,180)]],
                                                                                         (1,0) :[[pygame.transform.rotate(attaque1_scale,270),pygame.transform.rotate(attaque2_scale,270)],[pygame.transform.rotate(attaque3_scale,270),pygame.transform.rotate(attaque4_scale,270)]],(-1,-1) :[[pygame.transform.rotate(attaque1_scale,45),pygame.transform.rotate(attaque2_scale,45)],[pygame.transform.rotate(attaque3_scale,45),pygame.transform.rotate(attaque4_scale,45)]],
                                                                                         (-1,1) :[[pygame.transform.rotate(attaque1_scale,135),pygame.transform.rotate(attaque2_scale,135)],[pygame.transform.rotate(attaque3_scale,135),pygame.transform.rotate(attaque4_scale,135)]],(1,1) :[[pygame.transform.rotate(attaque1_scale,225),pygame.transform.rotate(attaque2_scale,225)],[pygame.transform.rotate(attaque3_scale,225),pygame.transform.rotate(attaque4_scale,225)]],
                                                                                         (1,-1) :[[pygame.transform.rotate(attaque1_scale,315),pygame.transform.rotate(attaque2_scale,315)],[pygame.transform.rotate(attaque3_scale,315),pygame.transform.rotate(attaque4_scale,315)]]})

        GameConfig.MORT=[pygame.image.load('Images/Mort/mort1.png'),pygame.image.load('Images/Mort/mort2.png'),pygame.image.load('Images/Mort/mort3.png'),pygame.image.load('Images/Mort/mort4.png'),pygame.image.load('Images/Mort/mort5.png'),pygame.image.load('Images/Mort/mort6.png'),pygame.image.load('Images/Mort/mort7.png'),pygame.image.load('Images/Mort/mort8.png'),pygame.image.load('Images/Mort/mort9.png'),pygame.image.load('Images/Mort/mort10.png'),pygame.image.load('Images/Mort/mort11.png'),pygame.image.load('Images/Mort/mort12.png'),pygame.image.load('Images/Mort/mort13.png'),pygame.image.load('Images/Mort/mort14.png')]
        for i in range (len(GameConfig.MORT)):
            GameConfig.MORT[i] = pygame.transform.scale(GameConfig.MORT[i], (GameConfig.MORT_W,GameConfig.MORT_H))
        
        