class rectangle :
    def __init__(self, length, width):
        print("test")

        self.length = length
        self.width = width
        print(self.length, self.width)
    def area(self):
        print("Area of rectangle:", self.length * self.width)

    def perimeter(self):
         print("Perimeter of rectangle:", self.length + self.width)

my_rectangle = rectangle(10,20)
my_rectangle.area()
