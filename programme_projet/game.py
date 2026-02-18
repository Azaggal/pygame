import pygame
from random import randint
from player import *
from game_config import *
from game_state import *    
from move import *
from enemy_distance_lent import *
from enemy_distance_rapide import *
from map import *
from enemy_corps_a_corps import *
from enemy_boss import *
from mort import *
from mannequin import *

def get_next_move(): 
    next_move = Move()  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        next_move.right=True    
    if keys[pygame.K_q]:
        next_move.left = True
    if keys[pygame.K_s]:
        next_move.down=True    
    if keys[pygame.K_z]:
        next_move.up = True
    if keys[pygame.K_UP]:
        next_move.fire_up = True
    if keys[pygame.K_LEFT]:
        next_move.fire_left = True 
    if keys[pygame.K_DOWN]:
        next_move.fire_down = True
    if keys[pygame.K_RIGHT]:
        next_move.fire_right = True     
    return next_move

   


def game_loop(window):
    game_state=GameState()
    quitting = False
    while not quitting :
        for event in pygame . event .get () :
            if event . type == pygame . QUIT :
                quitting = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    game_state.interaction()
                elif event.key == pygame.K_ESCAPE:
                    game_state.echap()

            if event.type == pygame.MOUSEBUTTONDOWN :
                game_state.clique()
                    


        next_move = get_next_move()
        game_state.advance_state(next_move) 
        game_state.draw(window,Map.DATA_SALLE_COURANTE)

        pygame.time.delay(20)
        pygame.display.update()
    
    

if __name__ == "__main__" :
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Musique/donjon.ogg")
    pygame.mixer.music.play(-1)
    window = pygame.display.set_mode((GameConfig.WINDOW_W, GameConfig.WINDOW_H ))
    GameConfig.init()
    Map.init()
    Player.init_sprites()
    Projectile.init_sprites()
    Enemy_Distance_Lent.init_sprites()
    Enemy_Distance_Rapide.init_sprites()
    Enemy_Corps_A_Corps.init_sprites()
    Enemy_Boss.init_sprites()
    Mannequin.init_sprites()
    Mort.init_sprites()
    pygame . display . set_caption ("The Last Defender")
    game_loop(window)
    pygame.quit()
    quit()