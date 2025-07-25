from views.Creature import Creature
import models.EntityManager

class Zombie(Creature):
    def __init__(self, animationDir):
        super().__init__(animationDir, 6, [0, 0])

    def spawn(self):
        pass

    def update(self):
        super().update()
        self.move(0.001, 0.001)
