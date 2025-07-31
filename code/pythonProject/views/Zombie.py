from views.Creature import Creature

from utility import *

import models.EntityManager

class Zombie(Creature):
    def __init__(self, animationDir, position=Vec2d(0, 0), healthMax=1, speed=0.02):
        super().__init__(animationDir, healthMax, position)
        self.attacking = False
        self.attackDistance = 0.5
        self.speed = speed

    def update(self):
        super().update()

        #Dead event
        if self.health <= 0:
            return
        
        #Hurted event
        if self.hurted:
            return
        
        if self.attacking and self.animationIndex != 'Attack1':
            self.animationIndex = 'Attack1'
            self.frameIndex = 0
            self.animationInterval = 100
        
        if self.animationIndex == 'Attack1' and self.frameIndex == 7:
            if distance(self.position, models.EntityManager.mainCharacter.position) < self.attackDistance:
                models.EntityManager.mainCharacter.hurted = True
                print(f"Zombie {self.animationDir} at {self.position} attacked player at {models.EntityManager.mainCharacter.position}, player health: {models.EntityManager.mainCharacter.health}")


        if self.animationIndex == 'Attack1':
            #print(f"Creature {self.animationDir} at {self.position} is dying, frameIndex: {self.frameIndex}")
            if self.frameIndex >= 14:
                self.animationIndex = 'Idle'
                self.frameIndex = 0
                self.attacking = False
            return
            

        if distance(self.position, models.EntityManager.mainCharacter.position) < self.attackDistance:
            self.attacking = True

        #Move towards the player if nothing happens
        if distance(self.position, models.EntityManager.mainCharacter.position) < 50:
            if len(self.route) > 0:
                self.setAnimationIndex('Run')
                #self.setDirection(self.getDirection(self.route[0]))
                self.move(self.dx, self.dy)
                self.way = (self.way[0] - self.dx, self.way[1] - self.dy)
                if self.way[0] <= 0 and self.way[1] <= 0:
                    self.route.pop(0)
                    if len(self.route) > 0:
                        self.dx, self.dy = self.route[0][0] * self.speed, self.route[0][1] * self.speed * 2
                        self.way = (self.route[0][0], self.route[0][1])
            #BFS would not work if the zombie is too close to the player
            elif abs(self.position[0] - models.EntityManager.mainCharacter.position[0]) > 0.5:
                self.setAnimationIndex('Run')
                self.move(-abs(self.position[0] - models.EntityManager.mainCharacter.position[0]) / (self.position[0] - models.EntityManager.mainCharacter.position[0]) * self.speed, 0)
            elif abs(self.position[1] - models.EntityManager.mainCharacter.position[1]) > 0.5:
                self.setAnimationIndex('Run')
                self.move(0, -abs(self.position[1] - models.EntityManager.mainCharacter.position[1]) / (self.position[1] - models.EntityManager.mainCharacter.position[1]) * self.speed * 2)
            else:
                self.setAnimationIndex('Idle')

    
    def move(self, dx, dy):
        super().move(dx, dy)        
        if dx > 0:
            self.direction = 0
        elif dy > 0:
            self.direction = 2
        elif dx < 0:
            self.direction = 4
        elif dy < 0:
            self.direction = 6

    def updateRoute(self):
        self.route = bfs(tuple(self.position), tuple(models.EntityManager.mainCharacter.position), [])
        if len(self.route) > 0:
            self.dx, self.dy = self.route[0][0] * self.speed, self.route[0][1] * self.speed * 2
            self.way = (self.route[0][0], self.route[0][1])
        #print(f"Zombie at {self.position} set initial way to {self.way} with dx={self.dx}, dy={self.dy}")