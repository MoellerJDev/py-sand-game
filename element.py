import pygame
import settings

class Element:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)  # Default color is white

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * settings.GRID_SIZE, self.y * settings.GRID_SIZE, settings.GRID_SIZE, settings.GRID_SIZE))

    def update(self, grid):
        pass  # Default behavior is to do nothing
