import pygame
import zipfile
import io
from PIL import Image
from gameObject import GameObject
from player import Player
from enemy import Enemy
class Game:
    def __init__(self):
        self.width = 600
        self.height = 600
        self.white_colour = (255, 255, 255)

        self.game_window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        #loading assets
        def load_assets(archive):
            assets = {}
            with zipfile.ZipFile(archive, 'r') as zfile:
                for name in zfile.namelist():
                    with zfile.open(name) as file:
                        assets[name] = io.BytesIO(file.read())
            return assets

        archive = 'ASSETS1.Z'
        assets_in_memory = load_assets(archive)
        with assets_in_memory['background.png'] as background_file:
            background_asset = background_file.read()
        with assets_in_memory['treasure.png'] as treasure_file:
            treasure_asset = treasure_file.read()
        with assets_in_memory['player.png'] as player_file:
            player_asset = player_file.read()


        # Loading the game assets
        # NOTE: We're using different values and image paths here specifically for the Trinket application
        self.background = GameObject(0, 0, self.width, self.height, assets_in_memory['background.png'])
        self.treasure = GameObject(280, 35, 40, 40, assets_in_memory['treasure.png'])
        self.player = Player(280, 530, 40, 40, assets_in_memory['player.png'], 1)

        # Array of enemies
        self.enemies = [
            Enemy(0, 450, 40, 40, assets_in_memory['enemy.png'], 3),
            Enemy(250, 300, 40, 40, assets_in_memory['enemy.png'], 3),
            Enemy(0, 150, 40, 40, assets_in_memory['enemy.png'], 3),
        ]

    def draw_objects(self):
        self.game_window.fill(self.white_colour)

        # Blitting assets to the screen
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))

        # Looping through the enemies
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))

        pygame.display.update()

    def move_objects(self, player_direction):
        self.player.move(player_direction, self.height)
        for enemy in self.enemies:
            enemy.move(self.width)

    def check_if_collided(self):
        # Checks for collisions between the player and the enemies
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                return True
        # Checks for collisions between the player and the treasure
        if self.detect_collision(self.player, self.treasure):
            return True
        return False

    # Collision detection
    @staticmethod
    def detect_collision(object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False
        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False
        return True

    def run_game_loop(self):
        player_direction = 0

        while True:
            # Handle events
            events = pygame.event.get()
            for event in events:
                # If there's a QUIT event, we break the loop and exit the method
                if event.type == pygame.QUIT:
                    return

                # Listening for when a key is pressed down on the keyboard
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1

                # Stopping the player when arrow keys are released
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0

            # Execute logic
            self.move_objects(player_direction)

            # Update display
            self.draw_objects()

            if self.check_if_collided():
                # If there's any collision, we quit the game
                return

            # NOTE: We've altered this value so that the codes run more smoothly
            self.clock.tick(120)
