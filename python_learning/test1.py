def isPalindrome(s):
    #code here
    word = s.lower()
    rev = word[::-1]
    if word == rev:
        print("true")
    else:
        print("false")
    return Noneend=""
isPalindrome("Madan")