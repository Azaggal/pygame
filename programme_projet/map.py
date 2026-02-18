import pytmx
import pygame

class Map :

    def init():
        Map.DATA_SALLE_DEBUT = pytmx.load_pygame('Tiled/Salle_debut.tmx')
        Map.DATA_SALLE1 = pytmx.load_pygame('Tiled/Salle1.tmx')
        Map.DATA_SALLE2 = pytmx.load_pygame('Tiled/Salle2.tmx')
        Map.DATA_SALLE_BOSS = pytmx.load_pygame('Tiled/Salle_boss.tmx')
        Map.DATA_SALLE_TRESOR=pytmx.load_pygame('Tiled/Salle_tresor.tmx')
        Map.SALLE_COURANTE = 0
        Map.DATA_SALLE_COURANTE = Map.DATA_SALLE_DEBUT
        Map.object_layer_name = "Collisions"  # Nom de la couche d'objets dans Tiled
        Map.MurDebut = []
        Map.Mur1 = []
        Map.Mur2 = []
        Map.MurBoss =[]
        Map.MurTresor = []

        for layer in Map.DATA_SALLE_DEBUT.visible_layers:
                if isinstance(layer, pytmx.TiledObjectGroup) and layer.name == Map.object_layer_name:
                    for obj in layer:
                        if obj.type == "Mur":  # Filtrer par nom ou type (facultatif)
                            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                            Map.MurDebut.append(rect)  
        
        for layer in Map.DATA_SALLE1.visible_layers:
                if isinstance(layer, pytmx.TiledObjectGroup) and layer.name == Map.object_layer_name:
                    for obj in layer:
                        if obj.type == "Mur":  # Filtrer par nom ou type (facultatif)
                            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                            Map.Mur1.append(rect) 

        for layer in Map.DATA_SALLE2.visible_layers:
                if isinstance(layer, pytmx.TiledObjectGroup) and layer.name == Map.object_layer_name:
                    for obj in layer:
                        if obj.type == "Mur":  # Filtrer par nom ou type (facultatif)
                            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                            Map.Mur2.append(rect) 

        for layer in Map.DATA_SALLE_BOSS.visible_layers:
                if isinstance(layer, pytmx.TiledObjectGroup) and layer.name == Map.object_layer_name:
                    for obj in layer:
                        if obj.type == "Mur":  # Filtrer par nom ou type (facultatif)
                            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                            Map.MurBoss.append(rect) 

        for layer in Map.DATA_SALLE_TRESOR.visible_layers:
                if isinstance(layer, pytmx.TiledObjectGroup) and layer.name == Map.object_layer_name:
                    for obj in layer:
                        if obj.type == "Mur":  # Filtrer par nom ou type (facultatif)
                            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                            Map.MurTresor.append(rect) 



        Map.Mur = Map.MurDebut  

    
    def advance_state():
        if Map.SALLE_COURANTE == 0:
            Map.DATA_SALLE_COURANTE = Map.DATA_SALLE_DEBUT
            Map.Mur = Map.MurDebut  
        elif Map.SALLE_COURANTE == 1 :
            Map.DATA_SALLE_COURANTE = Map.DATA_SALLE1
            Map.Mur = Map.Mur1
        elif Map.SALLE_COURANTE == 2 :
            Map.DATA_SALLE_COURANTE = Map.DATA_SALLE2
            Map.Mur = Map.Mur2
        elif Map.SALLE_COURANTE == 3 :
            pygame.mixer.music.fadeout(2000)
            pygame.time.delay(2000)
            pygame.mixer.music.load("Musique/boss.ogg")
            pygame.mixer.music.play(-1)
            Map.DATA_SALLE_COURANTE = Map.DATA_SALLE_BOSS
            Map.Mur = Map.MurBoss
        elif Map.SALLE_COURANTE == 4 :
            pygame.mixer.music.fadeout(2000)
            pygame.time.delay(2000)
            pygame.mixer.music.load("Musique/fin.ogg")
            pygame.mixer.music.play()
            Map.DATA_SALLE_COURANTE = Map.DATA_SALLE_TRESOR
            Map.Mur = Map.MurTresor
    
