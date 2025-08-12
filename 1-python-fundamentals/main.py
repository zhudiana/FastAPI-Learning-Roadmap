class Calculate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

calc = Calculate(4,6)
print(calc.add())