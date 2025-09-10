import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    if dy <= dx:
        p = 2 * dy - dx
        for _ in range(dx):
            points.append((x, y))
            x += sx
            if p < 0:
                p += 2 * dy
            else:
                y += sy
                p += 2 * (dy - dx)
    else:
        p = 2 * dx - dy
        for _ in range(dy):
            points.append((x, y))
            y += sy
            if p < 0:
                p += 2 * dx
            else:
                x += sx
                p += 2 * (dx - dy)
    points.append((x2, y2))
    return points

# Plot
line = bresenham_line(2, 2, 15, 10)
x_vals, y_vals = zip(*line)
plt.figure()
plt.title("Bresenham Line")
plt.plot(x_vals, y_vals, 'ro')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
