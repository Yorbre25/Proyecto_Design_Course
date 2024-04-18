#  import same root modules
from draw_points import *

input = "input/small_sample/"
original_path = input + "sample_2.png"
depth_path = input + "depth_sample_2.png"
img_to_pcd_NYU(original_path, depth_path, "output/output.ply")