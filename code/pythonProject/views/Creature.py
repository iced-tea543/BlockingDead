import pygame
from utility import *
from views.Entity import Entity
import views.RenderUtility
import models.EntityManager

class Creature(Entity):
    def __init__(self, animationDir, healthMax, position):
        super().__init__(animationDir, 'Idle', 50, position)
        self.healthMax = healthMax

        self.dead = False

        #Events that would block the thread with highest priority (health <= 0, hurted)
        self.health = healthMax
        self.hurted = False

    #Priority ranked from highest to lowest from top to bottom in this function
    def update(self):
        
        #Reset the frame index to 0 when zombie is dying
        if self.health <= 0 and self.animationIndex != 'Die':
            self.animationIndex = 'Die'
            self.frameIndex = 0
        elif self.hurted and self.animationIndex != 'TakeDamage' and self.animationIndex != 'Die':
            self.animationIndex = 'TakeDamage'
            print("taking damage!")
            self.frameIndex = 0
            self.health -= 1

        if self.animationIndex == 'Die':
            #print(f"Creature {self.animationDir} at {self.position} is dying, frameIndex: {self.frameIndex}")
            if self.frameIndex >= 14:
                self.dead = True
                return
        elif self.animationIndex == 'TakeDamage':
            if self.frameIndex >= 14:
                self.hurted = False
                self.frameIndex = 0
        
        super().update()

class Player(Creature):
    def __init__(self, animationDir, position = Vec2d(0, 0)):
        super().__init__(animationDir, 6, position)
        self.attackDx = 0
        self.attackDy = 0

    def move(self, dx, dy):
        #print(self.position)
        return super().move(dx, dy)
    
    def update(self):
        if self.animationIndex == 'Attack1' and self.frameIndex == 0:
            for zombie in models.EntityManager.zombies:
                screenX, screenY = iso_to_screen_staggered(*zombie.getScreenPosition(), 128, 64,models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY)
                #zombie.hurted = True
                blitX = screenX
                blitY = screenY - (55 - 64)
                
                zombieRect = pygame.Rect(blitX, blitY, 70, 55)

                if zombieRect.clipline((380, 280), (380 + self.dx, 280 + self.dy)):
                    print(f"Zombie at {zombie.getScreenPosition()} is hurted by player at {self.getScreenPosition()}")
                    zombie.hurted = True
                
                pygame.draw.rect(views.RenderUtility.SCREEN, (245, 155, 0), zombieRect, width = 2)
        return super().update()
