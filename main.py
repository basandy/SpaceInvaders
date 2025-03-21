import math
import random
import pygame
from New_Class import *
import player_functions

pygame.init()
pygame.font.init()
#Creating objects from the actor class, with different coordinates and movement speed
game_over_image = actors('game-over.png', 250, 200, 0, 0, 0, 0)
main_actor = actors('Defender.png', 368, 536, 5, 0, 0, 5)
background = actors('Background.png', 0, 0, 0, 0, 0, 0)
bullet_level1 = actors('bullet.png', 368, 500, 0, 0, 0, 1)
total_score1 = show_different_values(10, 10) #actors('SCORE', 10, 10, 0, 0, 0, 1)
enemy_level1 = []
#Create Level1 enemies using a for loop in the list again appending an object from the actor class
enemy_level1_num = 1

for i in range(enemy_level1_num):
    rand_intx = random.randint(50, 750)
    rand_numy = random.randint(0, 30)
    #This code create a new enemy into the list using the actor class
    enemy_level1.append(actors('ufo3.png', rand_intx, rand_numy, 8, 20, 0, 2))
    print( f"First run for index {i}, X value is {rand_intx} AND Y value is {rand_numy} and Length of the arracy is {len(enemy_level1)}")
    if i == 1:
        #generate a test nemy for debugging
        testenemy = actors('ufo.png', rand_intx, rand_numy +10, 8, 30, 0, 2)
icon = pygame.image.load('spaceship.png')
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(icon)

# The below while loop is the Game window, because it is running infitely and anything to be persisten must me mention here
running = True
move = 0
player_speed = 0.5
bullet_yaxis = 400
bullet_xaxis = 0
bullet_state = 'Ready'
while running:
    main_actor.screen.fill((199, 34, 44))
    background.actor_location()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Checking the Key press and detecting,which key is pressed and what action to take after the key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move = main_actor.move_in_xaxis
            if event.key == pygame.K_LEFT:
                move = - main_actor.move_in_xaxis
            #When and key A is pressed, call the bullet_state function from the player function file to change the status to "Fire"
            if event.key == pygame.K_a:
                if bullet_state == 'Ready':
                    bullet_state = player_functions.bullet_status()
                    bullet_xaxis, bullet_yaxis = player_functions.fire_bullet(main_actor.appear_in_xaxis,
                                                                              main_actor.appear_in_yaxis)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                move = 0
    #Moving our Defender actor when left or righ keys are pressed with the value of Move
    main_actor.appear_in_xaxis = main_actor.appear_in_xaxis + move
    #Make the move value as 0 when side walls are hit, hence stop the movement of the actor when arro key is pressed at the wall
    if main_actor.appear_in_xaxis >= 736 or main_actor.appear_in_xaxis <= 0:
        move = 0
    #WHen Key A is pressed the bullet state changed to "Fire", and then the bullet moves until the state is Fire

    if bullet_state == "Fire":
        bullet_yaxis, bullet_state = player_functions.move_bullet(bullet_yaxis, bullet_state)
        bullet_level1.bullet_location(bullet_xaxis, bullet_yaxis)
        for i in range(enemy_level1_num):

            iscollision1 = player_functions.iscollision(enemy_level1[i].appear_in_xaxis, enemy_level1[i].appear_in_yaxis, \
                                                        bullet_xaxis, bullet_yaxis)

            if iscollision1:
                bullet_state, enemy_level1[i].appear_in_xaxis, enemy_level1[i].appear_in_yaxis, main_actor.score, bullet_xaxis, \
                bullet_yaxis = player_functions.bullet_impact(bullet_state, enemy_level1[i].appear_in_xaxis, enemy_level1[i].appear_in_yaxis,\
                                                              main_actor.score, bullet_xaxis, bullet_yaxis)

    main_actor.actor_location()
    total_score1.show_score(main_actor.score, total_score1.appear_in_xaxis, total_score1.appear_in_xaxis)
    for i in range(enemy_level1_num):
        game_over = player_functions.game_over_check(enemy_level1[i].appear_in_xaxis, enemy_level1[i].appear_in_yaxis,\
                       main_actor.appear_in_xaxis, main_actor.appear_in_yaxis)
        if game_over:
            for i in range(enemy_level1_num):
                enemy_level1[i].game_over()
            bullet_level1.game_over()
            main_actor.game_over()
            game_over_image.actor_location()
        enemy_level1[i].enemy_movement()
        #enemy_level1[i].test_movement()
        enemy_level1[i].actor_location()
        print(f"x part of {i} is: {enemy_level1[i].appear_in_xaxis} + Y part of {i} is: {enemy_level1[i].appear_in_yaxis}")
        print(f"x part of {i} is Move: {enemy_level1[i].move_in_xaxis} + Y part of{i} is Move: {enemy_level1[i].move_in_yaxis}")
    pygame.display.flip()
