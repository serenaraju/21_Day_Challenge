# IntroTutorial for sorting

import math
import os
import random
import re
import sys

# Complete the introTutorial function below.

def introTutorial(V, arr):
    return arr.index(V)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# Insertion sort 1


import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    x = n-1
    m = arr[x]
 
    while(arr[x-1]>m and x-1>=0):
      
        arr[x] = arr[x - 1]
        print(*arr, sep = ' ')
        x-=1
    if x<0:
        arr[0] = m
    else:
        arr[x] = m
    print(*arr, sep = ' ')




if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
