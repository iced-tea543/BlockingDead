from views.Creature import *
from views.Zombie import *

mainCharacter = Player('Survivor 2')

#testZombie = Zombie(r"C:\Desktop\BlockDead\2D HD Zombie Rural Tileset\Animations\Spritesheets\With shadow\RuralZombie 1")


zombies = []

def spawnZombie(postion=[0, 0]):
    zombie = Zombie("RuralZombie 1",postion)
    zombie.updateRoute()
    zombies.append(zombie)

def updateZombies():
    for zombie in zombies:
        zombie.update()
        #if zombie.isDead():
        #    zombies.remove(zombie)

def updateZombieRoutes():
    for zombie in zombies:
        zombie.updateRoute()