"""
Example of using pylint package
"""

def add(n1, n2):
    """
    Function returning the sum of 2 arguments
    """
    return n1 + n2

NUM_1 = 4
NUM_2 = 5
TOTAL = add(NUM_2, NUM_2)

print(f"The sum of {NUM_1} and {NUM_2} is {TOTAL}\n")
