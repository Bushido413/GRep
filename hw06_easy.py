# Задание-1:
class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.side1 = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
        self.side2 = ((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** 0.5
        self.side3 = ((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2) ** 0.5

    def get_perimeter(self):
            perimeter = self.side1 + self.side2 + self.side3
            return perimeter

    def get_half_perimeter(self):
        half_perimeter = self.get_perimeter() * 0.5
        return half_perimeter

    def get_square(self):
        p = self.get_half_perimeter()
        square = (p*(p-self.side1)*(p-self.side2)*(p-self.side3)) ** 0.5
        return square

    def get_height(self):
        s = self.get_square()
        height = (s*2) / self.side1
        return height


m = Triangle(0, 0, 0, 1, 1, 0)
print('Площадь треугольника:', m.get_height())


# Задание-1:
class Trapezoid:

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.side1 = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
        self.side2 = ((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2) ** 0.5
        self.side3 = ((self.x3 - self.x4) ** 2 + (self.y3 - self.y4) ** 2) ** 0.5
        self.side4 = ((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2) ** 0.5

    def verify(self):
        diagonal1 = ((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** 0.5
        diagonal2 = ((self.x4 - self.x2) ** 2 + (self.y4 - self.y2) ** 2) ** 0.5
        return diagonal1 == diagonal2

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4

    def get_height(self):
        return ((self.side1**2) - (((self.side4 - self.side2)**2 + (self.side1**2) - (self.side3**2)) / ((self.side4-self.side2)*2))**2) ** 0.5

    def square(self):
        h = self.get_height()
        return (h*0.5) * (self.side2 + self.side4)


n = Trapezoid(0, 0, 1, 1, 2, 1, 3, 0)
print(n.square())
