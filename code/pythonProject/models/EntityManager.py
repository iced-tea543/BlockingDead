import pygame

from views.Creature import Player

allSprites = pygame.sprite.OrderedUpdates()

mainCharacter = Player(r'C:\Desktop\BlockDead\2D HD Zombie Rural Tileset\Animations\Spritesheets\With shadow\Survivor 2')

allSprites.add(mainCharacter)
