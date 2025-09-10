import matplotlib.pyplot as plt

def draw_bresenham_line(x_start, y_start, x_end, y_end):
    x_vals = []
    y_vals = []

    dx = abs(x_end - x_start)
    dy = abs(y_end - y_start)

    x, y = x_start, y_start
    step_x = 1 if x_end > x_start else -1
    step_y = 1 if y_end > y_start else -1

    if dy <= dx:
        decision = 2 * dy - dx
        for _ in range(dx + 1):
            x_vals.append(x)
            y_vals.append(y)
            if decision >= 0:
                y += step_y
                decision -= 2 * dx
            x += step_x
            decision += 2 * dy
    else:
        decision = 2 * dx - dy
        for _ in range(dy + 1):
            x_vals.append(x)
            y_vals.append(y)
            if decision >= 0:
                x += step_x
                decision -= 2 * dy
            y += step_y
            decision += 2 * dx

    return x_vals, y_vals

# Input
x1 = int(input("Start X: "))
y1 = int(input("Start Y: "))
x2 = int(input("End X: "))
y2 = int(input("End Y: "))

x_data, y_data = draw_bresenham_line(x1, y1, x2, y2)

plt.plot(x_data, y_data, marker='o', color='blue')
plt.title("Bresenham's Line Drawing")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
