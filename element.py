import pygame
import settings

class Element:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)  # Default color is white

    def draw(self, screen, x, y, size):
        pygame.draw.rect(screen, self.color, (x, y, size, size))

    def update(self, grid):
        pass  # Default behavior is to do nothing
