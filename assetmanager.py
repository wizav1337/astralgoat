import zipfile

def create_zip_archive(files, output_file):
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zfile:
        for file in files:
            zfile.write(file)

assets = ['assets/background.png', 'assets/enemy.png', 'assets/player.png', 'assets/treasure.png']
output_file = 'ASSETS1.Z'

create_zip_archive(assets, output_file)