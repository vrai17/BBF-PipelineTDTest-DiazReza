import math

class AsciiCircle:
    def __init__(self, width, height, radius, thickness):
        self.width = width
        self.height = height
        self.radius = radius
        self.thickness = thickness
        self.center_x = width // 2
        self.center_y = height // 2

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                distance = math.sqrt((x - self.center_x) ** 2 + (y - self.center_y) ** 2)
                if self.radius - self.thickness / 2 < distance < self.radius + self.thickness / 2:
                    print(".", end="")
                else:
                    print("#", end="")
            print()

# Define the parameters
width, height = 41, 41
radius = 17.5  # Radius of the circle
thickness = 3  # Thickness of the circle

# Create an instance of AsciiCircle
circle = AsciiCircle(width, height, radius, thickness)

# Draw the circle
circle.draw()
