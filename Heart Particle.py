import pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart")
clock = pygame.time.Clock()
size = min(WIDTH, HEIGHT) * 0.022
ticker = 0

class Particle:
    def __init__(self, angle):
        self.angle = angle
        self.offset = random.random() * math.pi

    def move(self):
        noise = math.sin(self.angle + ticker + self.offset) * (0.3 * size)
        r = size + noise
        self.x = r * 16 * (math.sin(self.angle) ** 3)
        self.y = -r * (
            13 * math.cos(self.angle)
            - 5 * math.cos(2 * self.angle)
            - 2 * math.cos(3 * self.angle)
            - math.cos(4 * self.angle)
        )

        self.angle += 0.004
particles = []
count = int(size * size * 200)
for i in range(count):
    angle = i * (2 * math.pi / count)
    particles.append(Particle(angle))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for p in particles:
        p.move()
        x = WIDTH // 2 + int(p.x)
        y = int(HEIGHT * 0.45 + p.y)
        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            screen.set_at((x, y), (255, 0, 0))
    ticker += 0.02
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()