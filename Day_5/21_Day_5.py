# Matrix problem EASY. -> Diagonal Difference

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
   
    # Write your code here
    for i in range(len(arr)):
        for j in range(len(arr)):
            #print(j)
            if(i==j):
                sum1 = sum1+arr[i][j]
            if(len(arr)-j-1==i):
                sum2 = sum2+arr[i][j]


    return abs(sum1-sum2)

if __name__ == '__main__':
   
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

#Matrix problem HARD -> Matrix Script

#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
joined_str = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for i in range(m):
    for j in matrix:
        joined_str.append(j[i])
j_str_2 = ''.join(joined_str)
y = (re.sub(r'([\w])[^A-Za-z1-9]+([\w])', r'\1 \2', str(j_str_2)))
z = (re.sub('  ',' ',y))
 
print(z)



