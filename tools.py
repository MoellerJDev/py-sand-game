import pygame

class Element:
    def __init__(self, x, y):
        # The x and y parameters indicate the current position of the element
        self.x = x
        self.y = y

    def update(self, grid):
        # The update method will be called each frame to update the element's position
        # The grid parameter is a 2D list representing the game's grid of elements
        pass

    def draw(self, screen):
        # The draw method will be called each frame to draw the element on the screen
        # The screen parameter is a Pygame Surface object representing the game screen
        pass

class Sand(Element):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (237, 201, 175)  # Sand color

    def update(self, grid):
        # If the space below this element is empty, move down
        if self.y < len(grid) - 1 and grid[self.y + 1][self.x] is None:
            grid[self.y][self.x] = None
            self.y += 1
            grid[self.y][self.x] = self

    def draw(self, screen):
        # Draw a small square at the element's position
        pygame.draw.rect(screen, self.color, (self.x * 10, self.y * 10, 10, 10))
