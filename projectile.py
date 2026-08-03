import math
import pygame


class Projectile:

    def __init__(self, x, y, speed, angle, ground, gravity):

        self.x = x
        self.y = y
        self.ground = ground

        radians = math.radians(angle)

        self.vx = speed * math.cos(radians)
        self.vy = -speed * math.sin(radians)

        self.gravity = gravity

        self.radius = 8

        self.path = []

    def update(self, dt):

        self.vy += self.gravity * dt

        self.x += self.vx * dt
        self.y += self.vy * dt

        # Stop at ground level
        if self.y >= self.ground:
            self.y = self.ground
            self.vx = 0
            self.vy = 0

        self.path.append((self.x, self.y))

    def draw(self, screen):

        # Draw trail
        for point in self.path:
            pygame.draw.circle(
                screen,
                (100, 200, 255),
                (int(point[0]), int(point[1])),
                2
            )

        # Draw projectile
        pygame.draw.circle(
            screen,
            (255, 100, 100),
            (int(self.x), int(self.y)),
            self.radius
        )