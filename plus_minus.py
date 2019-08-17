#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zer = 0
    for elm in arr:
        if elm > 0:
            pos += 1
        elif elm < 0:
            neg += 1
        else:
            zer += 1
    print(pos/n)
    print(neg/n)
    print(zer/n)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
