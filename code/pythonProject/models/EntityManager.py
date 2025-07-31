from models.Creature import *
from models.Zombie import *
import models.DataManager
import random
#testZombie = Zombie(r"C:\Desktop\BlockDead\2D HD Zombie Rural Tileset\Animations\Spritesheets\With shadow\RuralZombie 1")

def loadMainCharacter():
    models.DataManager.mainCharacter = Player('Survivor 2')

def spawnZombie(postion=Vec2d(0, 0)):
    zombie = Zombie(f"RuralZombie {random.randint(1, 5)}", postion, speed=random.randint(5, 15) / 1000)
    zombie.updateRoute()
    models.DataManager.zombies.append(zombie)

def updateZombies():
    for zombie in models.DataManager.zombies:
        zombie.update()
        if zombie.dead:
           models.DataManager.zombies.remove(zombie)

def updateZombieRoutes():
    for zombie in models.DataManager.zombies:
        zombie.updateRoute()