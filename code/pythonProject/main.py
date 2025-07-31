#r"C:\Desktop\BlockDead\2D HD Zombie City Tileset\Isometric Tiles\Ground A1_E.png
# All resources are downloaded from https://etahoshi.itch.io/minimal-fantasy-gui-by-eta and https://smallscaleint.itch.io/zombie-rural-hd-isometric-tileset
from utility import Vec2d
from models.Creature import Player

from views.RenderUtility import *
from views.UIManager import *
from views.UIManager import drawLoadingScreen
from views.Button import Button

import models.DataManager
import models.EntityManager

from controllers.MouseControl import *

allTiles = []
clock = pygame.time.Clock()

mainMenu = None
gameOverMenu = None

def reset():
    models.DataManager.cameraOffsetX = -(400-64)
    models.DataManager.cameraOffsetY = -(300-64)
    models.EntityManager.loadMainCharacter()
    models.DataManager.zombies = []
    models.EntityManager.spawnZombie()
    models.EntityManager.spawnZombie()

def onGameStart():
    global clock, buttons, mainMenu, gameOverMenu

    pygame.init()
    pygame.display.set_caption("Blocking Dead")

    drawLoadingScreen()

    
    models.DataManager.loadResource()
    models.EntityManager.loadMainCharacter()

    buttonImage = pygame.image.load(r"UI\Button_52x14.png").convert_alpha()
    hoverButtonImage = pygame.image.load(r"UI\HighlightButton_60x23.png").convert_alpha()

    mainMenu = UserInterface([
        Button(400 - buttonImage.get_rect().width // 2, 200 - buttonImage.get_rect().height // 2, "Start Game", (210, 192, 152), 
            buttonImage,
            hoverButtonImage,
            lambda: setattr(models.DataManager, 'runningStatus', 1)  # Start the game. This code is auto filled by the AI of vscode
        ),
        Button(400 - buttonImage.get_rect().width // 2, 300 - buttonImage.get_rect().height // 2, "Exit Game", (210, 192, 152), 
            buttonImage,
            hoverButtonImage,
            lambda: setattr(models.DataManager, 'runningStatus', -1)  # Exit the game. This code is auto filled by the AI of vscode
        ),
        Button(400 - buttonImage.get_rect().width // 2, 400 - buttonImage.get_rect().height // 2, "Reset Game", (210, 192, 152), 
            buttonImage,
            hoverButtonImage,
            reset  # Reset the game.
        )
    ])

    def restart():
        reset()
        models.DataManager.runningStatus = 1  # Restart the game. This code is auto
    gameOverMenu = UserInterface([
        Button(400 - buttonImage.get_rect().width // 2, 200 - buttonImage.get_rect().height // 2, "Restart", (210, 192, 152), 
            buttonImage,
            hoverButtonImage,
            restart
        ),
        Button(400 - buttonImage.get_rect().width // 2, 300 - buttonImage.get_rect().height // 2, "Exit Game", (210, 192, 152), 
            buttonImage,
            hoverButtonImage,
            lambda: setattr(models.DataManager, 'runningStatus', -1)  # Exit the game. This code is auto filled by the AI of vscode
        ),
        Button(400 - buttonImage.get_rect().width // 2, 300 - buttonImage.get_rect().height // 2, "Menu", (210, 192, 152), 
            buttonImage,
            hoverButtonImage,
            lambda: setattr(models.DataManager, 'runningStatus', 0)  # Exit the game. This code is auto filled by the AI of vscode
        )
    ])

    reset()

import random

def onGameDrawing():
    global allTiles
    #renderMap([(0, 0, tile, 2567, 1196)], models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY)
    renderMap(models.DataManager.terrain.tileToDraw + models.DataManager.terrainDecor.tileToDraw, models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY)
    renderMap(models.DataManager.decor.tileToDraw, models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY)

    renderMap(allTiles, models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY)

    renderMap(models.DataManager.roof.tileToDraw, models.DataManager.cameraOffsetX, models.DataManager.cameraOffsetY)

def onGameStep(tick):
    global allTiles

    if tick % 500 == 0:
        models.EntityManager.spawnZombie(models.DataManager.mainCharacter.position + Vec2d(random.randint(5, 10), random.randint(5, 15)))

    models.DataManager.mainCharacter.update()
    models.EntityManager.updateZombies()
    #models.EntityManager.testZombie.update()

    allTiles = models.DataManager.decor.tileToDraw + models.DataManager.house.tileToDraw


    playerX, playerY = models.DataManager.mainCharacter.getScreenPosition()

    for zombie in models.DataManager.zombies:
        allTiles.append((*zombie.getScreenPosition(), zombie.image, 70, 55))

    allTiles.append((playerX, playerY, models.DataManager.mainCharacter.image, 70, 55))

#tile = pygame.image.load(r"C:\Desktop\BlockDead\BlockDead.png").convert_alpha()

onGameStart()
frames = 0
while models.DataManager.runningStatus != -1:

    dt = clock.tick(80)
    frames += 1
    #Game if runningStatus = 1
    if models.DataManager.runningStatus == 1:
        clearScreen()

        onGameStep(frames)
        onGameDrawing()
        onGameMouseUpdate()
        onGameKeyUpdate()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                models.DataManager.runningStatus = -1

    elif models.DataManager.runningStatus == 0:
        views.RenderUtility.SCREEN.fill((171, 155, 142))
        mainMenu.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                models.DataManager.runningStatus = -1
            elif event.type == pygame.MOUSEMOTION:
                mainMenu.mouseMoveUpdate(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mainMenu.mouseClickUpdate()

    elif models.DataManager.runningStatus == 2:
        onGameDrawing()
        #https://python-forum.io/thread-19004.html: draw a transparent rectangle
        overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        views.RenderUtility.SCREEN.blit(overlay, (0, 0))

        gameOverMenu.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                models.DataManager.runningStatus = -1
            elif event.type == pygame.MOUSEMOTION:
                gameOverMenu.mouseMoveUpdate(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gameOverMenu.mouseClickUpdate()



    # pygame.draw.line(views.RenderUtility.SCREEN, (255, 165, 0), (380, 280),\
    #                 (380 + models.EntityManager.mainCharacter.dx, 280 + models.EntityManager.mainCharacter.dy))

    # surface = pygame.Surface((800, 600), pygame.SRCALPHA)
    # surface.fill((0, 0, 0, 255))

    # pygame.draw.circle(surface, (0, 0, 0, 50), center=(400, 300), radius=100)

    # SCREEN.blit(surface, (0, 0))
    pygame.display.flip()
    #print(clock.get_fps())


pygame.quit()