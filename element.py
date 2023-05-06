class Cursor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)  # White color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * 10, self.y * 10, 10, 10))

        cursor = Cursor(settings.GRID_WIDTH // 2, settings.GRID_HEIGHT // 2)

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
