from PIL import Image
from os.path import dirname
path_bloco = dirname(__file__) + '/blocos/bloco.png'

HEIGHT_BLOCO, WIDTH_BLOCO = Image.open(path_bloco).size
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (168, 168, 168)
WIDTH = 1000
HEIGHT = 500
