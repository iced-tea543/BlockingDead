import pygame

from utility import iso_to_screen_staggered

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

LOGIC_TILE_WIDTH = 128
LOGIC_TILE_HEIGHT = 64  # Tiled 中的逻辑瓦片高度

def clearScreen():
    SCREEN.fill((0, 0, 0))

def renderMap(tileToDraw, cameraOffsetX, cameraOffsetY):
    for tileInfo in sorted(tileToDraw, key=lambda tileInfo: (tileInfo[1], tileInfo[0])):

        mapX, mapY, tileImage, tileImagePixelWidth, tileImagePixelHeight = tileInfo
        screenX, screenY = iso_to_screen_staggered(mapX, mapY, LOGIC_TILE_WIDTH, LOGIC_TILE_HEIGHT,
                                                     cameraOffsetX, cameraOffsetY)
        blitX = screenX
        blitY = screenY - (tileImagePixelHeight - LOGIC_TILE_HEIGHT)

        # if SCREEN.get_rect().colliderect(pygame.Rect(blitX, blitY, tileImagePixelWidth, tileImagePixelHeight)):
        #     SCREEN.blit(tileImage, (blitX, blitY))
        if -tileImagePixelWidth < blitX < SCREEN_WIDTH + tileImagePixelWidth and \
                -tileImagePixelHeight < blitY < SCREEN_HEIGHT + tileImagePixelHeight:
            SCREEN.blit(tileImage, (blitX, blitY))
