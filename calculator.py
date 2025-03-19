# calculator.py
class Calculator:
    def add(self, x, y,z):
        return x + y + z
    
    def subtract(self, x, y, z):
        return x - y -z
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    
calc = Calculator()
print(calc.add(1,2,3))