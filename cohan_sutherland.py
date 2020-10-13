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
pygame.display.set_caption("Cohen Sutherland Algorithm")

# Defining region codes
INSIDE = 0  # 0000
UP = 8	 # 1000
DOWN = 4  # 0100
RIGHT = 2  # 0010
LEFT = 1  # 0001

# Viewport co-ordinates
x_max = 700
y_max = 500
x_min = 100
y_min = 100

# utility function to draw a line


def dda(x1, y1, x2, y2):
    screen_close = False
    while not screen_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_close = True

        dx = x2-x1
        dy = y2-y1

        if(abs(dx) > abs(dy)):
            step = abs(dx)
        else:
            step = abs(dy)

        x = x1
        y = y1
        x_inc = dx/step
        y_inc = dy/step

        i = 1
        while i <= step:
            pygame.draw.rect(screen_display, white, [
                             x, y, pixel_size, pixel_size])
            x = x + x_inc
            y = y + y_inc
            i += 1
        pygame.display.update()


def r_code(p, q):
    # "|=" is bitwise OR operator
    code = INSIDE
    if p < x_min:
        code |= LEFT
    elif p > x_max:
        code |= RIGHT
    if q < y_min:
        code |= DOWN
    elif q > y_max:
        code |= UP

    return code


def cohen_sutherland(x1, y1, x2, y2):

    C1 = r_code(x1, y1)
    C2 = r_code(x2, y2)
    clip = False

    while True:

        #inside
        if C1 == 0 and C2 == 0:
            clip = True
            break

        #outside
        elif (C1 & C2) != 0:
            break

        else:
            A = 1
            B = 1

            if C1 != 0:
                C_out = C1
            else:
                C_out = C2

            if C_out & UP:
                A = x1 + (x2 - x1) * ((y_max - y1) / (y2 - y1))
                B = y_max

            if C_out & DOWN:
                A = x1 + (x2 - x1) * ((y_min - y1) / (y2 - y1))
                B = y_min

            if C_out & LEFT:
                B = y1 + (y2 - y1) * ((x_min - x1) / (x2 - x1))
                A = x_min

            if C_out & RIGHT:
                B = y1 + (y2 - y1) * ((x_max - x1) / (x2 - x1))
                A = x_max

            if C_out == C1:
                x1 = A
                y1 = B
                C1 = r_code(x1, y1)

            else:
                x2 = A
                y2 = B
                C2 = r_code(x2, y2)

    if clip:
        dda(x1, y1, x2, y2)
    else:
        print("Line is Outside")


#driver code
dda(x_min, y_min, x_max, y_min)
dda(x_min, y_min, x_min, y_max)
dda(x_max, y_min, x_max, y_max)
dda(x_min, y_max, x_max, y_max)

# User-defined Input
# x1 = int(input("x co-od. of point A of line AB: "))
# y1 = int(input("y co-od. of point A of line AB: "))
# x2 = int(input("x co-od. of point B of line AB: "))
# y2 = int(input("y co-od. of point B of line AB: "))

#Pre-defined Input
x1 = y1 = 300
x2 = y2 = 480
cohen_sutherland(x1, y1, x2, y2)
x3 = 750
y3 = 580
x4 = 50
y4 = 90
cohen_sutherland(x3, y3, x4, y4)
pygame.quit()
