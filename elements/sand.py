from element import Element
import pygame
import settings

class Sand(Element):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (194, 178, 128)  # Sand color
        self.is_settled = False

    def update(self, grid):
        from elements.water import Water  # Import locally inside the method

        if self.is_settled:
            return

        # Check if there is water below the sand
        if self.y < settings.GRID_HEIGHT - 1 and isinstance(grid[self.y + 1][self.x], Water):
            # Check if there is empty space below the water
            if self.y < settings.GRID_HEIGHT - 2 and grid[self.y + 2][self.x] is None:
                # Move the sand down and mark it as settled
                grid[self.y][self.x] = None
                self.y += 1
                grid[self.y][self.x] = self
                self.is_settled = True
        else:
            # If there is no water below, allow the sand to fall down if space is available
            if self.y < settings.GRID_HEIGHT - 1 and grid[self.y + 1][self.x] is None:
                grid[self.y][self.x] = None
                self.y += 1
                grid[self.y][self.x] = self

            # Reset the settled state when the sand moves
            self.is_settled = False
