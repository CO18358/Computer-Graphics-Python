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
pygame.display.set_caption("Position of a point w.r.t. to the line")

def draw(x1, y1, x2, y2, p, q):
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

        i=1
        while i <= step:
            pygame.draw.rect(screen_display, white,[x, y, pixel_size, pixel_size])
            x = x + x_inc
            y = y + y_inc
            i += 1

        pygame.draw.rect(screen_display, white, [p, q, pixel_size, pixel_size])
        pygame.display.update()

#driver code
# User-defined Input
# p = int(input("x co-od. of point P: "))
# q = int(input("y co-od. of point P: "))
# x1 = int(input("x co-od. of point A of line AB: "))
# y1 = int(input("y co-od. of point A of line AB: "))
# x2 = int(input("x co-od. of point B of line AB: "))
# y2 = int(input("y co-od. of point B of line AB: "))

# Pre-defined Input
p = 200
q = 300
x1 = y1 = 100
x2 = y2 = 500
draw(x1, y1, x2, y2, p, q)

#slope
m = (y2-y1)/(x2-x1)
#y-intercept
b = y1-(m*x1)

#left-right
X = (q-b)/m
if(p>X):
    print("Point P is on right of Line AB")
elif(p<X):
    print("Point P is on left of Line AB")
else:
    print("Point P is on Line AB")

#top-bottom
# Note: y-axis increases downwards
Y=m*p+b
if(q > Y):
    print("Point P is below of Line AB")
elif(q < Y):
    print("Point P is above of Line AB")
else:
    print("Point P is on Line AB")

pygame.quit()
