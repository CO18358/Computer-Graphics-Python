import pygame

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
pygame.display.set_caption("Midpoint Circle")

def mp_line(x1, y1, x2, y2):
    screen_close = False
    while not screen_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_close = True

        x = x1
        y = y1
        dx = x2 - x1
        dy = y2 - y1

        if(abs(dx) > abs(dy)):
            d = dy - dx/2
            while(x <= x2):
                pygame.draw.rect(screen_display, white, [x, y, pixel_size, pixel_size])
                x += 1
                if(d < 0):
                    d = d + dy

                else:
                    d = d + dy - dx
                    y += 1
        else:
            d = dx - dy / 2
            while (y <= y2):
                pygame.draw.rect(screen_display, white, [x, y, pixel_size, pixel_size])
                y += 1
                if (d < 0):
                    d = d + dx

                else:
                    d = d + dx - dy
                    x += 1

        pygame.display.update()

#driver code
# User-defined Input
# x1 = int(input("x co-od. of point A of line AB: "))
# y1 = int(input("y co-od. of point A of line AB: "))
# x2 = int(input("x co-od. of point B of line AB: "))
# y2 = int(input("y co-od. of point B of line AB: "))

# Pre-defined Input
x1 = y1 = 100
x2 = y2 = 500
mp_line(x1, y1, x2, y2)
pygame.quit()