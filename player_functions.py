import random
import math
bullet_state = 'Ready'


def fire_bullet(xaxis, yaxis):
    global bullet_xaxis, bullet_yaxis
    bullet_xaxis = xaxis
    bullet_yaxis = yaxis
    return bullet_xaxis, bullet_yaxis


def bullet_status():
    global bullet_state
    bullet_state = "Fire"
    return bullet_state


def move_bullet(bullet_y, state):
    bullet_y = bullet_y - 15
    if bullet_y <= 0:
        state = 'Ready'
        bullet_y = 0
    return bullet_y, state

#Calculate the distance between bullet and eney to determine a hit
def iscollision(enemyx, enemyy, bulletx, bullety):
    #print(f"Enemy X axis is: {enemyx}; Enemy Y axis is: {enemyy};")
    #print(f"Bullet X axis is: {bulletx}; Bullet Y axis is: {bullety};")

    distance = math.sqrt((math.pow(enemyx- bulletx, 2)) + (math.pow(enemyy- bullety, 2)))
    #print(f"Distance between the Bullet and Enemy is: {distance}")
    if distance < 27:
        return True
    else:
        return False
#This Function acts to ascertain what happens when the bllet hit an enemy
#This reset that enemy position and also changes the bullet state to "Ready" which means that the key A will again Fire a bullet
#This also changes the bullet x axis and Y axis so that bullet remain hidden and not shown
#This function also increases by a value(in this case it is 1 when the bullet hit an enemy
def bullet_impact(bullet_state, enemyx, enemyy, score, bulletx, bullety):
    score += 1
    bullet_state, enemyx, enemyy, bulletx, bullety = ("Ready",random.randint(50, 750),random.random(),0,400)
    #print(score)
    return bullet_state, enemyx, enemyy, score, bulletx, bullety

def game_over_check(enemyX, enemyY, defenderX, defenderY):
    if enemyY >= defenderY:
        return True




