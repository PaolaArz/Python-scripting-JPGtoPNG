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
	print(filename)
	im = Image.open(original_dir + '/' + filename)
	rgb_im = im.convert('RGB')
	name = filename[:-4]
	rgb_im.save(new_dir + '/' + name + '.png')
