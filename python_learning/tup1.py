"""You are given a tuple numbers that contains integers. You need to return a tuple containing doubles of given numbers.

Examples:

Input: tup = (4, 5, 1, 2, 3, 5)
Output: 8 10 2 4 6 10
Explanation: multiplied numbers by 2.
Input: tup = (3, 1, 4, 7, 2, 6, 4)
Output: 6 2 8 14 4 12 8
Explanation: multiplied number by 2
"""
def doubleTup(numbers):
    #code here
    for i in range(len(numbers)):
        numbers = list(numbers)
        numbers[i] *= 2
        numbers = tuple(numbers)
    return numbers
# Example usages
print(doubleTup((4, 5, 1, 2, 3, 5)))
print(doubleTup((3, 1, 4, 7, 2, 6, 4))) 