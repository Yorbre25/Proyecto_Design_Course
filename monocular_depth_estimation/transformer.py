import os
from PIL import Image
from transformers import pipeline
import matplotlib.pyplot as plt

def show_depth_map(depth_map_array):
    plt.imshow(depth_map_array, cmap='gray')
    plt.colorbar()
    plt.show()

def make_8bit_image(depth_map_array):
    max_pixel_value = depth_map_array.max()
    depth_map_array = depth_map_array / max_pixel_value * 255
    depth_map_array = depth_map_array.astype('uint8')
    return depth_map_array

def save_image(depth_map_array, output_path):
    image = Image.fromarray(depth_map_array)
    image.save(output_path)


def get_depth_map(depth_estimation_pipeline, image_path, output_path):

    # load input image
    image = Image.open(image_path)
    if image.size != (640, 480):
        image = image.resize((640, 480))

    # Realizar la estimación de profundidad en la imagen de entrada
    depth_map = depth_estimation_pipeline(image)

    # access the predicted depth map
    depth_map_tensor = depth_map['predicted_depth']

    # Convertir el tensor de profundidad en una matriz numpy y mostrarlo
    depth_map_array = depth_map_tensor[0].numpy()
    depth_map_array = make_8bit_image(depth_map_array)

    # show_depth_map(depth_map_array)
    save_image(depth_map_array, output_path)

def run_depth_estimation(input_dir, output_dir):
    # load depth-estimation pipeline
    depth_estimation_pipeline = pipeline("depth-estimation", model="vinvino02/glpn-nyu")

    dir_list = os.listdir(input_dir)
    for filename in dir_list:
        if filename != None and filename.endswith(('.png', '.jpg')):
            image_path = input_dir + filename
            output_path = output_dir + filename.split('.')[0] + '_depth.png'
            get_depth_map(depth_estimation_pipeline, image_path, output_path)


input_dir = "input/"
output_dir = "output/"
run_depth_estimation(input_dir, output_dir)