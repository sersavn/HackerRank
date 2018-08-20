x = [1,2,3,4,5,6,7,8,9,0]
y = [1,3,5,7,9]
#
#print([item for item in x if item not in y])

se = [1,2,2,2,3,4,5,9,10,12]

def almostIncreasingSequence(sequence):
    seq = se
    sets = list(set(x))
    #dif = len(sequence) - len(set(sequence))
    return([item for item in seq if item not in sets])
    #return(seq)
print(almostIncreasingSequence(se))
