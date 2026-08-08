import pgzrun

WIDTH = 800
HEIGHT = 550

def draw():

    screen.fill((0,0,0))

    screen.draw.text(
        "NEON WIREFRAME CITY", 
        center= (500, 50),
        fontsize=55, color=(255, 0, 255)
    )

    sun_x = 500
    sun_y = 180
    radius = 90

    screen.draw.circle((sun_x, sun_y), radius, (255, 0, 255))

    for y in range(130, 240, 15):
        screen.draw.line((420, y), (580, y), (255))