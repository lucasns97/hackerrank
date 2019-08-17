#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.

def argmax(arr):
    max_e = -99999999999
    max_id = None
    for i in range(len(arr)):
        if arr[i] > max_e:
            max_e = arr[i]
            max_id = i
    return max_id

def argmin(arr):
    min_e = 99999999999
    min_id = None
    for i in range(len(arr)):
        if arr[i] < min_e:
            min_e = arr[i]
            min_id = i
    return min_id

def miniMaxSum(arr):
    amax = argmax(arr)
    min_sum = 0
    for i in range(len(arr)):
        if i == amax:
            continue
        min_sum += arr[i]

    amin = argmin(arr)
    max_sum = 0
    for i in range(len(arr)):
        if i == amin:
            continue
        max_sum += arr[i]
    
    sums = [str(min_sum), str(max_sum)]
    print(' '.join(sums))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
