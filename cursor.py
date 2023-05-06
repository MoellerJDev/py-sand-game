import pygame

class Cursor:
    def __init__(self, size):
        self.x = 0
        self.y = 0
        self.color = (255, 255, 255)  # White color
        self.size = size

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def is_clicked(self, x, y):
        return self.x <= x < self.x + self.size and self.y <= y < self.y + self.size

    def decrease_size(self):
        self.size -= 1 if self.size > 1 else 0

    def increase_size(self):
        self.size += 1
