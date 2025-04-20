import math
import random
import pygame
from New_Class import *
import player_functions
from pygame import mixer
clock = pygame.time.Clock()
level_display_time = game_over_time = 100
enemy_count = 0
pygame.init()
pygame.font.init()

gameover_sound = mixer.Sound("game-over.wav")
background_music = mixer.Sound("game-background.wav")
bulet_sound = mixer.Sound("bullet-fire.wav")
bullet_hit_sound = mixer.Sound("enemy-hit.wav")
#Creating objects from the actor class, with different coordinates and movement speed
game_over_image = actors('game-over.png', 250, 200, 0, 0, 0, 0,0,0,"Ready")
level1_image = actors('level-1.png', 250, 100, 0, 0, 0, 0,0,0,"Active")
main_actor = actors('Defender.png', 368, 536, 5, 0, 0, 5,736,0,"Ready")
background = actors('Background.png', 0, 0, 0, 0, 0, 0,0,0,"Ready")
bullet_level = actors('bullet.png', 368, 500, 24, 12, 0, 1,0,0,"Ready")
test_bullet = actors('bullet.png', 368, 500, 0, 0, 0, 1,0,0,"Ready")
total_score1 = show_different_values(10, 10) #actors('SCORE', 10, 10, 0, 0, 0, 1)
enemy_level1 = []
#Create Level1 enemies using a for loop in the list again appending an object from the actor class
enemy_level1_num = 6
bullet_level1 = []
bullet_level1.append(actors('bullet.png', 368, 500, 20, -12, 0, 1,0,0,"Ready"))
bullet_level1.append(actors('bullet.png', 368, 500, -7, -3, 0, 1,0,0,"Ready"))
bullet_level1.append(actors('bullet.png', 368, 500, 44, -3, 0, 1,0,0,"Ready"))
background_music.play(-1)
for i in range(enemy_level1_num):
    rand_intx = random.randint(50, 750)
    rand_numy = random.randint(0, 30)
    rand_rlimit = random.randint(rand_intx, 750)
    rand_llimit = random.randint(0, rand_numy)
    #This code create a new enemy into the list using the actor class
    enemy_level1.append(actors('ufo3.png', rand_intx, rand_numy, 8, 20, 0, 2,rand_rlimit,rand_llimit,"Ready"))
    if i == 1:
        #generate a test nemy for debugging
        testenemy = actors('ufo.png', rand_intx, rand_numy +10, 8, 30, 0, 2,1,1,"Ready")
icon = pygame.image.load('spaceship.png')
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(icon)

# The below while loop is the Game window, because it is running infitely and anything to be persisten must me mention here

moveleft = moveright =0
#moveright = 0
running = True
while running:
    main_actor.screen.fill((199, 34, 44))
    background.actor_location()
    level_display_time -= 1
    if level1_image.state == "Active":
        if level_display_time > 0:
            level1_image.actor_location()
            if level_display_time == 0:
                level1_image.state = "In-Active"
                level_display_time = 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Checking the Key press and detecting,which key is pressed and what action to take after the key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveright = main_actor.move_in_xaxis
            if event.key == pygame.K_LEFT:
                moveleft = - main_actor.move_in_xaxis
            #When and key A is pressed, call the bullet_state function from the player function file to change the status to "Fire"
            if event.key == pygame.K_a:
                for i in range(len(bullet_level1)):
                    if bullet_level1[i].state == "Ready":
                        bullet_level1[i].state = player_functions.bullet_status()
                        bullet_level1[i].appear_in_xaxis, bullet_level1[i].appear_in_yaxis = player_functions.fire_bullet(
                            main_actor.appear_in_xaxis, main_actor.appear_in_yaxis,bullet_level1[i].move_in_xaxis,bullet_level1[i].move_in_yaxis)
                        bulet_sound.play()
                        break

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                moveleft = 0
                moveright = 0

    #Make the move value as 0 when side walls are hit, hence stop the movement of the actor when arro key is pressed at the wall
    if main_actor.appear_in_xaxis >= 736:# or main_actor.appear_in_xaxis <= 0:
        #move = 0
        moveright = 0
    elif main_actor.appear_in_xaxis <= 0:
        moveleft = 0


    # Moving our Defender actor when left or righ keys are pressed with the value of Move
    main_actor.appear_in_xaxis = main_actor.appear_in_xaxis + moveleft + moveright
    #When Key A is pressed the bullet state changed to "Fire", and then the bullet moves until the state is Fire
    #print(f"second bullet state check{bullet_level1.state}")
    for i in range(len(bullet_level1)):
        if bullet_level1[i].state == "Fire":
            bullet_level1[i].appear_in_yaxis, bullet_level1[i].state = player_functions.move_bullet(
                bullet_level1[i].appear_in_yaxis, bullet_level1[i].state)
            bullet_level1[i].bullet_location()
            for i in range(enemy_level1_num):
                for j in range(len(bullet_level1)):
                    iscollision1 = player_functions.iscollision(enemy_level1[i].appear_in_xaxis,
                                                                enemy_level1[i].appear_in_yaxis,
                                                                bullet_level1[j].appear_in_xaxis,
                                                                bullet_level1[j].appear_in_yaxis)
                    if iscollision1:
                        bullet_hit_sound.play()
                        bullet_level1[j].state, enemy_level1[i].appear_in_xaxis, enemy_level1[i].appear_in_yaxis, \
                        enemy_level1[i].rlimit, enemy_level1[i].llimit, main_actor.score \
                                         = player_functions.bullet_impact(bullet_level1[j].state, enemy_level1[i].appear_in_xaxis, enemy_level1[i].appear_in_yaxis,\
                                                                                   enemy_level1[i].rlimit,enemy_level1[i].llimit, main_actor.score)
    main_actor.actor_location()
    total_score1.show_score(main_actor.score, total_score1.appear_in_xaxis, total_score1.appear_in_xaxis)
    for i in range(enemy_level1_num):
        game_over = player_functions.game_over_check(enemy_level1[i].appear_in_xaxis, enemy_level1[i].appear_in_yaxis,\
                       main_actor.appear_in_xaxis, main_actor.appear_in_yaxis)
        if game_over:

            game_over_time -= 1
            if game_over_time > 0:
                gameover_sound.play()
            print(game_over_time)
            for i in range(enemy_level1_num):
                enemy_level1[i].game_over()
            for i in range(len(bullet_level1)):
                bullet_level1[i].state = "Ready"
            main_actor.game_over()
            game_over_image.actor_location()

        enemy_level1[i].enemy_movement()
        enemy_level1[i].actor_location()

    pygame.display.flip()
