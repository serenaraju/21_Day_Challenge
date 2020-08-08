#  Recursion 3 -> EASY

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n == 1:
        return 1
    else:
        return (factorial(n-1)*n)

if __name__ == '__main__':

    n = int(input())

    result = factorial(n)

    print(result)

# Binary Search Trees -> EASY


class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):

        if root is None:
            return -1
        else:
            lheight = self.getHeight(root.left)
            rheight = self.getHeight(root.right)

            if(lheight>rheight):
                return lheight+1
            else:
                return rheight+1
        
        #Write your code here

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       