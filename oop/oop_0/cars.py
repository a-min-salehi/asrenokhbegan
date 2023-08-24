class Car:
    wheels_count = 4

    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model
        self.doors_count = 4


input_color = input("enter a color")

c1 = Car(input_color, "toyota", "prius")

c2 = Car(input_color, "saypa", "pride111")

c1.model = "landcruiser"

print(f"the c1 car  = {c1.color} {c1.brand} {c1.model}")
print(f"wheels = {c1.wheels_count}")
print(f"doors = {c1.doors_count}")

print(f"the c2 car  = {c2.color} {c2.brand} {c2.model}")
print(f"wheels = {c2.wheels_count}")
print(f"doors = {c2.doors_count}")
