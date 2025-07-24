import pygame
import os

from utility import *

camera_offset_x = -(400-64)
camera_offset_y = -(300-64)

class Entity(pygame.sprite.Sprite):
    def __init__(self, animationDir, animationIndex, animationSpeed, position):
        super().__init__()

        self.animationDir = animationDir
        self.animationIndex = animationIndex
        self.animationSpeed = animationSpeed

        self.spriteSheet = {}
        self.direction = 0
        self.frameIndex = 0
        self.lastUpdateTime = pygame.time.get_ticks()

        self.loadAnimation()

        self.position = [int(position[0]), int(position[1])]

    def loadAnimation(self):
        for fileName in os.listdir(self.animationDir):
            self.spriteSheet[fileName[:fileName.find('.')]] = pygame.image.load(os.path.join(self.animationDir, fileName)).convert_alpha()

    def move(self, dx, dy):
        print(self.getPosition())
        self.position[0] += dx
        self.position[1] += dy

        self.updateScreenPosition()

    def updateScreenPosition(self):
        actualX = self.position[0]

        if int(self.position[1]) % 2 != 0:
            actualX -= 0.5

        screenX, screenY = iso_to_screen_staggered(
            actualX, self.position[1], 128, 128,
            camera_offset_x, camera_offset_y
        )

        self.rect.x = int(screenX)
        self.rect.y = int(screenY - (128 - 64))

    def getPosition(self):
        actualX = self.position[0]

        if int(self.position[1]) % 2 != 0:
            actualX -= 0.5
        return (actualX, self.position[1])

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.lastUpdateTime >= self.animationSpeed:
            self.lastUpdateTime = now
            self.frameIndex = (self.frameIndex + 1) % 15
            rect = pygame.Rect(self.frameIndex * 128, self.direction * 128, 128, 128)
            self.image = self.spriteSheet[self.animationIndex].subsurface(rect)


            self.image = self.image.subsurface(40, 35, 70, 55)

            self.rect = self.image.get_rect()

        # 更新屏幕位置
        self.updateScreenPosition()

    def setAnimationIndex(self, animationIndex):
        self.animationIndex = animationIndex

    def setDirection(self, direction):
        self.direction = direction


class Chest(Entity):
    def __init__(self, animationDir):
        super().__init__(animationDir)

    def spawn(self):
        pass