# Anagram

import math
import os
import random
import re
import sys
import re
from collections import Counter
# Complete the anagram function below.
def anagram(s):

    if len(s)%2==0:
        
        splits = [item[0:int(len(s)/2)], item[int(len(s)/2):int(len(s))]]
        #print(splits)
        print(len(splits[0])-sum((Counter(splits[0]) & Counter(splits[1])).values()))

    else:
        print(-1)
    
    


if __name__ == '__main__':

    anagram_list = [input() for _ in range(int(input()))]

    for item in anagram_list:
        anagram(item)

# Making Anagrams

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    return len(s1)+len(s2)-sum((Counter(s1) & Counter(s2)).values())*2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
