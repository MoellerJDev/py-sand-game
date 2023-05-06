from element import Element
import pygame

class Sand(Element):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (194, 178, 128)  # Sand color

    def update(self, grid):
        # If the space below this element is empty, move down
        if self.y < len(grid) - 1 and grid[self.y + 1][self.x] is None:
            grid[self.y][self.x] = None
            self.y += 1
            grid[self.y][self.x] = self