# Hackerrank in a string -> EASY

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    hk = "hackerrank"
    m = 0
    count = 0
    for i in s:
        if i == hk[m]:
            count+=1
            m+=1
            if count == 10:
                return "YES"
    return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
