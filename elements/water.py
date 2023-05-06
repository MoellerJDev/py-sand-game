from element import Element
from elements.sand import Sand
import pygame

class Water(Element):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (0, 0, 255)  # Blue color

    def update(self, grid):
        # If the space below this element is empty or is Sand, move down
        if self.y < len(grid) - 1 and (grid[self.y + 1][self.x] is None or isinstance(grid[self.y + 1][self.x], Sand)):
            grid[self.y][self.x] = None
            self.y += 1
            grid[self.y][self.x] = self
        # If can't move down but can move left, move left
        elif self.x > 0 and grid[self.y][self.x - 1] is None:
            grid[self.y][self.x] = None
            self.x -= 1
            grid[self.y][self.x] = self
        # If can't move down or left but can move right, move right
        elif self.x < len(grid[0]) - 1 and grid[self.y][self.x + 1] is None:
            grid[self.y][self.x] = None
            self.x += 1
            grid[self.y][self.x] = self

    def update(self, grid):
        # If the space below this element is empty or is Sand, move down
        if self.y < len(grid) - 1 and (grid[self.y + 1][self.x] is None or isinstance(grid[self.y + 1][self.x], Sand)):
            grid[self.y][self.x] = None
            self.y += 1
            grid[self.y][self.x] = self
        # If can't move down but can move left, move left
        elif self.x > 0 and grid[self.y][self.x - 1] is None:
            grid[self.y][self.x] = None
            self.x -= 1
            grid[self.y][self.x] = self
        # If can't move down or left but can move right, move right
        elif self.x < len(grid[0]) - 1 and grid[self.y][self.x + 1] is None:
            grid[self.y][self.x] = None
            self.x += 1
            grid[self.y][self.x] = self
