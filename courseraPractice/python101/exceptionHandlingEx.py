# Exception Handling Practice 
#
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

numerator = int(input('Enter the numerator value: '))
denominator = int(input('Enter the denominator value: '))


print(save_divide(numerator, denominator))

# second test

import math

def squareR(num):
    try:
        result = math.sqrt(num)
        print(f"Result: {result}")
    except ValueError:
        print(f"Cannot get the square root of a negative number. Please try again")
    else:
        print(f"No error encountered")
    finally:
        print(f"Process Complete")

x = float(input('Enter the value of x: '))
squareR(x)

# third test

def cal(num2):
    try:
        result = num2 // (num2 - 5)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error occurred during calculation")
    except ValueError:
        print('Invalid value')
    except ZeroDivisionError:
        print('Error: Cannot divide by zero')
    else:
        print(f"No error encountered")
    finally:
        print(f"Process Finished")

y = int(input(f"Place the value of y: "))
cal(y)


