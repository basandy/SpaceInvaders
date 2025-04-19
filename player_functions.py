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
    xaxisdiff = enemyx- bulletx
    yaxisdiff = enemyy- bullety
    xaxisdiffsqr = math.pow(enemyx- bulletx, 2)
    yaxisdiffsqr = math.pow(enemyy- bullety, 2)
    distance = math.sqrt((math.pow(enemyx- bulletx - 24, 2)) + (math.pow(enemyy- bullety + 12, 2)))
    #print(f"Distance between the Bullet and Enemy is: {distance}")
    if distance < 21:
        return True, distance, xaxisdiff, yaxisdiff, xaxisdiffsqr, yaxisdiffsqr,enemyy, bullety
    else:
        return False, distance, xaxisdiff, yaxisdiff, xaxisdiffsqr, yaxisdiffsqr, enemyy, bullety
#This Function acts to ascertain what happens when the bllet hit an enemy
#This reset that enemy position and also changes the bullet state to "Ready" which means that the key A will again Fire a bullet
#This also changes the bullet x axis and Y axis so that bullet remain hidden and not shown
#This function also increases by a value(in this case it is 1 when the bullet hit an enemy
def game_over_check(enemyX, enemyY, defenderX, defenderY):
    if enemyY >= defenderY:
        return True

def bullet_impact(bullet_state, enemyx, enemyy,new_rlimit,new_llimit, score, bulletx, bullety):
    score += 1
    xaxis_enemy = random.randint(50, 750)
    yaxis_enemy = random.randint(0, 50)
    xaxis_limit = random.randint(xaxis_enemy, 750)
    yaxis_limit = random.randint(0, yaxis_enemy)
    bullet_state, enemyx, enemyy,new_rlimit,new_llimit, bulletx, bullety = ("Ready",xaxis_enemy,yaxis_enemy,xaxis_limit,yaxis_limit,0,400)
    return bullet_state, enemyx, enemyy,new_rlimit,new_llimit, score, bulletx, bullety


