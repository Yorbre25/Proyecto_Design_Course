from draw_points import img_to_pcd_NYU
import os

# Ruta de la carpeta que contiene las imágenes
carpeta = 'input/datasets/bottle'

# Obtener una lista de todos los archivos en la carpeta
archivos = os.listdir(carpeta)

# Filtrar solo los archivos de imagen (png y jpg)
imagenes = [archivo for archivo in archivos if archivo.endswith(('.png', '_depth.png'))]

# Iterar sobre cada imagen
for imagen in imagenes:
    original_ruta = os.path.join(carpeta, imagen)

    depth_map_ruta = os.path.join(carpeta, os.path.splitext(imagen)[0] + '_depth.png')
    
    if os.path.exists(depth_map_ruta) and os.path.exists(original_ruta):
        # Cargar ambas imágenes
        output_path = os.path.join('output/dataset', os.path.splitext(imagen)[0] + '.ply')  
        img_to_pcd_NYU(original_ruta, depth_map_ruta, output_path)