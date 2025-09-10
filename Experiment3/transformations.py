import numpy as np
import matplotlib.pyplot as plt

# --------- Define the Original Polygon (a triangle) ----------
polygon = np.array([
    [1, 1],
    [4, 1],
    [2.5, 4]
])

# --------- Transformation Functions ----------

def translate(polygon, tx, ty):
    """Translate polygon by tx and ty"""
    translation_vector = np.array([tx, ty])
    return polygon + translation_vector

def scale(polygon, sx, sy):
    """Scale polygon with respect to origin"""
    scaling_matrix = np.array([[sx, 0], [0, sy]])
    return polygon @ scaling_matrix

def rotate(polygon, angle_degrees):
    """Rotate polygon around origin"""
    theta = np.radians(angle_degrees)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    return polygon @ rotation_matrix

# --------- Visualization Function ----------

def plot_polygon(polygons, labels, title="2D Transformations"):
    """Plot multiple polygons with labels"""
    plt.figure()
    colors = ['blue', 'green', 'red', 'purple']
    
    for i, poly in enumerate(polygons):
        poly_closed = np.vstack([poly, poly[0]])  # close the shape
        plt.plot(poly_closed[:, 0], poly_closed[:, 1], marker='o', label=labels[i], color=colors[i % len(colors)])
    
    plt.title(title)
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

# --------- Apply Transformations ----------

translated = translate(polygon, tx=5, ty=3)
scaled     = scale(polygon, sx=2, sy=0.5)
rotated    = rotate(polygon, angle_degrees=45)

# --------- Plot Results ----------
plot_polygon(
    [polygon, translated, scaled, rotated],
    labels=["Original", "Translated", "Scaled", "Rotated"]
)
