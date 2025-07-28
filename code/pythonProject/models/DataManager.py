cameraOffsetX = -(400-64)
cameraOffsetY = -(300-64)

from models.MapLoader import GameMap

tile = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_terrain.csv")
decor = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_decor.csv",-1)
house = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_house.csv", 20)
roof = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_roof.csv", 20)

boundaries = [
    ((10.38, 14.56), (14.52, 5.6)),
    ((1.85, 7.5),(3.723, 2.826))
]