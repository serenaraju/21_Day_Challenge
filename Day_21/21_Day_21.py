# Cut the sticks -> EASY

#!/bin/python3

import math
import os
import random
import re
import sys
from math import inf

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    x = min(arr)
    print(x)
    count,z_c = 0,0
    count_list = []
    while(1):
        count = 0
        for i in range(len(arr)):
            if (arr[i]>=x and arr[i]!=inf): 
                arr[i] -= x
                count+=1
            if (arr[i]<=0):
                arr[i] = inf
                z_c+=1
            
        count_list.append(count)
        if z_c == len(arr):
                break
        x = min(arr)
        print(x)

    return count_list
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    
# Append and Delete

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    count = 0
    move = 0
    for i in range(min(len(t),len(s))):
        if (s[i]==t[i]):
            count+=1
        else:
            break

    if len(s)+len(t)-2*count <=k:
        return "Yes"
    
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
