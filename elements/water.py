import pygame
from element import Element
from elements.sand import Sand
import settings


class Water(Element):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (0, 0, 255)  # Blue color
        self.tick_counter = 0  # Tick counter for delay

    def update(self, grid):
        # Delay the movement of water by checking the tick counter
        if self.tick_counter < settings.WATER_DELAY:
            self.tick_counter += 1
            return

        self.tick_counter = 0  # Reset the tick counter

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
