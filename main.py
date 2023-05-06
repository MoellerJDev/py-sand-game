import pygame
import settings
from elements.sand import Sand
from elements.water import Water
from elements.fire import Fire
from elements.stone import Stone
from cursor import Cursor
from tools import Tools
import random

def update_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    positions = [(x, y) for x in range(cols) for y in range(rows)]
    random.shuffle(positions)

    for x, y in positions:
        element = grid[y][x]
        if element is not None:
            element.update(grid)

def draw_grid(screen, grid, cursor, tick_counter):
    screen.fill((0, 0, 0))

    usable_width = settings.SCREEN_WIDTH
    usable_height = settings.SCREEN_HEIGHT

    cell_width = usable_width // settings.GRID_WIDTH
    cell_height = usable_height // settings.GRID_HEIGHT

    for y, row in enumerate(grid):
        for x, element in enumerate(row):
            if element is not None:
                element.update(grid)
                element.draw(screen, x * cell_width, y * cell_height, cell_width)

    # Draw the cursor
    cursor[0].draw(screen)

    # Draw the tick counter
    font = pygame.font.SysFont(None, 24)
    text = font.render("Ticks: " + str(tick_counter), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()




def main():
    pygame.init()

    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

    grid = [[None for _ in range(settings.GRID_WIDTH)] for _ in range(settings.GRID_HEIGHT)]

    cursor = [Cursor(settings.CURSOR_SIZE)]  # Wrap cursor in a list to pass by reference
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