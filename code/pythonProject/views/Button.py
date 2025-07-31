import pygame
import views.RenderUtility
class Button:
    def __init__(self, x, y, text, textColor, image, hoverImage, action=None):
        self.x = x
        self.y = y
        self.textColor = textColor
        self.text = text
        self.image = image
        self.action = action
        self.hoverImage = hoverImage
        self.font = pygame.font.SysFont(r"PressStart2P-Regular", 13)
        self.status = 0  # 0: normal, 1: hovered, 2: clicked

    def draw(self):
        screen = views.RenderUtility.SCREEN
        screen.blit(self.image, (self.x, self.y))
        textSurface = self.font.render(self.text, True, self.textColor)
        textRect = textSurface.get_rect(center=(self.x + self.image.get_width() // 2, self.y + self.image.get_height() // 2))
        screen.blit(textSurface, textRect)

        if self.status == 1:  # hovered
            diffX = self.hoverImage.get_width() - self.image.get_width()
            diffY = self.hoverImage.get_height() - self.image.get_height()
            screen.blit(self.hoverImage, (self.x - diffX // 2, self.y - diffY // 2))

    def isHovered(self, mousePos):
        mouseX, mouseY = mousePos
        return self.x <= mouseX <= self.x + self.image.get_width() and \
               self.y <= mouseY <= self.y + self.image.get_height()