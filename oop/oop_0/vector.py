class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Creating objects
v1 = Vector(3, 4)
v2 = Vector(1, 2)

# Using operator overloading
distance = v1 + v2
print(f"Distance between v1 and v2: {distance}")

# Using the __abs__ function
magnitude_v1 = abs(v1)
print(f"Magnitude of v1: {magnitude_v1}")

# Using the __mul__ function
scale = 2
scaled_v1 = v1 * scale
print(f"Scaled v1 by {scale}: {scaled_v1}")
