import pygame
import settings
from elements.sand import Sand
from elements.water import Water
from elements.fire import Fire
from elements.stone import Stone
from cursor import Cursor
from tools import Tools

def update_grid(grid):
    for row in grid:
        for element in row:
            if element is not None:
                element.update(grid)

def draw_grid(screen, grid, cursor, tick_counter):
    screen.fill((0, 0, 0))
    cursor.draw(screen)

    for y, row in enumerate(grid):
        for x, element in enumerate(row):
            if element is not None:
                element.draw(screen, x * settings.CELL_SIZE, y * settings.CELL_SIZE, settings.CELL_SIZE)

    font = pygame.font.Font(None, 36)
    tick_text = font.render(f"Ticks: {tick_counter}", True, (255, 255, 255))
    screen.blit(tick_text, (10, 10))

def main():
    pygame.init()

    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

    grid = [[None for _ in range(settings.GRID_WIDTH)] for _ in range(settings.GRID_HEIGHT)]
    
    cursor = Cursor()
    tick_counter = 0

    clock = pygame.time.Clock()
    FPS_LIMIT = 60  # Maximum frames per second

    running = True
    while running:
        running = Tools.handle_events(grid, cursor)
        update_grid(grid)
        draw_grid(screen, grid, cursor, tick_counter)
        tick_counter += 1
        pygame.display.flip()

        clock.tick(FPS_LIMIT)  # Limit the frames per second

    pygame.quit()

if __name__ == "__main__":
    main()
