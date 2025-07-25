#r"C:\Desktop\BlockDead\2D HD Zombie City Tileset\Isometric Tiles\Ground A1_E.png

from views.RenderUtility import *
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("2.5D Pygame Example with Camera (Tiled Isometric Staggered + CSV)")

running = True
import models.DataManager
import models.EntityManager
from controllers.MouseControl import mouseUpdate, keyUpdate

import views.Entity

decorTiles = models.DataManager.decor.tileToDraw

while running:
    clearScreen()
    renderMap(models.DataManager.map.tileToDraw, views.Entity.camera_offset_x, views.Entity.camera_offset_y)

    models.EntityManager.mainCharacter.update()
    #models.EntityManager.testZombie.update()


    playerX, playerY = models.EntityManager.mainCharacter.getScreenPosition()

    drawRoof = False



    renderMap(decorTiles\
              + [(playerX, playerY,
                  models.EntityManager.mainCharacter.image, 70, 55),
                 #((models.EntityManager.testZombie.getPosition()[0], models.EntityManager.testZombie.getPosition()[1],
                  #           models.EntityManager.testZombie.image, 70, 55))
                 ]+models.DataManager.house.tileToDraw
                 , views.Entity.camera_offset_x, views.Entity.camera_offset_y)

    renderMap(models.DataManager.roof.tileToDraw, views.Entity.camera_offset_x, views.Entity.camera_offset_y)


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