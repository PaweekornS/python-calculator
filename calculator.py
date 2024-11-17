class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b # problem 1: change b-a to a-b

    def multiply(self, a, b):
        result = 0
        if a < 0 and b < 0:   # both number are negative
            a = (a - a) - a
            b = (b - b) - b
        elif b < 0:  # one of the number is negative
            b = (b - b) - b
            a = -a

        for i in range(b):  # failure 2: change range(b + 1) to range(a)
            result = self.add(result, a)   # change add result from a to b

        return result

    def divide(self, a, b):
        result = 0
        sign = 1

        if b == 0:
            raise ValueError('Division by zero is not allowed')

        if a < 0 and b < 0:
            a = -a
            b = -b
        elif b < 0:
            b = -b
            sign = -1
        elif a < 0:
            a = -a
            sign = -1

        while a >= b:  # failure 3: change > to >=
            a = self.subtract(a, b)
            result += 1

        if sign == 1:
            return result
        else:
            return result - result - result
    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
    
        if a < 0:
            if b < 0:
                a = a - a - a
                b = b - b -b 
                while a >= b:
                    a -= b
                return -a
            else:
                while a < 0:
                    a += b
        elif a >= b:   # fault 4: change > to >=
            if b < 0:
                b = b - b - b
                while a > 0:
                    a -= b
            else:
                while a >= b:
                    a -= b

        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(-7, -5))