from task2.shape import Shape

class Rectangle(Shape):
    def __init__(self, color: str, width: float, height: float):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
