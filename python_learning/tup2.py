"""You are given a tuple numbers that contains a A.P sequence integer. You need to calculate the next three sequences of numbers and return the whole sequence in a tuple.

Examples:

Input: tup = ( 1, 5, 9, 13, 17)
Output: 1 5 9 13 17 21 25 29
Explanation: It's an increasing sequence 
by 4. So, the next three numbers are 17+4= 21,  21+4=25, 25+4=29."""

def nextThreeAP(numbers):
    #code here
    d = numbers[1] - numbers[0]
    next1 = numbers[-1] + d
    next2 = next1 + d
    next3 = next2 + d
    numbers = list(numbers)
    numbers.append(next1)
    numbers.append(next2)
    numbers.append(next3)
    numbers = tuple(numbers)
    return numbers
# Example usages    