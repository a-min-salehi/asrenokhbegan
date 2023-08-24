class Rectangle:
    def __init__(self, width, height):
        if height > width:
            self.width = width
            self.height = height
        else:
            raise ValueError("Invalid values for width and height , height most be larger than width")

    def __eq__(self, other):
        if self.width == other.width and self.height == other.height:
            return True
        return False

    def calculate_area(self):
        return self.width * self.height

    def __lt__(self, other):
        if self.calculate_area() < other.calculate_area():
            return True
        return False

    def __gt__(self, other):
        if self.calculate_area() > other.calculate_area():
            return True
        return False


r1 = Rectangle(8, 12)

r2 = Rectangle(5, 10)

print(r1 == r2)
print(r1 > r2)
print(r1 < r2)
