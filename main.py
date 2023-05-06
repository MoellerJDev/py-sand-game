import pygame
import settings
from element import Sand

def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    GRID_WIDTH = SCREEN_WIDTH // 10
    GRID_HEIGHT = SCREEN_HEIGHT // 10

    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

    running = True
    grid = [[None for _ in range(settings.GRID_WIDTH)] for _ in range(settings.GRID_HEIGHT)]
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x, y = x // 10, y // 10  # Convert screen coordinates to grid coordinates
                grid[y][x] = Sand(x, y)

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