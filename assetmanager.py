import pickle
import io
from PIL import Image

# Load the assets into memory
assets = {
    'background.png': Image.open('assets/background.png'),
    'treasure.png': Image.open('assets/treasure.png'),
    'player.png': Image.open('assets/player.png'),
    'enemy.png': Image.open('assets/enemy.png')
}

# Serialize and save the assets to a custom binary file
with open('ASSETS1.bin', 'wb') as binary_file:
    pickle.dump(assets, binary_file)