# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

def measure_udacity(list):
    occurence = 0
    for e in list:
        if e[0] == 'U':
            occurence += 1
    return occurence


print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

#print measure_udacity(['Umika','Umberto'])
#>>> 2
