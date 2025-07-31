from views.Creature import *
from views.Zombie import *
import random

mainCharacter = Player('Survivor 2')

#testZombie = Zombie(r"C:\Desktop\BlockDead\2D HD Zombie Rural Tileset\Animations\Spritesheets\With shadow\RuralZombie 1")


zombies = []

def spawnZombie(postion=Vec2d(0, 0)):
    zombie = Zombie(f"RuralZombie {random.randint(1, 5)}", postion, speed=random.randint(5, 15) / 1000)
    zombie.updateRoute()
    zombies.append(zombie)

def updateZombies():
    for zombie in zombies:
        zombie.update()
        if zombie.dead:
           zombies.remove(zombie)

def updateZombieRoutes():
    for zombie in zombies:
        zombie.updateRoute()