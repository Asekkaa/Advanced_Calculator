# mymath.py

# Addition function
def add(x, y):
    return x + y

# Subtraction function
def subtract(x, y):
    return x - y

# Multiplication function
def multiply(x, y):
    return x * y

# Division function
def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y

# Power function
def power(x, y):
    result = 1
    for _ in range(int(y)):
        result *= x
    return result

# Square root function (using Newton's method for approximation)
def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    guess = x / 2.0
    tolerance = 0.00001
    while abs(guess * guess - x) > tolerance:
        guess = (guess + x / guess) / 2.0
    return guess

# Sine function (using Taylor series approximation)
def sin(x):
    result = 0
    term = x
    n = 1
    while abs(term) > 0.00001:
        result += term
        n += 2
        term *= -x * x / (n * (n - 1))
    return result

# Cosine function (using Taylor series approximation)
def cos(x):
    result = 1
    term = 1
    n = 0
    while abs(term) > 0.00001:
        n += 2
        term *= -x * x / (n * (n - 1))
        result += term
    return result

# Tangent function (sin / cos)
def tan(x):
    return sin(x) / cos(x)

# Logarithm function (using natural logarithm approximation)
def log(x, base=2.718281828459045):  # base 'e' by default
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    result = 0
    n = (x - 1) / (x + 1)
    term = n
    i = 1
    while abs(term) > 0.00001:
        result += term / i
        i += 2
        term *= n * n
    return 2 * result / log(base)

# Factorial function
def factorial(x):
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
