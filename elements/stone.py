from element import Element
import pygame
import settings

class Stone(Element):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (169, 169, 169)  # Stone is gray
        self.is_falling = False

    def update(self, grid):
        from elements.water import Water  # Import locally inside the method

        if self.is_falling:
            # Check if there is empty space below the stone
            if self.y < settings.GRID_HEIGHT - 1 and grid[self.y + 1][self.x] is None:
                grid[self.y][self.x] = None
                self.y += 1
                grid[self.y][self.x] = self
            else:
                self.is_falling = False
        else:
            # Check if there is water below the stone
            if self.y < settings.GRID_HEIGHT - 1 and isinstance(grid[self.y + 1][self.x], Water):
                self.is_falling = True
