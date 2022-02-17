# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    if len(s) == 0:
        return True
    if s[-1] != s[0]:
        return False
    if s[1] != s[-2]:
        return False
    if s[-1] == s[0]:
        return True
 
 
print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('andrea')
#>>> True
