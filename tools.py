import pygame
import settings
from elements.sand import Sand
from elements.water import Water
from elements.fire import Fire
from elements.stone import Stone

class Tools:
    @staticmethod
    def place_particles(grid, x, y, particle_type, cursor_size):
        half_size = cursor_size // 2
        for i in range(-half_size, half_size + 1):  # Place particles within cursor size
            for j in range(-half_size, half_size + 1):
                new_x = x + i
                new_y = y + j
                if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]):
                    grid[new_y][new_x] = particle_type(new_x, new_y)

    @staticmethod
    def handle_events(grid, cursor):
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x, y = x // settings.CELL_SIZE, y // settings.CELL_SIZE

                # Handle mouse clicks for placing elements
                if event.button == 1:  # Left mouse button
                    Tools.place_particles(grid, x, y, Sand, cursor[0].size)
                elif event.button == 3:  # Right mouse button
                    Tools.place_particles(grid, x, y, Water, cursor[0].size)
                elif event.button == 2:  # Middle mouse button
                    Tools.place_particles(grid, x, y, Fire, cursor[0].size)
                elif event.button == 4:  # Fourth mouse button
                    Tools.place_particles(grid, x, y, Stone, cursor[0].size)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and cursor[0].y > 0:  # Move up
                    cursor[0].y -= 1
                elif event.key == pygame.K_a and cursor[0].x > 0:  # Move left
                    cursor[0].x -= 1
                elif event.key == pygame.K_s and cursor[0].y < settings.GRID_HEIGHT - 1:  # Move down
                    cursor[0].y += 1
                elif event.key == pygame.K_d and cursor[0].x < settings.GRID_WIDTH - 1:  # Move right
                    cursor[0].x += 1
                elif event.key == pygame.K_SPACE:  # Place element
                    grid[cursor[0].y][cursor[0].x] = Sand(cursor[0].x, cursor[0].y)
                elif event.key == pygame.K_z:  # Decrease cursor size
                    cursor[0].size -= 1 if cursor[0].size > 1 else 0
                elif event.key == pygame.K_c:  # Increase cursor size
                    cursor[0].size += 1

        return running
