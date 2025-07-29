#r"C:\Desktop\BlockDead\2D HD Zombie City Tileset\Isometric Tiles\Ground A1_E.png

from views.RenderUtility import *

pygame.init()
pygame.display.set_caption("2.5D Pygame Example with Camera (Tiled Isometric Staggered + CSV)")

running = True
import models.DataManager
import models.EntityManager
models.EntityManager.spawnZombie((0, 2))
from controllers.MouseControl import mouseUpdate, keyUpdate

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not running:
        break
    
    clearScreen()
    renderMap(models.DataManager.tile.tileToDraw, models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY)

    models.EntityManager.mainCharacter.update()
    models.EntityManager.updateZombies()
    #models.EntityManager.testZombie.update()

    allTiles = models.DataManager.decor.tileToDraw + models.DataManager.house.tileToDraw


    playerX, playerY = models.EntityManager.mainCharacter.getScreenPosition()

    for zombie in models.EntityManager.zombies:
        allTiles.append((zombie.getScreenPosition()[0], zombie.getScreenPosition()[1], zombie.image, 70, 55))

    allTiles.append((playerX, playerY, models.EntityManager.mainCharacter.image, 70, 55))

    renderMap(allTiles, models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY)

    renderMap(models.DataManager.roof.tileToDraw, models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY)


    # surface = pygame.Surface((800, 600), pygame.SRCALPHA)
    # surface.fill((0, 0, 0, 255))

    # pygame.draw.circle(surface, (0, 0, 0, 50), center=(400, 300), radius=100)

    # SCREEN.blit(surface, (0, 0))

    mouseUpdate()
    keyUpdate()
    pygame.display.flip()


pygame.quit()