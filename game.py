import pygame

def clr(color):
    if color % 3 == 0:
        return RED
    elif color % 3 == 2:
        return GREEN
    else:
        return YELLOW

pygame.init()

W = 1200
H = 800

sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_icon(pygame.image.load('2.bmp'))
pygame.display.set_caption('First game')

color = 3
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (250, 250, 0)

# pygame.draw.rect(sc, BLUE, (10, 10,  50, 100), 7)
#
# pygame.draw.line(sc, GREEN, (200, 20), (350, 50))
# pygame.draw.aaline(sc, GREEN, (200, 40), (359, 70))
#
# pygame.draw.lines(sc, RED, True, [(200, 80), (250, 80), (300, 200)])
# pygame.draw.aalines(sc, RED, True, [(300, 80), (350, 80), (400, 200)])
#
# pygame.draw.polygon(sc, WHITE, [[150, 210], [180, 250], [90, 290], [30, 230]])
# pygame.draw.polygon(sc, WHITE, [[150, 310], [180, 350], [90, 390], [30, 330]], 1)
#
# pygame.draw.circle(sc, BLUE, (300, 250), 40)
# pygame.draw.ellipse(sc, BLUE, (300, 300, 100, 50), 1)
#
# pi = 3.14
# pygame.draw.arc(sc, RED, (450, 30, 50, 150), pi, 2*pi, 5)
#
# pygame.display.update()

FPS = 10
clock = pygame.time.Clock()

x = W // 2
y = H//2
speed = 10

FlagLeft = FlagRight = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                FlagLeft = True
                color += 1
            elif event.key == pygame.K_RIGHT:
                FlagRight = True
                color -= 1
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                FlagLeft = FlagRight = False

    if FlagLeft:
        x-=speed
        color += 1
    elif FlagRight:
        x +=speed
        color -= 1

# while 1:
#
# keys pygame.key.get_pressed()
#
# if keys [pygame.K_LEFT]:
# speed
# elif keys [pygame.K_RIGHT]:
# x += speed
# sc.fill(WHITE)
# pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
# pygame.display.update()



    sc.fill(WHITE)
    # pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    # pygame.draw.polygon(sc, GREEN, ([x,y], [x+30, y], [x+15, y-30]))
    pygame.draw.circle(sc, clr(color), (x, y-30), 15)
    color +=1
    pygame.draw.circle(sc, clr(color), (x, y), 15)
    color += 1
    pygame.draw.circle(sc, clr(color), (x, y + 30), 15)
    color += 1
    pygame.display.update()

    clock.tick(FPS)