class circle:
    def __init__(self,radius):
        self.radius = radius

    def area_circle(self):
        print("Area of the circle", 3.14159265359 * self.radius**2)
    def perimeter_circle(self):
        print("Perimeter of the Circle:", 2*3.14159265359*self.radius)

areaCircle = circle(4)
perimeterCircle = circle(4)
areaCircle.area_circle()
perimeterCircle.perimeter_circle()
        
