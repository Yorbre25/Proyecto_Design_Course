import numpy as np # linear algebra
from PIL import Image
from numpy import asarray

def extract_color_image(img_path):
    img = Image.open(img_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = asarray(img)
    img = img/255.0 # normalize RGB values to [0, 1]

    height, width, channels = img.shape
    length = height * width

    color_list = img.reshape((length, channels)) # array of RGB values
    return color_list
