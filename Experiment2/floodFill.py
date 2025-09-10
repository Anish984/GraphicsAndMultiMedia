def flood_fill(canvas, x, y, target_color=0, replacement_color=2):
    if x < 0 or x >= canvas.shape[1] or y < 0 or y >= canvas.shape[0]:
        return
    if canvas[y, x] != target_color:
        return

    canvas[y, x] = replacement_color

    flood_fill(canvas, x+1, y, target_color, replacement_color)
    flood_fill(canvas, x-1, y, target_color, replacement_color)
    flood_fill(canvas, x, y+1, target_color, replacement_color)
    flood_fill(canvas, x, y-1, target_color, replacement_color)

# Create a shape to fill
canvas = np.zeros((100, 100), dtype=int)
polygon = [(30, 30), (70, 30), (70, 70), (30, 70)]
canvas = scanline_fill(polygon, canvas.shape)

# Flood fill inside a region that was NOT filled (outside the polygon)
flood_fill(canvas, 10, 10, target_color=0, replacement_color=2)

# Plot
plt.figure()
plt.title("Flood Fill")
plt.imshow(canvas, cmap='nipy_spectral', origin='lower')
plt.grid(False)
plt.show()
