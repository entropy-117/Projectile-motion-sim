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
    PIXELS_PER_METER = 50

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Projectile Motion Simulator")

        self.font = pygame.font.SysFont(None, 28)

        self.clock = pygame.time.Clock()

        self.running = True

        # Ground position
        self.ground = 650

        # Angle slider
        self.angle_slider = Slider(self.screen, 50, 20, 200, 20, min=1, max=180, step=1, initial=60)
        self.angle_label = TextBox(
            self.screen, 260, 15, 60, 30,
            fontSize=18,
            colour=(30, 30, 30),
            textColour=(255, 255, 255),
            borderColour=(200, 200, 200)
        )
        self.angle_label.disable()

        # Speed slider (shown in m/s, converted to pixels/s internally)
        self.speed_slider = Slider(self.screen, 350, 20, 200, 20, min=1, max=20, step=1, initial=10)
        self.speed_label = TextBox(
            self.screen, 560, 15, 60, 30,
            fontSize=18,
            colour=(30, 30, 30),
            textColour=(255, 255, 255),
            borderColour=(200, 200, 200)
        )
        self.speed_label.disable()

        # Gravity slider (shown in m/s^2, converted to pixels/s^2 internally)
        self.gravity_slider = Slider(self.screen, 650, 20, 200, 20, min=1, max=25, step=1, initial=10)
        self.gravity_label = TextBox(
            self.screen, 860, 15, 60, 30,
            fontSize=18,
            colour=(30, 30, 30),
            textColour=(255, 255, 255),
            borderColour=(200, 200, 200)
        )
        self.gravity_label.disable()

        # Create one projectile
        self.Projectile = Projectile(
            x=100,
            y=self.ground,
            speed=self.speed_slider.getValue() * self.PIXELS_PER_METER,
            angle=self.angle_slider.getValue(),
            ground=self.ground,
            gravity=self.gravity_slider.getValue() * self.PIXELS_PER_METER
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
                        speed=self.speed_slider.getValue() * self.PIXELS_PER_METER,
                        angle=self.angle_slider.getValue(),
                        ground=self.ground,
                        gravity=self.gravity_slider.getValue() * self.PIXELS_PER_METER
                    )

    def update(self, dt):
        """Update game objects."""

        self.Projectile.update(dt)

    def draw(self):
        """Draw everything."""

        self.screen.fill(self.BACKGROUND)

        # Category labels below sliders
        angle_caption = self.font.render("Angle", True, (255, 255, 255))
        self.screen.blit(angle_caption, (50, 45))

        speed_caption = self.font.render("Speed", True, (255, 255, 255))
        self.screen.blit(speed_caption, (350, 45))

        gravity_caption = self.font.render("Gravity (m/s^2)", True, (255, 255, 255))
        self.screen.blit(gravity_caption, (650, 45))

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

        # Ball position display (0 at ground, increasing upward)
        display_y = self.ground - self.Projectile.y
        position_text = self.font.render(
            f"X: {int(self.Projectile.x)}  Y: {int(display_y)}",
            True,
            (255, 255, 255)
        )
        self.screen.blit(position_text, (50, 75))

        # Slider value labels
        self.angle_label.setText(str(int(self.angle_slider.getValue())))
        self.speed_label.setText(str(int(self.speed_slider.getValue())))
        self.gravity_label.setText(str(int(self.gravity_slider.getValue())))

        pygame_widgets.update(self.event_list)

        pygame.display.flip()

    def run(self):
        """Main game loop."""

        while self.running:

            dt = self.clock.tick(self.FPS) / 1000

            self.events()
            self.update(dt)
            self.draw()

        pygame.quit()


if __name__ == "__main__":
    app = Main()
    app.run()