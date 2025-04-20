import random
import math
bullet_state = 'Ready'


def fire_bullet(xaxis, yaxis, movex, movey):
    xaxis = xaxis + movex
    yaxis = yaxis + movey
    return xaxis, yaxis

def bullet_status():
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
    xaxisdiff = enemyx- bulletx
    yaxisdiff = enemyy- bullety
    xaxisdiffsqr = math.pow(enemyx- bulletx, 2)
    yaxisdiffsqr = math.pow(enemyy- bullety, 2)
    distance = math.sqrt((math.pow(enemyx- bulletx, 2)) + (math.pow(enemyy- bullety, 2)))
    if distance < 21:
        return True
    else:
        return False
#This Function acts to ascertain what happens when the bllet hit an enemy
#This reset that enemy position and also changes the bullet state to "Ready" which means that the key A will again Fire a bullet
#This also changes the bullet x axis and Y axis so that bullet remain hidden and not shown
#This function also increases by a value(in this case it is 1 when the bullet hit an enemy
def game_over_check(enemyX, enemyY, defenderX, defenderY):
    if enemyY >= defenderY:
        return True

def bullet_impact(bullet_state, enemyx, enemyy,new_rlimit,new_llimit, score):
    score += 1
    xaxis_enemy = random.randint(50, 750)
    yaxis_enemy = random.randint(0, 50)
    xaxis_limit = random.randint(xaxis_enemy, 750)
    if xaxis_limit - xaxis_enemy < 10:
        xaxis_limit = xaxis_enemy + 10
    yaxis_limit = random.randint(0, yaxis_enemy)
    bullet_state, enemyx, enemyy,new_rlimit,new_llimit = ("Ready",xaxis_enemy,yaxis_enemy,xaxis_limit,yaxis_limit)
    return bullet_state, enemyx, enemyy,new_rlimit,new_llimit, score

##All Test Fuctions for debugging and testing new features##



