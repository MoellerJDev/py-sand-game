from element import Element
from elements.sand import Sand
import pygame

class Stone(Element):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (169, 169, 169)  # Stone is gray

    def update(self, grid):
        # Check the surrounding squares, if any are Fire, change this Stone to Sand
        for dx, dy in Element.SURROUNDING:
            # Make sure we're inside the grid
            if 0 <= self.x + dx < len(grid[0]) and 0 <= self.y + dy < len(grid):
                neighboring_element = grid[self.y + dy][self.x + dx]
                if neighboring_element is not None and type(neighboring_element).__name__ == 'Fire':
                    grid[self.y][self.x] = Sand(self.x, self.y)
                    return
