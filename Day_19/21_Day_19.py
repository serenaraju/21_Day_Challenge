#!/bin/python3

# Day of the programmer

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year<=1917:
        if year%4 == 0:
            return ("12.09.{}".format(year))
        else:
            return ("13.09.{}".format(year))

    elif year>=1919:
        if (year%400 == 0 or (year%4 == 0 and year%100 != 0)):
            return ("12.09.{}".format(year))
        else:
            return ("13.09.{}".format(year))
    
    else:
        return ("26.09.{}".format(year))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
