import pygame
import os

from utility import *

import models.DataManager

camera_offset_x = -(400-64)
camera_offset_y = -(300-64)

class Entity(pygame.sprite.Sprite):
    def __init__(self, animationDir, animationIndex, animationInterval, position):
        super().__init__()

        self.animationDir = animationDir
        self.animationIndex = animationIndex
        self.animationInterval = animationInterval

        #self.spriteSheet = {}
        self.direction = 0
        self.frameIndex = 0

        self.lastUpdateTime = pygame.time.get_ticks()

        #self.loadAnimation()
        
        self.updateAnimation()

        self.position = [int(position[0]), int(position[1])]

    #def loadAnimation(self):
    #    for fileName in os.listdir(self.animationDir):
    #       self.spriteSheet[fileName[:fileName.find('.')]] = pygame.image.load(os.path.join(self.animationDir, fileName)).convert_alpha()

    def move(self, dx, dy):

        self.position[0] += dx
        self.position[1] += dy

        flag = False
        for p1, p2 in models.DataManager.boundaries:
            if pointOnLine(p1, p2, self.position):
                flag = True

        if flag:
            self.position[0] -= dx
            self.position[1] -= dy
            return False

        #self.updateScreenPosition()
        return True
    
    def setPosition(self, position):
        self.position[0] = position[0]
        self.position[1] = position[1]
        #self.updateScreenPosition()

    # def updateScreenPosition(self):
    #     actualX = self.position[0]

    #     if int(self.position[1]) % 2 != 0:
    #         actualX -= 0.5

    #     screenX, screenY = iso_to_screen_staggered(
    #         actualX, self.position[1], 128, 128,
    #         models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY
    #     )

    #     self.rect.x = int(screenX)
    #     self.rect.y = int(screenY - (128 - 64))

    def getScreenPosition(self):
        actualX = self.position[0]

        if int(self.position[1]) % 2 != 0:
            actualX -= 0.5
        return (actualX, self.position[1])

    def updateAnimation(self):
        #rect = pygame.Rect(self.frameIndex * 128, self.direction * 128, 128, 128)
        #self.image = models.DataManager.spriteSheet[self.animationDir][self.animationIndex].subsurface(rect)

        self.image = models.DataManager.spriteSheet[self.animationDir][self.animationIndex][self.direction][self.frameIndex]
        #self.image = self.image.subsurface(30, 25, 80, 65)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.lastUpdateTime >= self.animationInterval:
            self.lastUpdateTime = now
            self.frameIndex = (self.frameIndex + 1) % 15
            self.updateAnimation()

            #self.rect = self.image.get_rect()

        #self.updateScreenPosition()

    def setAnimationIndex(self, animationIndex):
        self.animationIndex = animationIndex

    def setDirection(self, direction):
        self.direction = direction


class Chest(Entity):
    def __init__(self, animationDir):
        super().__init__(animationDir)

    def spawn(self):
        pass