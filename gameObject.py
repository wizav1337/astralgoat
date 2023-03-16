import pygame
from PIL import Image

class GameObject:
    def __init__(self, x, y, width, height, image_obj):
        # Converting the PIL Image object to a pygame Surface object
        image_obj = image_obj.convert('RGBA')  # Ensure the image is in RGBA mode
        image_data = image_obj.tobytes("raw", 'RGBA')
        image_size = image_obj.size
        image = pygame.image.fromstring(image_data, image_size, 'RGBA')

        # Scaling the image
        self.image = pygame.transform.scale(image, (width, height))

        # Saving the parameters as properties of the class objects
        self.x = x
        self.y = y
        self.width = width
        self.height = height
