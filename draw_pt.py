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
pygame.display.set_caption("Draw a Point")

def draw_pt(p, q):
    screen_close = False
    while not screen_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_close = True
        
        pygame.draw.rect(screen_display, white, [p, q, pixel_size, pixel_size])
        pygame.display.update()

#driver code
# User-defined Input
# p = int(input("x co-od. of point P: "))
# q = int(input("y co-od. of point P: "))
# Pre-defined Input
p = 400
q = 300
draw_pt(p, q)
pygame.quit()
