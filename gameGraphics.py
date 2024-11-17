import pygame

GRID_SIZE = 10
CELL_SIZE = 32
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

pygame.init()

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Game Graphics")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

player_position = [0, 0]
player_rect = pygame.Rect(player_position[0] * CELL_SIZE, player_position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_UP and player_position[1] > 0:
                player_position[1] -= 1
            elif event.key == pygame.K_DOWN and player_position[1] < GRID_SIZE - 1:
                player_position[1] += 1
            elif event.key == pygame.K_LEFT and player_position[0] > 0:
                player_position[0] -= 1
            elif event.key == pygame.K_RIGHT and player_position[0] < GRID_SIZE -1:
                player_position[0] += 1
            player_rect = pygame.Rect(player_position[0] * CELL_SIZE, player_position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, player_rect)

    pygame.display.flip()

pygame.quit()
