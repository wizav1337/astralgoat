from gameObject import GameObject


class Enemy(GameObject):

    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)

        self.speed = speed

    # The enemies move horizontally across the screen
    def move(self, max_width):
        # If the enemy is all the way to the left, changes its speed to be positive so it'll go to the right
        if self.x <= 0:
            self.speed = abs(self.speed)
        # If the enemy is all the way to the right, changes the speed to be negative instead so it'll go back to the left
        elif self.x >= max_width - self.width:
            self.speed = -self.speed

        self.x += self.speed