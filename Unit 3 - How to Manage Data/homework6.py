# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def column_check(list_name):
    result = True
    length = len(list_name)
    list = [list_name]
    check_column = []
    add = 0
            
    while add < length:
        check_column = []
        for s in list_name:
            column = s[add]
            if column in check_column:
                return False
            check_column.append(column)
        add += 1
    return result

def row_check(list_name):
    result = True
    
    for e in list_name:
        check_row = []
        for s in e:
            if s in check_row:
                return False
            check_row.append(s)
    return result

def check_sudoku(mylist):
    check = []
    length = len(mylist)
    add = 0
    result = True
    
    if row_check(mylist) == False:
        return False
    if column_check(mylist) == False:
        return False
    for e in mylist:
        for sublist in e:
            if sublist <= 0:
                return False
            if sublist > length:
                return False
            if not sublist % 1 == 0: #check if its a whole number
                return False
    return result


#print check_sudoku(incorrect)
#>>> False

#print check_sudoku(correct)
#>>> True

#print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

#print check_sudoku(incorrect4)
#>>> False

#print check_sudoku(incorrect5)
#>>> False
