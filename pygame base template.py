import pygame
pygame.init()

# Set up basic colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# init of screen size and title
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shoval's first game")

# --- main program
done = False
clock = pygame.time.Clock()

while not done:
    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game logic should go here

    # Drawing code should go here

    screen.fill(WHITE)  # Clear the screen to white
    pygame.display.flip()  # Update the screen with what I drew

    clock.tick(60)  # 60 frames per second limit

pygame.quit()

