# Try except:

def save_divide(num, den):
    try:
        return num // den
    except ZeroDivisionError:
        print('Error: cannot divide by zero')
        return none
    else:
        print(f"Something went wrong")
    finally:
        print(f"Process Complete")
# test

numerator = int(input('Enter the numerator value: -'))
denominator = int(input('Enter the denominator value: -'))


print(save_divide(numerator, denominator))

# second test

import math

def squareR(num):
    try:
        return math.sqrt(num)
    except ValueError:
        print(f"Cannot get the square root of a negative number. Please try again")
    else:
        print(f"Something went wrong")
    finally:
        print(f"Process Complete")

x = int(input('Enter the value of x: '))
print(squareR(x))

