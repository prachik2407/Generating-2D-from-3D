import trimesh
import numpy as np
import matplotlib.pyplot as plt
import os

# Print the current working directory
print("Current Working Directory:", os.getcwd())

# Ensure the file path is correct
file_path = r'd:\Internship\python\cube.stl'

# Load the STL file
mesh = trimesh.load(file_path)

# Create a voxel grid
voxel_size = 0.1
bounds = mesh.bounds
x = np.arange(bounds[0, 0], bounds[1, 0], voxel_size)
y = np.arange(bounds[0, 1], bounds[1, 1], voxel_size)
z = np.arange(bounds[0, 2], bounds[1, 2], voxel_size)
xx, yy, zz = np.meshgrid(x, y, z)
points = np.vstack((xx.ravel(), yy.ravel(), zz.ravel())).T

# Check which points are inside the mesh
inside = mesh.contains(points)
voxel_grid = np.zeros(xx.shape, dtype=bool)
voxel_grid.ravel()[inside] = True

# Get the 2D floor plan by summing along the z-axis
floor_plan = voxel_grid.sum(axis=2) > 0

# Plot the floor plan
plt.imshow(floor_plan, cmap="gray", origin='lower')
plt.title("2D Floor Plan")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
