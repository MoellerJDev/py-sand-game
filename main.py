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

    # Draw the cursors
    for i, cursor_pos in enumerate(settings.CURSOR_POSITIONS):
        cursor_x = cursor_pos * cursor.size
        cursor_y = 0
        cursor.draw(screen)  # Update this line


    # Draw the elements in the grid
    for y, row in enumerate(grid):
        for x, element in enumerate(row):
            if element is not None:
                element.update(grid)
                element.draw(screen, x * settings.CELL_SIZE, y * settings.CELL_SIZE, settings.CELL_SIZE)

    # Draw the tick counter
    font = pygame.font.SysFont(None, 24)
    text = font.render("Ticks: " + str(tick_counter), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()


def main():
    pygame.init()

    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

    running = True
    grid = [[None for _ in range(settings.GRID_WIDTH)] for _ in range(settings.GRID_HEIGHT)]
    cursor = Cursor(settings.CURSOR_SIZE)  # Create a cursor instance
    placing_particle = None

    while running:
        running = Tools.handle_events(grid, cursor, placing_particle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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