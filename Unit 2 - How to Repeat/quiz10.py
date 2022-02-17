# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    if n == 0:
        return 1
    start = n
    while n > 1:
        n = n - 1
        start = start * n
    return start


#print factorial(4)
#>>> 24
print factorial(0)
#>>> 120
#print factorial(6)
#>>> 720
