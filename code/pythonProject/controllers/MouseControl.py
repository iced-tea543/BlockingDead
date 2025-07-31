import math
from utility import distance

import pygame

import models.EntityManager
import models.Entity

characterSpeed = 0.02
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

def onGameMouseUpdate():
    mousePosition = pygame.mouse.get_pos()
    dx, dy = mousePosition[0] - 400, mousePosition[1] - 300

    angle_rad = math.atan2(dy, dx)
    angle_deg = math.degrees(angle_rad)

    if distance((400, 300), mousePosition) < 50 and not models.DataManager.mainCharacter.hurted:
        models.DataManager.mainCharacter.animationIndex = 'Idle'
    elif not models.DataManager.mainCharacter.hurted:
        #reset the frame index to 0 when the mouse is clicked
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP) and event.button == 1:
                models.DataManager.mainCharacter.frameIndex = 0

        if pygame.mouse.get_pressed()[0]:
            # Set the animation index to 'Attack1' (Attack animation)
            models.DataManager.mainCharacter.animationIndex = 'Attack1'
            models.DataManager.mainCharacter.animationInterval = 100
            models.DataManager.mainCharacter.attackDx = dx
            models.DataManager.mainCharacter.attackDy = dy
        else:
            # Set the animation index to 'Run' and adjust the direction based on the angle (Move animation)
            models.DataManager.mainCharacter.animationInterval = 50
            models.DataManager.mainCharacter.animationIndex = 'Run'
            models.DataManager.mainCharacter.direction = int(angle_deg / 45 + 8 if angle_deg / 45 < 0 else angle_deg / 45)
            
            # print(f"Move: {directions[models.DataManager.mainCharacter.direction]} pixels, direction: {models.DataManager.mainCharacter.direction}")
            if models.DataManager.mainCharacter.move(directions[models.DataManager.mainCharacter.direction][0], directions[models.DataManager.mainCharacter.direction][1] * 2):
                models.DataManager.cameraOffsetX += directions[models.DataManager.mainCharacter.direction][0] * 128
                models.DataManager.cameraOffsetY += directions[models.DataManager.mainCharacter.direction][1] * 64
            models.EntityManager.updateZombieRoutes()


def onGameKeyUpdate():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        models.DataManager.runningStatus = 0










    # if keys[pygame.K_LEFT]:
    #     models.DataManager.mainCharacter.setDirection(4)
    #     models.DataManager.mainCharacter.setAnimationIndex('Run')
    #     if models.DataManager.mainCharacter.move(-characterSpeed, 0):
    #         models.DataManager.cameraOffsetX-= 128 * characterSpeed
    #     models.EntityManager.updateZombieRoutes()
    # elif keys[pygame.K_RIGHT]:
    #     models.DataManager.mainCharacter.direction = 0
    #     models.DataManager.mainCharacter.setAnimationIndex('Run')
    #     if models.DataManager.mainCharacter.move(characterSpeed, 0):
    #         models.DataManager.cameraOffsetX+= 128 * characterSpeed
    #     models.EntityManager.updateZombieRoutes()
    # elif keys[pygame.K_UP]:
    #     models.DataManager.mainCharacter.direction = 6
    #     models.DataManager.mainCharacter.setAnimationIndex('Run')
    #     if models.DataManager.mainCharacter.move(0, -characterSpeed*2):
    #         models.DataManager.cameraOffsetY -= 64 * characterSpeed
    #     models.EntityManager.updateZombieRoutes()
    # elif keys[pygame.K_DOWN]:
    #     models.DataManager.mainCharacter.direction = 2
    #     models.DataManager.mainCharacter.setAnimationIndex('Run')
    #     if models.DataManager.mainCharacter.move(0, characterSpeed*2):
    #         models.DataManager.cameraOffsetY += 64 * characterSpeed
    #     models.EntityManager.updateZombieRoutes()