import pygame
from views.Entity import Entity

class Creature(Entity):
    def __init__(self, animationDir, healthMax, position):
        super().__init__(animationDir, 'Idle', 50, position)
        self.healthMax = healthMax
        self.dead = False
        self.health = healthMax

    def update(self):
        if self.dead:
            return
        
        if self.health > 0:
            super().update()
        
        if self.health <= 0 and self.animationIndex != 'Die':
            self.animationIndex = 'Die'
            self.frameIndex = 0

        if self.animationIndex == 'Die':
            print(f"Creature {self.animationDir} at {self.position} is dying, frameIndex: {self.frameIndex}")
            if self.frameIndex >= 14:
                self.dead = True
                return
            else:
                now = pygame.time.get_ticks()
                if now - self.lastUpdateTime >= self.animationInterval:
                    self.lastUpdateTime = now
                    self.frameIndex += 1
                    self.updateAnimation()
                return

class Player(Creature):
    def __init__(self, animationDir, position = [0, 0]):
        super().__init__(animationDir, 6, position)

    def move(self, dx, dy):
        print(self.position)
        return super().move(dx, dy)
