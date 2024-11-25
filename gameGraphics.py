import pygame
import random

GRID_SIZE = 10
CELL_SIZE = 32
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

pygame.init()

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Game Graphics")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

player_position = [0, 0]
player_rect = pygame.Rect(player_position[0] * CELL_SIZE, player_position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)

class Monster:
    def __init__(self, x, y):
        self.position = [x, y]
        self.rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    
    def move(self):
        direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        new_position = self.position[:]  # Copy current position
        if direction == 'UP' and new_position[1] > 0:
            new_position[1] -= 1
        elif direction == 'DOWN' and new_position[1] < GRID_SIZE - 1:
            new_position[1] += 1
        elif direction == 'LEFT' and new_position[0] > 0:
            new_position[0] -= 1
        elif direction == 'RIGHT' and new_position[0] < GRID_SIZE - 1:
            new_position[0] += 1
        
        # Update position
        self.position = new_position
        self.rect.topleft = (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE)

running = True
monsters = [Monster(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))]
player_moves = 0

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
            elif event.key == pygame.K_RIGHT and player_position[0] < GRID_SIZE - 1:
                player_position[0] += 1
            
            
            player_rect.topleft = (player_position[0] * CELL_SIZE, player_position[1] * CELL_SIZE)
            player_moves += 1

            # Trigger monster movement every other player move
            if player_moves % 2 == 0:
                for monster in monsters:
                    monster.move()

    # Check for encounters
    for monster in monsters[:]:  
        if player_position == monster.position:
            print("You have encountered a monster!")
            monsters.remove(monster)

    # Spawn new monsters if none are left
    if not monsters:
        print("It's quiet... too quiet...")
        monsters.append(Monster(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)))
        monsters.append(Monster(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)))

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, player_rect)

    for monster in monsters:
        pygame.draw.rect(screen, RED, monster.rect)

    pygame.display.flip()

pygame.quit()
