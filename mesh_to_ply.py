import open3d as o3d
import numpy as np

# Load the mesh from a file
mesh = o3d.io.read_triangle_mesh("./K24AC201.obj")

# Compute the center of the mesh
mesh_center = mesh.get_center()

# Translate the mesh to center it at the origin
mesh.translate(-mesh_center)

# Ensure the mesh has normals
if not mesh.has_vertex_normals():
    mesh.compute_vertex_normals()

# Sample points on the mesh surface with a given number of points
number_of_points = 1_000_000
pcd = mesh.sample_points_poisson_disk(number_of_points)

# Save the point cloud as a PLY file
o3d.io.write_point_cloud("output_file.ply", pcd)

# Optional: Visualize the point cloud
o3d.visualization.draw_geometries([pcd])
