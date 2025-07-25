import pygame

from views.Creature import *
from views.Zombie import *

allSprites = pygame.sprite.OrderedUpdates()

mainCharacter = Player(r'C:\Desktop\BlockDead\2D HD Zombie Rural Tileset\Animations\Spritesheets\With shadow\Survivor 2')

testZombie = Zombie(r"C:\Desktop\BlockDead\2D HD Zombie Rural Tileset\Animations\Spritesheets\With shadow\RuralZombie 1")

allSprites.add(mainCharacter)
