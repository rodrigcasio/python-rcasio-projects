"""
Functions from 'stats.py' (module)
"""

def mean(numbers):
    """
    This function returns the mean of a given list of numbers.
    Mean is calculated by the sum of all numbers divided  by the count of numbers
    """
    if not numbers:
        print(f"no elements given, please try again")
        return 0
    else:
        return sum(numbers) / len(numbers)

def median(numbers):
    """
    Function returns the median of a given list of numbers
    The median is the middle value when numbers are sorted
    (If there is an even number of observations, it returns the average of the two middle numbers
    """
    numbers.sort()
    
    # check the number of elements from given list is even
    if len(numbers) % 2 == 0:
        median_1 = numbers[len(numbers) // 2]
        median_2 = numbers[len(numbers) // 2 - 1]

        my_median = (median_1 + median_2) / 2 # avg of two middle values
    else:
        # if the number of elements from the given list is odd
        my_median = numbers[len(numbers) // 2] 

    return my_median


