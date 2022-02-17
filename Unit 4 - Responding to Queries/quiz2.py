# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    for k in index:
        if keyword in k[0]:
            return k[1]
    else:
        return []


print lookup(index,'udacity')
#>>> ['http://udacity.com','http://npr.org']
