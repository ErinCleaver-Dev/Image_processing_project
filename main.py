from converter import Converter
from pathlib import Path
import os 
from sys import argv

new_folder = 'converted'
folder = 'pokedex'

try:
    folder = argv[1]
    new_folder = argv[2]
except: 
    print('Used defalt directory')

new_path = Path(__file__).parent / new_folder
if not os.path.exists(new_path):
    os.makedirs(new_path)

path = Path(__file__).parent / folder
convert = Converter(path, 'jpg', new_folder)

convert.convert_to_png()