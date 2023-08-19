class Circle:
    pi = 3.14

    def __init__(self, x, y, radius):
        if x ** 2 + y ** 2 == radius ** 2:
            self.x = x
            self.y = y
            self.radius = radius
        else:
            raise ValueError("Invalid values for x, y, and radius. They should satisfy x^2 + y^2 = radius^2")

    def calculate_area(self):
        return self.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * self.pi * self.radius

    def __str__(self):
        return f"Circle with center at ({self.x}, {self.y}), radius {self.radius}"


# Create instances of Circle
try:
    circle1 = Circle(3, 4, 5)
    print(circle1)
    print("Area:", circle1.calculate_area())
    print("Perimeter:", circle1.calculate_perimeter())
except ValueError as e:
    print(e)

try:
    circle2 = Circle(1, 2, 2)
    print(circle2)
    print("Area:", circle2.calculate_area())
    print("Perimeter:", circle2.calculate_perimeter())
except ValueError as e:
    print(e)
