#r"C:\Desktop\BlockDead\2D HD Zombie City Tileset\Isometric Tiles\Ground A1_E.png
import math

from models.MapLoader import GameMap
import views.Entity
from views.Creature import Player
from views.RenderUtility import *
BLACK = (0, 0, 0)

print(iso_to_screen_staggered(1, 3, 128, 64))

pygame.init()
pygame.display.set_caption("2.5D Pygame Example with Camera (Tiled Isometric Staggered + CSV)")
map = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_terrain.csv")


Y_DRAW_CORRECTION = 0
running = True

import models.EntityManager
from controllers.MouseControl import mouseUpdate, keyUpdate

decor = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_decor.csv")

decorTiles = decor.tileToDraw

while running:
    clearScreen()
    renderMap(map.tileToDraw, views.Entity.camera_offset_x, views.Entity.camera_offset_y)

    models.EntityManager.mainCharacter.update()
    renderMap(decorTiles + [(models.EntityManager.mainCharacter.getPosition()[0], models.EntityManager.mainCharacter.getPosition()[1],\
                             models.EntityManager.mainCharacter.image, 70, 55)], views.Entity.camera_offset_x, views.Entity.camera_offset_y)




    # surface = pygame.Surface((800, 600), pygame.SRCALPHA)
    # surface.fill((0, 0, 0, 255))

    # pygame.draw.circle(surface, (0, 0, 0, 50), center=(400, 300), radius=100)

    # SCREEN.blit(surface, (0, 0))

    mouseUpdate()
    keyUpdate()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()