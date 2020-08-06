# Numpy library practice 

# Arrays -> EASY
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr[::-1],float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# Shape and Reshape -> EASY

import numpy

seq_initial = [input().split() ]
seq = numpy.array(seq_initial,int)

print(numpy.reshape(seq,(3,3)))