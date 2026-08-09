import math
import pygame


class Projectile:

    def __init__(self, x, y, speed, angle, ground, gravity):

        self.x = x
        self.y = y
        self.ground = ground

        self.start_x = x
        self.max_height = 0
        self.time_elapsed = 0
        self.landed = False

        radians = math.radians(angle)

        self.vx = speed * math.cos(radians)
        self.vy = -speed * math.sin(radians)

        self.gravity = gravity

        self.radius = 8

        self.path = []

    def update(self, dt):

        if self.landed:
            return  # nothing left to track once it's down

        self.time_elapsed += dt

        self.vy += self.gravity * dt

        self.x += self.vx * dt
        self.y += self.vy * dt

        # Track how high above the ground it's gotten
        current_height = self.ground - self.y
        if current_height > self.max_height:
            self.max_height = current_height

        # Stop at ground level
        if self.y >= self.ground:
            self.y = self.ground
            self.vx = 0
            self.vy = 0
            self.landed = True

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