import random
import pygame
import datetime
#pygame.init()
pygame.font.init()

class actors():
    screen = pygame.display.set_mode((800, 600))
    #This function assigns different parameter to any new object, with location and movement
    #This can also be used to create anew new static image and show it on screen on demand
    def __init__(self, actorimage,appear_in_xaxis, appear_in_yaxis, move_in_xaxis,move_in_yaxis, score, life,rlimit, llimit):
        self.actorimage = actorimage
        self.appear_in_xaxis = appear_in_xaxis
        self.appear_in_yaxis = appear_in_yaxis
        self.move_in_xaxis = move_in_xaxis
        self.move_in_yaxis = move_in_yaxis
        self.score = score
        self.life = life
        self.rlimit = rlimit
        self.llimit = llimit

    def __str__(self):
        return f"The player class access for testing"
    def actor_location(self):
        # Load the image
        player_image = pygame.image.load(self.actorimage)
        # Draw the image at the given position
        actors.screen.blit(player_image, (self.appear_in_xaxis, self.appear_in_yaxis))
        return player_image
    #This function changes the movement value of an object when it either side of the screen wall, currently used only for enemies
    def enemy_movement(self):
        # Reverse direction if hitting screen boundaries
        if self.appear_in_xaxis >= self.rlimit:  # Right boundary
            self.move_in_xaxis = -self.move_in_xaxis
            self.appear_in_yaxis += self.move_in_yaxis
        if self.appear_in_xaxis <= self.llimit:  # Left boundary
            self.move_in_xaxis = -self.move_in_xaxis
            self.appear_in_yaxis += self.move_in_yaxis
        # Update enemy movement
        self.appear_in_xaxis += self.move_in_xaxis
        return self.appear_in_xaxis, self.appear_in_yaxis, self.rlimit, self.llimit
    #The function to move the bullet toward Y axis by decreasing theY Axis value
    def bullet_movement(self, bullet_yaxis):
        bullet_yaxis = bullet_yaxis - self.move_in_yaxis
        return bullet_yaxis
    #This function shows teh bullet location after change in Y axis, this is cereated because action location was not feasible
    #This can be checked later if implemeted throught he actor location function
    def  bullet_location(self, bullet_xaxis, bullet_yaxis):
        player_image = pygame.image.load(self.actorimage)
        actors.screen.blit(player_image, (bullet_xaxis + 24, bullet_yaxis - 12))
    #Unused function to test any object movement, currently created to check the bullet movement
    def test_movement(self):

        if self.appear_in_xaxis >= self.rlimit:  # Right boundary
            self.move_in_xaxis = -self.move_in_xaxis
            self.appear_in_yaxis += self.move_in_yaxis
        if self.appear_in_xaxis <= self.llimit:  # Left boundary
            self.move_in_xaxis = -self.move_in_xaxis
            self.appear_in_yaxis += self.move_in_yaxis
        self.appear_in_xaxis += self.move_in_xaxis
        return self.appear_in_xaxis, self.appear_in_yaxis, self.rlimit, self.llimit

    #This is make make move value of an actor as 0 when Game over condition is achieved, Use any actor and call this method to make te move values as 0
    def game_over(self):
        self.move_in_xaxis = 0
        self.move_in_yaxis = 0



class show_different_values(actors):
    font = pygame.font.Font("freesansbold.ttf", 20)
    # def __init__(self, actorimage,appear_in_xaxis, appear_in_yaxis, move_in_xaxis,move_in_yaxis, score, life):
    #     super().__init__(actorimage,appear_in_xaxis, appear_in_yaxis, move_in_xaxis,move_in_yaxis, score, life)
    def __init__(self,appear_in_xaxis, appear_in_yaxis):
        self.appear_in_xaxis = appear_in_xaxis
        self.appear_in_xaxis = appear_in_yaxis

        #super().__init__(appear_in_xaxis, appear_in_yaxis)

    def show_score(self, total_score, scoreX, scoreY):
        score_text = self.font.render("score : " + str(total_score), True, (255, 255, 255))
        self.screen.blit(score_text, (scoreX, scoreY))


