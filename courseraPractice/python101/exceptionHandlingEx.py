# Try except:

def save_divide(num, den):
    try:
        return num // den
    except ZeroDivisionError:
        print('Error: cannot divide by zero')
        return none

# test

numerator = int(input('Enter the numerator value: -'))
denominator = int(input('Enter the denominator value: -'))


print(save_divide(numerator, denominator))
