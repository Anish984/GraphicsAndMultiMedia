import numpy as np
import matplotlib.pyplot as plt

def scanline_fill(polygon, canvas_size=(100, 100)):
    canvas = np.zeros(canvas_size, dtype=int)
    n = len(polygon)

    # Find min and max y
    ymin = min(p[1] for p in polygon)
    ymax = max(p[1] for p in polygon)

    for y in range(ymin, ymax + 1):
        intersections = []
        for i in range(n):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % n]

            if y1 == y2:
                continue  # Ignore horizontal edges
            if (y >= min(y1, y2)) and (y < max(y1, y2)):
                # Find x intersection
                x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                intersections.append(int(x))

        intersections.sort()
        for i in range(0, len(intersections), 2):
            if i + 1 < len(intersections):
                for x in range(intersections[i], intersections[i + 1]):
                    if 0 <= x < canvas_size[1] and 0 <= y < canvas_size[0]:
                        canvas[y, x] = 1
    return canvas

# Define polygon (square/triangle etc.)
polygon = [(20, 20), (60, 20), (50, 50), (30, 60)]

# Fill polygon
canvas = scanline_fill(polygon)

# Plot
plt.figure()
plt.title("Scanline Polygon Fill")
plt.imshow(canvas, cmap='gray', origin='lower')
x, y = zip(*(polygon + [polygon[0]]))
plt.plot(x, y, 'r-')  # draw the polygon outline
plt.grid(False)
plt.show()
