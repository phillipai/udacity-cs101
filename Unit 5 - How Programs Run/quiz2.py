# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    e = 0
    hastable = []
    while e < nbuckets:
        hastable.append([])
        e += 1
    return hastable
    
make_hashtable(5)
#Expected result: [[], [], [], [], []]
