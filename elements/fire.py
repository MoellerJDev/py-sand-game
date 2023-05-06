from element import Element
import pygame

class Fire(Element):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (255, 255, 0)  # Fire starts as bright yellow
        self.life = 10  # The amount of time the fire will burn

    def update(self, grid):
        # Fire changes color as it burns
        self.life -= 1
        if self.life <= 0:
            grid[self.y][self.x] = None  # Fire burns out
        elif self.life < 3:
            self.color = (139, 0, 0)  # Dark red
        elif self.life < 7:
            self.color = (255, 0, 0)  # Red

        # Fire spreads to neighboring Sand elements and is extinguished by Water
        for dx, dy in Element.SURROUNDING:
            # Make sure we're inside the grid
            if 0 <= self.x + dx < len(grid[0]) and 0 <= self.y + dy < len(grid):
                neighboring_element = grid[self.y + dy][self.x + dx]
                if neighboring_element is not None:
                    if type(neighboring_element).__name__ == 'Sand':
                        grid[self.y + dy][self.x + dx] = Fire(self.x + dx, self.y + dy)  # Ignite the Sand
                    elif type(neighboring_element).__name__ == 'Water':
                        grid[self.y][self.x] = None  # Extinguish the Fire
                        return
