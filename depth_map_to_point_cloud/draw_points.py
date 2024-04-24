import open3d as o3d
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import imageio.v3 as iio
from PIL import Image
from numpy import asarray
from extract_color import extract_color_image

def img_to_pcd_NYU(original_path, depth_path, pcd_path):
    # Depth camera parameters:
    FX_DEPTH = 5.8262448167737955e+02
    FY_DEPTH = 5.8269103270988637e+02
    CX_DEPTH = 3.1304475870804731e+02
    CY_DEPTH = 2.3844389626620386e+02
    
    depth_image = Image.open(depth_path).convert('L')
    depth_image = asarray(depth_image)
    
    # get depth resolution:
    height, width = depth_image.shape
    length = height * width
    # compute indices:
    jj = np.tile(range(width), height)
    ii = np.repeat(range(height), width)
    # rechape depth image
    z = depth_image.reshape(length)
    # compute pcd:
    pcd = np.dstack([(ii - CX_DEPTH) * z / FX_DEPTH,
                 (jj - CY_DEPTH) * z / FY_DEPTH,
                 z]).reshape((length, 3))

    pcd_o3d = o3d.geometry.PointCloud()  # create point cloud object
    pcd_o3d.points = o3d.utility.Vector3dVector(pcd)  # set pcd_np as the point cloud points

    colors = extract_color_image(original_path)
    pcd_o3d.colors = o3d.utility.Vector3dVector(colors)  
    # Visualize:

    camera_position = np.array([2, 2, 2])
    lookat = camera_position + np.array([0, 0, -1])  # La cámara mira hacia abajo
    up = np.array([-5, 1, 5])  # Dirección hacia arriba
    front = np.array([-1, -1, -1])  # Dirección frontal
    zoom = 0.8

    o3d.visualization.draw_geometries([pcd_o3d], lookat=lookat, up=up, front=front, zoom=zoom)
    
    # Save:
    # o3d.io.write_point_cloud(pcd_path, pcd_o3d)




        

