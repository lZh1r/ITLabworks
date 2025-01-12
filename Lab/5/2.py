class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

a = Circle(9)

print(a.get_radius())
a.set_radius(11)
print(a.get_radius())