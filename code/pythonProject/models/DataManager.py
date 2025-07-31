cameraOffsetX = -(400-64)
cameraOffsetY = -(300-64)

import os
import pygame

from models.MapLoader import GameMap

terrain = None
terrainDecor = None
decor = None
house = None
roof = None

boundaries = [
    ((10.38, 14.56), (14.52, 5.6)),
    ((1.85, 7.5),(3.723, 2.826)),
    ((8.351025971044313, 14.427047609329783),(11.197787873376727, 19.93713995648954)),
    ((10.389087296525858, 13.423860018001118),(12.164133470105757, 17.816795077635515))
]

spriteSheet = {}

backGroundColor = (0, 0, 0)

runningStatus = 0 # 0 : main menu, 1 : game running, 2 : game paused, 3 : game over, -1 : game quit

zombies = []

mainCharacter = None

def loadResource():
    global terrain, terrainDecor, decor, house, roof
    terrain = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_terrain.csv")
    terrainDecor = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_terrainDecor.csv")
    decor = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_decor.csv",-1)
    house = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_house.csv", 20)
    roof = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_roof.csv", 20)

    loadSpriteSheet(r'C:\Desktop\BlockDead\2D HD Zombie Rural Tileset\Animations\Spritesheets\With shadow')

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