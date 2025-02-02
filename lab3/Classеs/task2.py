class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length ** 2

a = float(input("a:"))
shape = Shape()
print("Area of Shape:", shape.area())  

square = Square(5)
print("Area of Square:", square.area()) 