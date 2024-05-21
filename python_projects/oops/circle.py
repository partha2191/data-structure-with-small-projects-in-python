class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

circle1 = Circle(21)
print("Area of the circle is:", circle1.area())
print("Perimeter of the circle is:", circle1.perimeter())
    
