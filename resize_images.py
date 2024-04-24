import os
from PIL import Image

input_dir = "monocular_depth_estimation/input/"
output_dir = "monocular_depth_estimation/input/"

dir_list = os.listdir(input_dir)
for filename in dir_list:
    if filename != None and filename.endswith(('.png', '.jpg')):
        image_path = input_dir + filename
        output_path = output_dir + filename

        image = Image.open(image_path)
        image = image.resize((640, 480))

        image.save(output_path)
