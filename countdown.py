import pygame
pygame.init()

MINUTES = 3
RESOLUTION = (1280, 720)
FONT = 'Droid'
SIZE = 256
PREFIX = 'countdown-'
EXTENSION = '.png'

surf = pygame.Surface(RESOLUTION)
font = pygame.font.SysFont(FONT, SIZE, True, False)

frame = 1
for minute in range(MINUTES-1, -1, -1):
    for second in range(59, -1, -1):
        surf.fill((0,32,0))
        text = str(minute) + ':' + str(second).zfill(2)
        render = font.render(text, True, (255,255,255), (0,32,0))
        rect = render.get_rect()
        rect.center = [RESOLUTION[0]/2, RESOLUTION[1]/2]
        surf.blit(render, rect)
        pygame.image.save(surf, PREFIX + str(frame) + EXTENSION)
        frame += 1
