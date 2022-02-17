# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(num1, num2, num3):
    if num1 >= num2 > num3 or num1 > num3 > num2:
        return num1
    if num2 > num1 > num3 or num2 > num3 > num1:
        return num2
    if num3 > num1 > num2 or num3 > num2 > num1:
        return num3



print biggest(3, 6, 9)
#>>> 9

#print biggest(6, 9, 3)
#>>> 9

#print biggest(9, 3, 6)
#>>> 9

#print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9
