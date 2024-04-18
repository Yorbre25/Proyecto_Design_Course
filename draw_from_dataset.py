from draw_points import img_to_pcd_NYU
import os

# Ruta de la carpeta que contiene las imágenes
carpeta = 'input/datasets/nyu_study_0003_out'

# Obtener una lista de todos los archivos en la carpeta
archivos = os.listdir(carpeta)

# Filtrar solo los archivos de imagen (png y jpg)
imagenes = [archivo for archivo in archivos if archivo.endswith(('.png', '.jpg'))]

# Iterar sobre cada imagen
for imagen in imagenes:
    # Construir la ruta completa de la imagen png
    ruta_png = os.path.join(carpeta, imagen)
    
    # Construir la ruta completa de la imagen jpg
    ruta_jpg = os.path.join(carpeta, os.path.splitext(imagen)[0] + '.jpg')
    
    # Verificar si ambas imágenes existen
    if os.path.exists(ruta_png) and os.path.exists(ruta_jpg):
        # Cargar ambas imágenes
        output_path = os.path.join('output/dataset', os.path.splitext(imagen)[0] + '.ply')  
        img_to_pcd_NYU(ruta_jpg, ruta_png, output_path)