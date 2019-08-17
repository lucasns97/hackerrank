#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    n_a = len(apples)
    n_b = len(oranges)

    ans_a = 0
    ans_b = 0

    for i in range(n_a):
        if a + apples[i] >= s and a + apples[i] <= t:
            ans_a += 1
        
    for i in range(n_b):
        if b + oranges[i] <= t and b + oranges[i] >= s:
            ans_b += 1
        
    print(ans_a)
    print(ans_b)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
