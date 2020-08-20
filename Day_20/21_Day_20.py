#!/bin/python3

# Divisible Sum Pairs

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    track = set()
    for i in range(0,n):
        for j in range(0,n):
            if i<j and (ar[i]+ar[j])%k == 0:

                count+=1
                track.add((ar[i],ar[j]))
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
