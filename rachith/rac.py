class calculator:
    numb = 2

    def __init__(self,a, b, c):
        self.first = a
        self.second = b
        self.third = c


    def multy(self):
        return self.first * self.second *self.third - self.numb


obj = calculator(3, 4, 5)
print(obj.multy())

obj1 = calculator(5, 6, 8)
print(obj1.multy())