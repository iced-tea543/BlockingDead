#r"C:\Desktop\BlockDead\2D HD Zombie City Tileset\Isometric Tiles\Ground A1_E.png
from views.RenderUtility import *
import views.RenderUtility

pygame.init()
pygame.display.set_caption("2.5D Pygame Example with Camera (Tiled Isometric Staggered + CSV)")

running = True
import models.DataManager
import models.EntityManager

from controllers.MouseControl import mouseUpdate, keyUpdate

clock = pygame.time.Clock()

#tile = pygame.image.load(r"C:\Desktop\BlockDead\BlockDead.png").convert_alpha()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not running:
        break
    
    clearScreen()
    #renderMap([(0, 0, tile, 2567, 1196)], models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY)
    renderMap(models.DataManager.terrain.tileToDraw + models.DataManager.terrainDecor.tileToDraw, models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY)
    renderMap(models.DataManager.decor.tileToDraw, models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY)


    models.EntityManager.mainCharacter.update()
    models.EntityManager.updateZombies()
    #models.EntityManager.testZombie.update()

    allTiles = models.DataManager.decor.tileToDraw + models.DataManager.house.tileToDraw


    playerX, playerY = models.EntityManager.mainCharacter.getScreenPosition()

    for zombie in models.EntityManager.zombies:
        allTiles.append((*zombie.getScreenPosition(), zombie.image, 70, 55))

    allTiles.append((playerX, playerY, models.EntityManager.mainCharacter.image, 70, 55))

    renderMap(allTiles, models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY)

    renderMap(models.DataManager.roof.tileToDraw, models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY)


    # pygame.draw.line(views.RenderUtility.SCREEN, (255, 165, 0), (380, 280),\
    #                 (380 + models.EntityManager.mainCharacter.dx, 280 + models.EntityManager.mainCharacter.dy))

    # surface = pygame.Surface((800, 600), pygame.SRCALPHA)
    # surface.fill((0, 0, 0, 255))

    # pygame.draw.circle(surface, (0, 0, 0, 50), center=(400, 300), radius=100)

    # SCREEN.blit(surface, (0, 0))
    clock.tick(80)
    mouseUpdate()
    keyUpdate()
    pygame.display.flip()
    #print(clock.get_fps())


pygame.quit()