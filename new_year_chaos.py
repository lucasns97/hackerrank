#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def swap(q, i, j):
    temp = q[i]
    q[i] = q[j]
    q[j] = temp
    return q

def minimumBribes(q):
    vec = []
    bribes = 0
    for k in range(2):
        for i in range(len(q)-1, 0, -1):
            if q[i] < q[i-1]:
                q = swap(q, i, i-1)
                bribes += 1
    for i in range(len(q)-1, 0, -1):
        if q[i] < q[i-1]:
            print('Too chaotic')
            return
    print(bribes)
    return

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
