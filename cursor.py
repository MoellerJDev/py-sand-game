import pygame
import settings

class Cursor:
    def __init__(self):
        self.x = settings.GRID_WIDTH // 2
        self.y = settings.GRID_HEIGHT // 2
        self.color = (255, 255, 255)  # White color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * 10, self.y * 10, 10, 10))