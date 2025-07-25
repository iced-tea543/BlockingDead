import pygame
import logging

from models.ResourceImporter import *
from utility import *


class GameMap:
    def __init__(self, TSXaddr, mapAddr, lastPixelY=None):
        self.tile_images = {}  # tile ID -> pygame.Surface
        self.tileToDraw = []
        self.TSX = loadTSX(TSXaddr)
        self.map = loadMapFromCSV(mapAddr)
        self.loadMap(lastPixelY)

    def loadMap(self, lastPixelY=None):

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
                    content_start_y = findFirstPixelY(tileImageRaw)
                    TILE_IMAGE_PIXEL_WIDTH = RAW_IMAGE_WIDTH
                    TILE_IMAGE_PIXEL_HEIGHT = (RAW_IMAGE_HEIGHT if lastPixelY != -1 else findLastPixelY(tileImageRaw)) - content_start_y - (0 if lastPixelY == None or lastPixelY == -1 else lastPixelY)
                    tileImage = tileImageRaw.subsurface(0, content_start_y, TILE_IMAGE_PIXEL_WIDTH,
                                                           TILE_IMAGE_PIXEL_HEIGHT)
                    print(x, y, self.TSX[tileID])
                    self.tileToDraw.append((x, y, tileImage, TILE_IMAGE_PIXEL_WIDTH, TILE_IMAGE_PIXEL_HEIGHT))

    def isWalkable(self, x, y):
        return True
