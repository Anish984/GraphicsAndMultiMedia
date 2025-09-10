import matplotlib.pyplot as plt

# Input
radius_x = int(input("Radius along X: "))
radius_y = int(input("Radius along Y: "))

a = radius_x
b = radius_y

x = 0
y = b

# Region 1
d1 = b**2 - a**2 * b + 0.25 * a**2
x_coords = []
y_coords = []

while 2 * b**2 * x <= 2 * a**2 * y:
    for sign_x in [1, -1]:
        for sign_y in [1, -1]:
            x_coords.append(sign_x * x)
            y_coords.append(sign_y * y)

    if d1 < 0:
        x += 1
        d1 += 2 * b**2 * x + b**2
    else:
        x += 1
        y -= 1
        d1 += 2 * b**2 * x - 2 * a**2 * y + b**2

# Region 2
d2 = b**2 * (x + 0.5)**2 + a**2 * (y - 1)**2 - a**2 * b**2

while y >= 0:
    for sign_x in [1, -1]:
        for sign_y in [1, -1]:
            x_coords.append(sign_x * x)
            y_coords.append(sign_y * y)

    if d2 > 0:
        y -= 1
        d2 -= 2 * a**2 * y + a**2
    else:
        x += 1
        y -= 1
        d2 += 2 * b**2 * x - 2 * a**2 * y + a**2

plt.scatter(x_coords, y_coords, color='green', s=15)
plt.title("Midpoint Ellipse Drawing")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis('equal')
plt.grid(True)
plt.show()
