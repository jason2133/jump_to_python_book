class Fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = Fourcal()
a.setdata(6, 9)
print(a.sum())
print(a.sub())
print(a.mul())
print(a.div())
