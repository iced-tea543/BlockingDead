import pygame
import views.RenderUtility

def drawLoadingScreen():
    screen = views.RenderUtility.SCREEN
    
    font = pygame.font.SysFont(r"PressStart2P-Regular", 16)
    screen.fill((171, 155, 142))
    textSurface = font.render("Loading Game Resources...", True, (0, 0, 0))
    
    textRect = textSurface.get_rect(center=(screen.get_width()//2, screen.get_height()-30))
    screen.blit(textSurface, textRect)
    pygame.display.flip()


class UserInterface:
    def __init__(self, buttons):
        self.buttons = buttons

    def registerButton(self, button):
        # Register a button to the UI
        self.buttons.append(button)

    def draw(self):
        # Draw all buttons in the UI
        for button in self.buttons:
            button.draw()

    def mouseMoveUpdate(self, mousePos):
        for button in self.buttons:
            if button.isHovered(mousePos):
                button.status = 1
            else:
                button.status = 0

    def mouseClickUpdate(self):
        for index in range(len(self.buttons)):
            if self.buttons[index].status == 1:  # If the button is hovered
                self.buttons[index].action()  # Perform the button's action
            

    