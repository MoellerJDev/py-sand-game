import pygame

class Element:
    SURROUNDING = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)

    def update(self, grid):
        pass

    def draw(self, screen, x, y, size):
        pygame.draw.rect(screen, self.color, (x, y, size, size))

