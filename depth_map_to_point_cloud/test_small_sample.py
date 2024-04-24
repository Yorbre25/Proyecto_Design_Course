#  import same root modules
from draw_points import *

input = "input/datasets/bottle/"
original_path = input + "bottle_center.png"
depth_path = input + "bottle_center_depth.png"
img_to_pcd_NYU(original_path, depth_path, "output/output.ply")