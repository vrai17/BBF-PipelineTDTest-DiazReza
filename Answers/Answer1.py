import math

# Dimensions of the grid
width, height = 41, 41
radius = 17.5  # Radius of the circle
thickness = 3  # Thickness of the circle
center_x, center_y = width // 2, height // 2  # Center of the circle

for y in range(height):
    for x in range(width):
        distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        if radius - thickness / 2 < distance < radius + thickness / 2:
            print(".", end="")
        else:
            print("#", end="")
    print()
