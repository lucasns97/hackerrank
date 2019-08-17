#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def swap(vec, i, j):
    temp = vec[i]
    vec[i] = vec[j]
    vec[j] = temp
    return vec

def minimumSwaps(arr):
    i = 0
    count = 0
    while i < len(arr):
        elm = arr[i]-1
        #print(elm)
        while elm != i:
            arr = swap(arr, i, elm)
            count += 1
            elm = arr[i]-1
        i += 1
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
