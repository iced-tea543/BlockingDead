import math
from utility import distance

import pygame

import models.EntityManager
import views.Entity

characterSpeed = 0.003
directions = [
    (characterSpeed, 0),
    (characterSpeed / 2**0.5, characterSpeed / 2**0.5),
    (0, characterSpeed),
    (-characterSpeed / 2**0.5, characterSpeed / 2**0.5),
    (-characterSpeed, 0),
    (-characterSpeed / 2**0.5, -characterSpeed / 2**0.5),
    (0, -characterSpeed),
    (characterSpeed / 2**0.5, -characterSpeed / 2**0.5),
]

def mouseUpdate():
    mousePosition = pygame.mouse.get_pos()
    dx, dy = mousePosition[0] - 400, mousePosition[1] - 300

    angle_rad = math.atan2(dy, dx)
    angle_deg = math.degrees(angle_rad)

    if distance((400, 300), mousePosition) < 50:
        models.EntityManager.mainCharacter.animationIndex = 'Idle'
    else:
        models.EntityManager.mainCharacter.animationIndex = 'Run'
        models.EntityManager.mainCharacter.direction = int(angle_deg / 45 + 8 if angle_deg / 45 < 0 else angle_deg / 45)
        # print(f"Move: {directions[models.EntityManager.mainCharacter.direction]} pixels, direction: {models.EntityManager.mainCharacter.direction}")
        if models.EntityManager.mainCharacter.move(directions[models.EntityManager.mainCharacter.direction][0], directions[models.EntityManager.mainCharacter.direction][1] * 2):
            models.DataManager.cameraOffsetX += directions[models.EntityManager.mainCharacter.direction][0] * 128
            models.DataManager.cameraOffsetY += directions[models.EntityManager.mainCharacter.direction][1] * 64
        models.EntityManager.updateZombieRoutes()


def keyUpdate():
    speed = 0.003
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        models.EntityManager.mainCharacter.setDirection(4)
        models.EntityManager.mainCharacter.setAnimationIndex('Run')
        if models.EntityManager.mainCharacter.move(-speed, 0):
            models.DataManager.cameraOffsetX-= 128 * speed
        models.EntityManager.updateZombieRoutes()
    elif keys[pygame.K_RIGHT]:
        models.EntityManager.mainCharacter.direction = 0
        models.EntityManager.mainCharacter.setAnimationIndex('Run')
        if models.EntityManager.mainCharacter.move(speed, 0):
            models.DataManager.cameraOffsetX+= 128 * speed
        models.EntityManager.updateZombieRoutes()
    elif keys[pygame.K_UP]:
        models.EntityManager.mainCharacter.direction = 6
        models.EntityManager.mainCharacter.setAnimationIndex('Run')
        if models.EntityManager.mainCharacter.move(0, -speed*2):
            models.DataManager.cameraOffsetY -= 64 * speed
        models.EntityManager.updateZombieRoutes()
    elif keys[pygame.K_DOWN]:
        models.EntityManager.mainCharacter.direction = 2
        models.EntityManager.mainCharacter.setAnimationIndex('Run')
        if models.EntityManager.mainCharacter.move(0, speed*2):
            models.DataManager.cameraOffsetY += 64 * speed
        models.EntityManager.updateZombieRoutes()