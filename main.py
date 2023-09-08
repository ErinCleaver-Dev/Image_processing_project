from converter import Converter
from pathlib import Path

path = Path(__file__).parent / 'pokedex'
convert = Converter(path, 'jpg')

convert.convert_to_png()