import pygame
import math

pygame.init()

pixel_size = 1

# COLOR CODE
black = (0, 0, 0)
white = (255, 255, 255)

# SIZE PARAMETERS
screen_width = 800
screen_height = 600

# SET SCREEN SIZE
screen_display = pygame.display.set_mode((screen_width, screen_height))
screen_display.fill(black)

# TITLE
pygame.display.set_caption("Bresenham Circle")

def bresenham_circle(Cx, Cy, rad):
    screen_close = False
    while not screen_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_close = True

        x = 0
        y = rad
        d = 3 - 2*rad

        while x <= rad / math.sqrt(2):

            # O* - 45*
            pygame.draw.rect(screen_display, white, [Cx + y, Cy - x, pixel_size, pixel_size])
            # 45* - 90*
            pygame.draw.rect(screen_display, white, [Cx + x, Cy - y, pixel_size, pixel_size])
            # 90* - 135*
            pygame.draw.rect(screen_display, white, [Cx - x, Cy - y, pixel_size, pixel_size])
            # 135* - 180*
            pygame.draw.rect(screen_display, white, [Cx - y, Cy - x, pixel_size, pixel_size])
            # 180* - 225*
            pygame.draw.rect(screen_display, white, [Cx - y, Cy + x, pixel_size, pixel_size])
            # 225* - 270*
            pygame.draw.rect(screen_display, white, [Cx - x, Cy + y, pixel_size, pixel_size])
            # 270* - 315*
            pygame.draw.rect(screen_display, white, [Cx + x, Cy + y, pixel_size, pixel_size])
            # 315* - 360*
            pygame.draw.rect(screen_display, white, [Cx + y, Cy + x, pixel_size, pixel_size])

            if (d < 0):
                d = d + 4 * x + 6

            else:
                d = d + 4 * x - 4 * y + 10
                y -= 1

            x += 1

        pygame.display.update()

#driver code
# User-defined Input
# x = int(input("x co-od. of Centre C: "))
# y = int(input("y co-od. of Centre C: "))
# r = int(input("x co-od. of Radius: "))

# Pre-defined Input
x = 400
y = 300
r = 200
bresenham_circle(x, y, r)
pygame.quit()
