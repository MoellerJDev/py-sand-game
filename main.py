import pygame
import settings
from elements.sand import Sand
from elements.water import Water
from elements.fire import Fire
from elements.stone import Stone
from cursor import Cursor

def main():
    pygame.init()

    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

    running = True
    grid = [[None for _ in range(settings.GRID_WIDTH)] for _ in range(settings.GRID_HEIGHT)]
    
    cursor = Cursor()  # Create a cursor instance

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x, y = x // settings.GRID_SIZE, y // settings.GRID_SIZE  # Convert screen coordinates to grid coordinates
                if event.button == 1:  # Left mouse button
                    grid[y][x] = Sand(x, y)
                elif event.button == 3:  # Right mouse button
                    grid[y][x] = Water(x, y)
                elif event.button == 2:  # Middle mouse button
                    grid[y][x] = Fire(x, y)
                elif event.button == 4:  # Fourth mouse button
                    grid[y][x] = Stone(x, y)
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

        screen.fill((0, 0, 0))
        cursor.draw(screen)

        for row in grid:
            for element in row:
                if element is not None:
                    element.update(grid)
                    element.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
