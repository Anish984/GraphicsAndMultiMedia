import matplotlib.pyplot as plt

# Constants representing clipping edges
LEFT, RIGHT, BOTTOM, TOP = range(4)

def is_inside(point, edge, clip_window):
    """Check if a point is inside the given clipping edge."""
    x, y = point
    xmin, xmax, ymin, ymax = clip_window

    if edge == LEFT:
        return x >= xmin
    elif edge == RIGHT:
        return x <= xmax
    elif edge == BOTTOM:
        return y >= ymin
    elif edge == TOP:
        return y <= ymax

def compute_intersection(p1, p2, edge, clip_window):
    """Compute the intersection point of an edge with a clipping boundary."""
    x1, y1 = p1
    x2, y2 = p2
    xmin, xmax, ymin, ymax = clip_window

    if x1 == x2:  # Avoid division by zero
        x = x1
    if y1 == y2:  # Avoid division by zero
        y = y1

    if edge == LEFT:
        x = xmin
        y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
    elif edge == RIGHT:
        x = xmax
        y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
    elif edge == BOTTOM:
        y = ymin
        x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
    elif edge == TOP:
        y = ymax
        x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)

    return (x, y)

def sutherland_hodgman_clip(polygon, clip_window):
    """Clip a polygon using the Sutherland-Hodgman algorithm."""
    output_list = polygon

    for edge in [LEFT, RIGHT, BOTTOM, TOP]:
        input_list = output_list
        output_list = []
        if not input_list:
            break

        prev_point = input_list[-1]
        for curr_point in input_list:
            if is_inside(curr_point, edge, clip_window):
                if not is_inside(prev_point, edge, clip_window):
                    output_list.append(compute_intersection(prev_point, curr_point, edge, clip_window))
                output_list.append(curr_point)
            elif is_inside(prev_point, edge, clip_window):
                output_list.append(compute_intersection(prev_point, curr_point, edge, clip_window))
            prev_point = curr_point

    return output_list

def draw_polygon(points, color, label, linestyle='-'):
    """Draw a polygon using matplotlib."""
    if not points:
        return
    x, y = zip(*(points + [points[0]]))  # Close the polygon
    plt.plot(x, y, color=color, label=label, linestyle=linestyle, linewidth=2)

# --- Main Section ---

# Define clipping window: (xmin, xmax, ymin, ymax)
clip_window = (100, 300, 100, 300)

# Define original polygon points
original_polygon = [
    (50, 150), (200, 50), (350, 150),
    (350, 300), (250, 350), (150, 300)
]

# Perform clipping
clipped_polygon = sutherland_hodgman_clip(original_polygon, clip_window)

# Plotting
plt.figure(figsize=(8, 8))
draw_polygon(original_polygon, 'blue', "Original Polygon")
draw_polygon(
    [(clip_window[0], clip_window[2]), (clip_window[1], clip_window[2]),
     (clip_window[1], clip_window[3]), (clip_window[0], clip_window[3])],
    'black', "Clipping Window", linestyle='--'
)
draw_polygon(clipped_polygon, 'red', "Clipped Polygon")

# Display settings
plt.title("Sutherland-Hodgman Polygon Clipping")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
