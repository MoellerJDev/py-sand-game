import pygame
import settings
from elements.sand import Sand
from elements.water import Water
from elements.fire import Fire
from elements.stone import Stone

def place_particles(grid, x, y, particle_type):
    for i in range(-1, 2):  # Place multiple particles
        for j in range(-1, 2):
            new_x = x + i
            new_y = y + j
            if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]):
                grid[new_y][new_x] = particle_type(new_x, new_y)

class Tools:
    @staticmethod
    def handle_events(grid, cursor):
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x, y = x // settings.CELL_SIZE, y // settings.CELL_SIZE

                # Check if the cursor is clicked
                if cursor.is_clicked(x, y):
                    cursor.x = x * settings.CELL_SIZE  # Update cursor position
                    cursor.y = y * settings.CELL_SIZE

                    # Handle different cursor actions
                    if cursor.x == 0:
                        # Action for the first cursor
                        pass
                    elif cursor.x == cursor.size:
                        # Action for the second cursor
                        pass
                    elif cursor.x == cursor.size * 2:
                        # Action for the third cursor
                        pass
                    # Add more cursor actions as needed

                else:
                    # Handle other mouse click events (placing elements)
                    if event.button == 1:  # Left mouse button
                        place_particles(grid, x, y, Sand)
                    elif event.button == 3:  # Right mouse button
                        place_particles(grid, x, y, Water)
                    elif event.button == 2:  # Middle mouse button
                        place_particles(grid, x, y, Fire)
                    elif event.button == 4:  # Fourth mouse button
                        place_particles(grid, x, y, Stone)  # Place a stone

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
                    grid[cursor.y // settings.CELL_SIZE][cursor.x // settings.CELL_SIZE] = Sand(cursor.x // settings.CELL_SIZE, cursor.y // settings.CELL_SIZE)

        return running
