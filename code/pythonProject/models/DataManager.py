cameraOffsetX = -(400-64)
cameraOffsetY = -(300-64)

import os
import pygame

from models.MapLoader import GameMap

terrain = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_terrain.csv")
terrainDecor = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_terrainDecor.csv")
decor = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_decor.csv",-1)
house = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_house.csv", 20)
roof = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_roof.csv", 20)

boundaries = [
    ((10.38, 14.56), (14.52, 5.6)),
    ((1.85, 7.5),(3.723, 2.826))
]

spriteSheet = {}

def loadSpriteSheet(directory):
    for folderName in os.listdir(directory):
        for fileName in os.listdir(os.path.join(directory, folderName)):
            if folderName not in spriteSheet:
                spriteSheet[folderName] = {}
            print(f"Loading {fileName} from {folderName}")
            #spriteSheet[folderName][fileName[:fileName.find('.')]] = pygame.image.load(os.path.join(directory, folderName, fileName)).convert_alpha()
            fullSpriteSheet = pygame.image.load(os.path.join(directory, folderName, fileName)).convert_alpha()
            spriteSheet[folderName][fileName[:fileName.find('.')]] = [[None] * 15 for _ in range(8)]
            for direction in range(8):
                for frameIndex in range(15):
                    rect = pygame.Rect(frameIndex * 128, direction * 128, 128, 128)
                    spriteSheet[folderName][fileName[:fileName.find('.')]][direction][frameIndex] = fullSpriteSheet.subsurface(rect).subsurface(30, 25, 80, 65)


loadSpriteSheet(r'C:\Desktop\BlockDead\2D HD Zombie Rural Tileset\Animations\Spritesheets\With shadow')