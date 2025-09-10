def mid_point_circle(radius):
    x = 0
    y = radius
    p = 1 - radius
    points = []

    def plot_circle_points(xc, yc, x, y):
        return [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ]

    xc, yc = 0, 0
    while x <= y:
        points += plot_circle_points(xc, yc, x, y)
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

    return points

# Plot
circle = mid_point_circle(20)
x_vals, y_vals = zip(*circle)
plt.figure()
plt.title("Mid-Point Circle")
plt.plot(x_vals, y_vals, 'bo')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
