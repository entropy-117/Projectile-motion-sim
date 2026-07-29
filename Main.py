import pygame
from projectile import Projectile
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox    

class Main:

    WIDTH = 1000
    HEIGHT = 700
    FPS = 60
    BACKGROUND = (30, 30, 30)
    ANGLE = 60
    SPEED = 400

    def __init__(self):
        pygame.init()

        self.font = pygame.font.SysFont(None, 28)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.angle_slider = Slider(self.screen, 50, 20, 200, 20, min=1, max=90, step=1, initial=60)
        self.angle_label = TextBox(self.screen, 260, 15, 50, 30, fontSize=18, colour=(30, 30, 30), textColour=(255, 255, 255), borderColour=(0, 0, 0))
        self.angle_label.disable()

        self.speed_slider = Slider(self.screen, 350, 20, 200, 20, min=0, max=1200, step=10, initial=400)
        self.speed_label = TextBox(self.screen, 560, 15, 60, 30, fontSize=18,colour=(30, 30, 30),textColour=(255, 255, 255))
        self.speed_label.disable()

        pygame.display.set_caption("Projectile Motion Simulator")

        self.clock = pygame.time.Clock()

        self.running = True

        # Ground position
        self.ground = 650

        # Create one projectile
        self.Projectile = Projectile(
            x=100,
            y=self.ground,
            speed=self.SPEED,
            angle=self.ANGLE,
            ground = self.ground
        )

    def events(self):
        """Handle all user input."""

        self.event_list = pygame.event.get()

        for event in self.event_list:

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:

                # Restart projectile
                if event.key == pygame.K_SPACE:

                    self.Projectile = Projectile(
                        x=100,
                        y=self.ground,
                        speed=self.SPEED,
                        angle=self.ANGLE,
                        ground = self.ground
                    )

    def update(self, dt):
        """Update game objects."""

        self.Projectile.update(dt)

    def draw(self):
        """Draw everything."""

        self.screen.fill(self.BACKGROUND)

        # Category labels below sliders
        angle_caption = self.font.render("Angle", True, (255, 255, 255))
        self.screen.blit(angle_caption, (125, 50))

        speed_caption = self.font.render("Speed", True, (255, 255, 255))
        self.screen.blit(speed_caption, (425, 50))

        # Instructions
        instructions = self.font.render("Press SPACE to launch", True, (255, 255, 255))
        self.screen.blit(instructions, (self.WIDTH // 2 - 100, self.HEIGHT - 40))

        # Draw ground
        pygame.draw.line(
            self.screen,
            (200, 200, 200),
            (0, self.ground),
            (self.WIDTH, self.ground),
            2
        )

        self.Projectile.draw(self.screen)

        self.angle_label.setText(str(int(self.angle_slider.getValue())))
        self.speed_label.setText(str(int(self.speed_slider.getValue())))

        pygame_widgets.update(self.event_list)

        pygame.display.flip()

    def run(self):
        """Main game loop."""

        while self.running:

            dt = self.clock.tick(self.FPS) / 1000

            self.SPEED = self.speed_slider.getValue()
            self.ANGLE = self.angle_slider.getValue()
            self.events()
            self.update(dt)
            self.draw()

        pygame.quit()


if __name__ == "__main__":
    app = Main()
    app.run()