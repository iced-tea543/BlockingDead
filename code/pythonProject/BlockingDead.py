from cmu_graphics import *
from models.MapLoader import GameMap

from models.Creature import *
from models.Zombie import *

def onAppStart(app):
    # map = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_terrain.csv")
    # decor = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_decor.csv",-1)
    # house = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_house.csv", 20)
    # roof = GameMap(r'C:\Desktop\BlockDead\Resource.tsx', r"C:\Desktop\BlockDead\BlockDead_roof.csv", 20)
    app.title = "2.5D Pygame Example with Camera (Tiled Isometric Staggered + CSV)"
    app.stepsPerSecond = 60

def onStep(app):
    # renderMap(map.tileToDraw, app.camera_offset_x, app.camera_offset_y)
    # renderMap(decor.tileToDraw, app.camera_offset_x, app.camera_offset_y)
    # renderMap(house.tileToDraw, app.camera_offset_x, app.camera_offset_y)
    # renderMap(roof.tileToDraw, app.camera_offset_x, app.camera_offset_y)

    # Update and draw entities
    # models.EntityManager.mainCharacter.update()
    # models.EntityManager.mainCharacter.draw(app)

    # Handle mouse and keyboard input
    # mouseUpdate()
    pass

def onKeyPress(app, key):
    # Handle key presses
    if key == 'Escape':
        app.stop()
    # keyUpdate()

def onMouseMove(app, x, y):
    # Handle mouse movement
    pass        

runApp(height=600, width=800)