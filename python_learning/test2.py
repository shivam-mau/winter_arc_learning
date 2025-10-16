'''Given two strings denoting non-negative numbers s1 and s2. Calculate the 
sum of s1 and s2.

For example if s1 = "121" and s2 = "99", the result will be "220".  
Note: The numbers can be very large (up to 10^6 digits), hence converting them to integer 
adding may not work.'''
def findSum(s1, s2):
    #code here
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    res = ""
    n1 = len(s1)
    n2 = len(s2)
    s1 = s1[::-1]
    s2 = s2[::-1]

    carry = 0
    for i in range(n1):
        sum = (ord(s1[i]) - ord('0')) + (ord(s2[i]) - ord('0')) + carry
        res += chr(sum % 10 + ord('0'))
        carry = sum // 10

    for i in range(n1, n2):
        sum = (ord(s2[i]) - ord('0')) + carry
        res += chr(sum % 10 + ord('0'))
        carry = sum // 10

    if carry:
        res += chr(carry + ord('0'))

    res = res[::-1]
    return res