#Collections.OrderedDict() HACKERRANK Printing cumulative cost of a list of items -> dictionary
import re

track = dict()

uni_val = [input() for i in range(int(input()))]

for i in uni_val:
    x = re.findall(r'\d+',i)
    y = re.findall(r'(?![\s])[A-Z]*',i)
    y = [item for item in y if item!='']
    y = ' '.join(y)
    if y in track:
        track[y] =  track[y]+int(x[0])

    else:
        track[y] = int(x[0])


for key,val in track.items():
    print("{} {}".format(key,val))

#Company logo HACKERRANK Finding the top 3 most occurred alphabets in a string and sorting them -> dictionary and tuples
import math
import os
import random
import re
import sys

def find_logo(s):
    track = dict()

    for no in range(len(s)):
        
        if s[no] in track:
            track[s[no]] =  track[s[no]]+1

        else:
            track[s[no]] = 1
    c = 0
    top_3 = dict()
    track = sorted(track.items())
    
    tuple_list = sorted(track, reverse = True, key = lambda x : x[1])
    #print(tuple_list)
    for item in tuple_list:
        c = c+1
        if c == 4:
            break
        top_3[item[0]] = item[1]
    for key,val in top_3.items():
        print("{} {}".format(key,val))

if __name__ == '__main__':
    s = input()
    find_logo(s)

#Word Order HACKERRANK Printing the count of repeated strings from input -> dictionary
track = dict()

uni_val = [input() for i in range(int(input()))]

for i in uni_val:
    if i in track:
        track[i] =  track[i]+1

    else:
        track[i] = 1
        
print(len(track))
l = list()
for key,val in track.items():
    l.append(val)

print(*l, sep = ' ')
