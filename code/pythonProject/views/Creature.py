from views.Entity import Entity


class Creature(Entity):
    def __init__(self, animationDir, healthMax, position):
        super().__init__(animationDir, 'Idle', 50, position)
        self.healthMax = healthMax

class Player(Creature):
    def __init__(self, animationDir, position = [0, 0]):
        super().__init__(animationDir, 6, position)

    def update(self):
        super().update()

class Zombie(Creature):
    def __init__(self, animationDir):
        super().__init__(animationDir, 6, [0, 0])

    def spawn(self):
        pass

