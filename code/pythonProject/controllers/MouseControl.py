import math

import pygame

import models.EntityManager
import views.Entity

CAMERA_SPEED = 0.2
directions = [
    (CAMERA_SPEED, 0),
    (CAMERA_SPEED / 2**0.5, CAMERA_SPEED / 2**0.5),
    (0, CAMERA_SPEED),
    (-CAMERA_SPEED / 2**0.5, CAMERA_SPEED / 2**0.5),
    (-CAMERA_SPEED, 0),
    (-CAMERA_SPEED / 2**0.5, -CAMERA_SPEED / 2**0.5),
    (0, -CAMERA_SPEED),
    (CAMERA_SPEED / 2**0.5, -CAMERA_SPEED / 2**0.5),
]

def mouseUpdate():
    if pygame.mouse.get_pressed()[0]:
        mousePosition = pygame.mouse.get_pos()
        dx, dy = mousePosition[0] - 400, mousePosition[1] - 300

        angle_rad = math.atan2(dy, dx)
        angle_deg = math.degrees(angle_rad)

        models.EntityManager.mainCharacter.animationIndex = 'Run'
        models.EntityManager.mainCharacter.direction = int(angle_deg / 45 + 8 if angle_deg / 45 < 0 else angle_deg / 45)

        views.Entity.camera_offset_x += directions[models.EntityManager.mainCharacter.direction][0]
        views.Entity.camera_offset_y += directions[models.EntityManager.mainCharacter.direction][1]

    else:
        models.EntityManager.mainCharacter.animationIndex = 'Idle'

def keyUpdate():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        models.EntityManager.mainCharacter.setDirection(4)
        models.EntityManager.mainCharacter.setAnimationIndex('Run')

        models.EntityManager.mainCharacter.move(-0.001, 0)
        views.Entity.camera_offset_x-= 128 * 0.001
    elif keys[pygame.K_RIGHT]:
        models.EntityManager.mainCharacter.direction = 0
        models.EntityManager.mainCharacter.setAnimationIndex('Run')
        models.EntityManager.mainCharacter.move(0.001, 0)
        views.Entity.camera_offset_x+= 128 * 0.001
    elif keys[pygame.K_UP]:
        models.EntityManager.mainCharacter.direction = 6
        models.EntityManager.mainCharacter.setAnimationIndex('Run')
        models.EntityManager.mainCharacter.move(0, -0.002)
        views.Entity.camera_offset_y -= 64 * 0.002
    elif keys[pygame.K_DOWN]:
        models.EntityManager.mainCharacter.direction = 2
        models.EntityManager.mainCharacter.setAnimationIndex('Run')
        models.EntityManager.mainCharacter.move(0, 0.002)
        views.Entity.camera_offset_y += 64 * 0.002