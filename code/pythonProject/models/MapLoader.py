import pygame
import logging

from models.ResourceImporter import *
from utility import *


class GameMap:
    def __init__(self, TSXaddr, mapAddr):
        self.tile_images = {}  # tile ID -> pygame.Surface
        self.tileToDraw = []
        self.TSX = loadTSX(TSXaddr)
        self.map = loadMapFromCSV(mapAddr)
        self.loadMap()

    def loadMap(self):

        MAP_SIZE_X = len(self.map[0])
        MAP_SIZE_Y = len(self.map)

        logging.info(f"Map is loaded: {MAP_SIZE_X}x{MAP_SIZE_Y} tiles")

        for y in range(MAP_SIZE_Y):
            for x in range(MAP_SIZE_X):
                tileID = self.map[y][x]
                if tileID != -1:
                    tileImageRaw = pygame.image.load(self.TSX[tileID]).convert_alpha()

                    RAW_IMAGE_WIDTH = tileImageRaw.get_width()
                    RAW_IMAGE_HEIGHT = tileImageRaw.get_height()

                    logging.basicConfig(
                        level=logging.DEBUG,
                        format="%(asctime)s [%(levelname)s] %(message)s",
                        handlers=[
                            logging.FileHandler("last.log", encoding='utf-8'),
                            logging.StreamHandler()
                        ]
                    )
                    contentStartY = findFirstPixelY(tileImageRaw)
                    contentStartX = findFirstPixelX(tileImageRaw)
                    TILE_IMAGE_PIXEL_WIDTH = findLastPixelX(tileImageRaw) - contentStartX
                    TILE_IMAGE_PIXEL_HEIGHT = findLastPixelY(tileImageRaw) - contentStartY

                    tileImage = tileImageRaw.subsurface(contentStartX, contentStartY, TILE_IMAGE_PIXEL_WIDTH,
                                                           TILE_IMAGE_PIXEL_HEIGHT)
                    print(x, y, self.TSX[tileID])
                    self.tileToDraw.append((x, y, tileImage, TILE_IMAGE_PIXEL_WIDTH, TILE_IMAGE_PIXEL_HEIGHT))

    def isWalkable(self, x, y):
        return True
