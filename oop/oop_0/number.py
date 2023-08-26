class Number:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x - other.x


# Creating objects
n1 = Number(3)
n2 = Number(1)

print(type(n2))

# Using operator overloading
distance = n1 + n2

print(f"n1 + n2: {distance}")
