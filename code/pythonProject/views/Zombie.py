from views.Creature import Creature

from utility import *

import models.DataManager
import models.EntityManager

class Zombie(Creature):
    def __init__(self, animationDir, position=[0, 0]):
        super().__init__(animationDir, 6, position)

    def update(self):
        super().update()
        if distance(self.position, models.EntityManager.mainCharacter.position) < 50:
            if len(self.route) > 0:
                self.setAnimationIndex('Run')
                #self.setDirection(self.getDirection(self.route[0]))
                self.move(self.dx, self.dy)
                self.way = (self.way[0] - self.dx, self.way[1] - self.dy)
                if self.way[0] <= 0 and self.way[1] <= 0:
                    self.route.pop(0)
                    if len(self.route) > 0:
                        self.dx, self.dy = self.route[0][0] * 0.003, self.route[0][1] * 0.006
                        self.way = (self.route[0][0], self.route[0][1] )
            else:
                self.setAnimationIndex('Idle')

        
    def updateRoute(self):
        print(f"Zombie at {self.position} updating route to main character at {models.EntityManager.mainCharacter.position}")
        self.route = bfs(tuple(self.position), tuple(models.EntityManager.mainCharacter.position), [])
        if len(self.route) > 0:
            self.dx, self.dy = self.route[0][0] * 0.003, self.route[0][1] * 0.006
            self.way = (self.route[0][0], self.route[0][1])
        #print(f"Zombie at {self.position} set initial way to {self.way} with dx={self.dx}, dy={self.dy}")