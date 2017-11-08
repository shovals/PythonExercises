import pygame
import math
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PI = math.pi
# Select the font to use, size, bold, italics
font = pygame.font.SysFont('Calibri', 25, True, False)

size = (400, 500)
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

    screen.fill(WHITE)  # Clear the screen to white

    # Draw
    # Draw on the screen a line from (0,0) to (100,100)
    # 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

    # Draw on the screen several lines from (0,10) to (100,110)
    # 5 pixels wide using a loop
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)

    # Draw a rectangle
    pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)

    # Draw an ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    # Draw an arc as part of an ellipse.
    # Use radians to determine what angle to draw.
    pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 0, PI / 2, 2)
    pygame.draw.arc(screen, GREEN, [20, 220, 250, 200], PI / 2, PI, 2)
    pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], PI, 3 * PI / 2, 2)
    pygame.draw.arc(screen, RED, [20, 220, 250, 200], 3 * PI / 2, 2 * PI, 2)

    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    text = font.render("This is funARCtic", True, BLACK)
    screen.blit(text, [250, 250])
    # Update the screen with what I drew
    pygame.display.flip()

    clock.tick(60)  # 60 frames per second limit

pygame.quit()

