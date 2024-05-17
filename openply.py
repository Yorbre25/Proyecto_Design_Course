import open3d as o3d

path_to_pcd = "output/cuadra/pcd/IMG_1701.ply"
pcd = o3d.io.read_point_cloud(path_to_pcd)
o3d.visualization.draw_geometries([pcd])