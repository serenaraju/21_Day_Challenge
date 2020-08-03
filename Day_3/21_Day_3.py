# Detecting floating point number EASY

import re 

float_num = [input() for i in range(int(input()))]


for item in float_num:
    float_re = re.compile(r"^[+-0123456789][0-9]*\.[0-9]*$")
    x = float_re.search(item)==None
    if x==True:
        print('False')
    else:
        print('True')

#

# Find vowels MEDIUM
import re

vow = input()

vow_re = re.compile(r"(?<=[a-zA-Z])[AEIOUaeiou]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]")

all_vow = re.findall(vow_re,vow)

new_vow = list()
#new_vow = [item for item in all_vow if item!='']
for item in all_vow:
    if( item!=''):
        item_1 = item[:-1]
        new_vow.append(item_1)


if len(new_vow) == 0:
    print("-1")
for i in new_vow:
    print(i)


# Hex Color Code HARD

import re

hex_code = [input() for i in range(int(input()))]

hex_re = re.compile(r'(?<!^)(#(?:[0-9A-Fa-f]{3}){1,2})')

brack = False

for item in hex_code:


    regex = re.findall(hex_re,item)
    #print(regex)
    if regex != None:
        for item in regex:
            print(item)

