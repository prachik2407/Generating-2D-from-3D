# Generating-2D-from-3D
Generating a 2D Plan from a 3D STL Mesh using Voxelization

Key Points:
Correct File Path: Ensure the file path to the STL file is correct. The raw string (r'...') format is appropriate for Windows paths.
Voxel Grid Creation: The voxel grid is created based on the mesh bounds and a specified voxel size.
Points Inside the Mesh: Using mesh.contains(points) to check if the points are inside the mesh.
2D Plan: The plan is obtained by summing the voxel grid along the z-axis and plotting it using matplotlib.

Additional Notes:
Ensure the trimesh library and its dependencies are installed: pip install trimesh.
Make sure the STL file cube.stl exists at the specified location.
If any issues arise, check for error messages and confirm that the file path, library versions, and data are all correct.
