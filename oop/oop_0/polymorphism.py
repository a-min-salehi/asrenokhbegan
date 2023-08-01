# Method Overloading
class Calculator:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a+b


calculator = Calculator()
print(calculator.add(2, 3))
print(calculator.add(2, 3, 4))
