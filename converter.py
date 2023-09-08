from PIL import Image, ImageFilter
import glob
import re
import os


class Converter():
    def __init__(self, filepath, type):
        self.filepath =  f'{filepath}\*.{type}'
        self.type = type

        
    def convert_to_png(self):
        try:
            for image in glob.glob(self.filepath):
                new_image = Image.open(image)
                name, exe = os.path.splitext(os.path.basename(image))
                new_image.save(f'converted\{name}.png')

        except TypeError as error:
            print(f"Failed to find image: {error}")
