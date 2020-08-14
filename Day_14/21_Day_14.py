#!/bin/python3
#Breaking the records -> EASY

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    
    high_score = scores[0]
    low_score = scores[0]
    new_low = 0
    new_hi = 0

    for i in range(len(scores)):
        score = scores[i]
        if score < low_score:
            low_score = score
            new_low += 1
        elif score > high_score:
            high_score = score
            new_hi += 1
    return(new_hi,new_low)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#Find digits -> EASY

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    temp = n
    count = 0
    while temp!=0:
        x = temp%10
        print(x)
        if x == 0:
            temp = int(temp/10)
            continue
        elif n%x==0:
            count+=1
        temp = int(temp/10)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

# Utopian Tree

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    ht = 1
    for i in range(n):
        if i%2==0:
            ht*=2
        else:
            ht+=1
    return ht

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
