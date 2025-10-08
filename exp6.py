import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define cube vertices
vertices = np.array([
    [0, 0, 0],  # 0
    [1, 0, 0],  # 1
    [1, 1, 0],  # 2
    [0, 1, 0],  # 3
    [0, 0, 1],  # 4
    [1, 0, 1],  # 5
    [1, 1, 1],  # 6
    [0, 1, 1],  # 7
])

# Define the 6 faces by grouping vertex indices
faces = [
    [vertices[i] for i in [0, 1, 2, 3]],  # Bottom face
    [vertices[i] for i in [4, 5, 6, 7]],  # Top face
    [vertices[i] for i in [0, 1, 5, 4]],  # Front face
    [vertices[i] for i in [2, 3, 7, 6]],  # Back face
    [vertices[i] for i in [1, 2, 6, 5]],  # Right face
    [vertices[i] for i in [0, 3, 7, 4]],  # Left face
]

# Define distinct colors for each face
face_colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'orange']

# Create figure and 3D axis
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Create the 3D polygon collection and add to the axis
cube = Poly3DCollection(faces, facecolors=face_colors, edgecolors='black', linewidths=1, alpha=0.9)
ax.add_collection3d(cube)

# Set axis labels and title
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Cube with Colored Faces")

# Set equal aspect ratio for all axes
ax.set_box_aspect([1, 1, 1])

# Set limits for better visualization (optional)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

# Show the plot
plt.show()
