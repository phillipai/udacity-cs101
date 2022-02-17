#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    first = 0
    second = 1
    counter = 0
    while counter < n:
        second += first
        first += second
        counter += 2
    if n % 2 ==0:
        return first
    else:
        return second

#print fibonacci(36)
#>>> 14930352

print fibonacci(100)
#>>> 14930352
