import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def translation_matrix(tx, ty, tz):
    """Create a translation matrix."""
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

def scaling_matrix(sx, sy, sz):
    """Create a scaling matrix."""
    return np.array([
        [sx, 0,  0,  0],
        [0,  sy, 0,  0],
        [0,  0,  sz, 0],
        [0,  0,  0,  1]
    ])

def rotation_matrix_z(angle):
    """Create a rotation matrix around the Z-axis."""
    rad = np.radians(angle)
    cos_a = np.cos(rad)
    sin_a = np.sin(rad)
    return np.array([
        [cos_a, -sin_a, 0, 0],
        [sin_a,  cos_a, 0, 0],
        [0,      0,     1, 0],
        [0,      0,     0, 1]
    ])

def apply_transform(vertices, matrix):
    """Apply a transformation matrix to a list of vertices."""
    transformed = []
    for v in vertices:
        vec = np.array([*v, 1])  # Convert to homogeneous coordinate
        result = matrix @ vec
        transformed.append(result[:3])  # Drop the homogeneous coordinate
    return transformed

def draw_edges(ax, vertices, edges, color):
    """Draw edges connecting vertices on the 3D plot."""
    for start, end in edges:
        xs = [vertices[start][0], vertices[end][0]]
        ys = [vertices[start][1], vertices[end][1]]
        zs = [vertices[start][2], vertices[end][2]]
        ax.plot(xs, ys, zs, color=color)

# Define the cube's vertices and edges
vertices = [
    (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),
    (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)
]

edges = [
    (0,1), (1,2), (2,3), (3,0),  # bottom face
    (4,5), (5,6), (6,7), (7,4),  # top face
    (0,4), (1,5), (2,6), (3,7)   # vertical edges
]

# Define transformations: translate, scale, then rotate
T = translation_matrix(2, 2, 0)
S = scaling_matrix(1.5, 1.5, 1.5)
R = rotation_matrix_z(45)

# Combine transformations: note the order matters (R then S then T)
combined_transform = T @ S @ R

# Apply transformation to cube vertices
transformed_vertices = apply_transform(vertices, combined_transform)

# Plot original and transformed cube
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

draw_edges(ax, vertices, edges, 'blue')         # Original cube in blue
draw_edges(ax, transformed_vertices, edges, 'red')  # Transformed cube in red

ax.set_title("3D Transformation of Cube (Translation, Scaling, Rotation)")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_box_aspect([1, 1, 1])
plt.show()
