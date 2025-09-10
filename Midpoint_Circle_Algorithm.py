import matplotlib.pyplot as plt

# Input
center_x = int(input("Center X: "))
center_y = int(input("Center Y: "))
radius = int(input("Radius: "))

x = 0
y = radius
decision = 1 - radius

x_plot = []
y_plot = []

def add_symmetric_points(cx, cy, x, y):
    offsets = [
        (x, y), (-x, y), (x, -y), (-x, -y),
        (y, x), (-y, x), (y, -x), (-y, -x)
    ]
    for dx, dy in offsets:
        x_plot.append(cx + dx)
        y_plot.append(cy + dy)

add_symmetric_points(center_x, center_y, x, y)

while x < y:
    x += 1
    if decision < 0:
        decision += 2 * x + 1
    else:
        y -= 1
        decision += 2 * x + 1 - 2 * y

    add_symmetric_points(center_x, center_y, x, y)

plt.plot(x_plot, y_plot, 'o', color='purple')
plt.plot(center_x, center_y, 'ro')  # Mark center
plt.title("Midpoint Circle Drawing")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis('equal')
plt.grid(True)
plt.show()


