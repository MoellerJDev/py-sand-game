import pygame
import settings
from elements.sand import Sand
from elements.water import Water
from elements.fire import Fire
from elements.stone import Stone

class Tools:
    @staticmethod
    def handle_events(grid, cursor):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x, y = x // settings.CELL_SIZE, y // settings.CELL_SIZE
                if event.button == 1:  # Left mouse button
                    Tools.place_particles(grid, x, y, Sand)
                elif event.button == 3:  # Right mouse button
                    Tools.place_particles(grid, x, y, Water)
                elif event.button == 2:  # Middle mouse button
                    Tools.place_particles(grid, x, y, Fire)
                elif event.button == 4:  # Fourth mouse button
                    Tools.place_particles(grid, x, y, Stone)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and cursor.y > 0:  # Move up
                    cursor.y -= 1
                elif event.key == pygame.K_a and cursor.x > 0:  # Move left
                    cursor.x -= 1
                elif event.key == pygame.K_s and cursor.y < settings.GRID_HEIGHT - 1:  # Move down
                    cursor.y += 1
                elif event.key == pygame.K_d and cursor.x < settings.GRID_WIDTH - 1:  # Move right
                    cursor.x += 1
                elif event.key == pygame.K_SPACE:  # Place element
                    grid[cursor.y][cursor.x] = Sand(cursor.x, cursor.y)
        return True

    @staticmethod
    def place_particles(grid, x, y, particle_type):
        for i in range(-1, 2):  # Place multiple particles
            for j in range(-1, 2):
                grid[y + j][x + i] = particle_type(x + i, y + j)
