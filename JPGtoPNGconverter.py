#python3 JPGtoPNGconverter.py Poxedex/ newDirectory/

import sys
import os
from PIL import Image

original_dir = sys.argv[1]
new_dir = sys.argv[2]

#create new folder if it doesn't exist
if not os.path.exists(new_dir):
    os.mkdir(new_dir)

#convert images to png and saves into new folder
for filename in os.listdir(original_dir):
	im = Image.open(f'{original_dir}/{filename}')
	name = os.path.splitext(filename)[0]
	im.save(f'{new_dir}/{name}.png', 'png')
