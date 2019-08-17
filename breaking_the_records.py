#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):

    high_score = scores[0]
    low_score = scores[0]
    highs = 0
    lows = 0

    for score in scores:
        if score > high_score:
            highs += 1
            high_score = score
        elif score < low_score:
            lows += 1
            low_score = score
    
    return [highs, lows]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
