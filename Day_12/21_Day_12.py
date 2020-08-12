# Birthday Chocolate -> EASY

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    for i in range(len(s)-(m-1)):
        sum_choc = 0
        print(sum_choc)
        for j in range(m):
            sum_choc+=s[i+j]
            print(sum_choc)
        if sum_choc == d:
            count+=1
            
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
