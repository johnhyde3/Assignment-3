'''1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.'''


z=int(input("Enter a number: "))
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(z)
print("Factorial of",z,"is",result)

''' Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)'''


import math
z=int(input("Enter a number: "))
print("Square root:",math.sqrt(z))
print("Logarithm:",math.log(z))
print("Sine:",math.sin(z))


