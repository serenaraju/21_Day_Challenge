# Marc's Cakewalk -> EASY

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    miles = 0
    calorie = sorted(calorie, reverse = True)
    for i in range(len(calorie)):
        miles += calorie[i]*(2**i)
        #print(calorie[i])
    return miles

if __name__ == '__main__':
    

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    print(result)

# Candies -> MEDIUM

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    candy = [1]*n
    #print(candy)
    for i in range(n-1):
        if arr[i+1] > arr[i]:
            candy[i+1] = candy[i] + 1
    for i in range(n-1 , 0 , -1):
        if arr[i-1] > arr[i] and candy[i-1]<=candy[i]:
            candy[i-1] = candy[i] + 1
       
    #print(candy)

    return sum(candy)

if __name__ == '__main__':
   
    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    print(result)

# Minimum Absolute Difference in an Array -> EASY 

#!/bin/python3

import math
import os
import random
import re
import sys
from math import inf
# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    mini = inf
    for i in range(len(arr)-1):
        if abs(arr[i+1]-arr[i])<mini:
            mini = abs(arr[i+1]-arr[i])

    return mini   




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
