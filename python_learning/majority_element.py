'''Boyer–Moore algorithm
Given an array arr[]. Find the majority element in the array. If no majority 
element exists, return -1.

Note: A majority element in an array is an element that appears strictly more than 
arr.size()/2 times in the array.

Examples:

Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
Output: 1
Explanation: Since, 1 is present more than 7/2 times, so it is the majority element.
Input: arr[] = [7]
Output: 7
Explanation: Since, 7 is single element and present more than 1/2 times, so it is the 
majority element.
Input: arr[] = [2, 13]
Output: -1
Explanation: Since, no element is present more than 2/2 times, so there is no majority 
element.
'''
class Solution:
    def majorityElement(self, arr):
        candidate = None
        count = 0

        # Phase 1: Find a potential candidate
        for num in arr:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Phase 2: Verify candidate
        if arr.count(candidate) > len(arr)//2:
            return candidate
        return -1
# Example usage:
sol = Solution()
print(sol.majorityElement([2,13]))  # Output: 1