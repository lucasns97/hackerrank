#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def bin_search(lo, hi, vec, key):
    mid = (lo + hi)//2
    if hi < lo:
        return mid+2  ######?????
    if vec[mid] == key:
        print('passei', key)
        return mid+1
    elif vec[mid] > key:
        return bin_search(mid+1, hi, vec, key)
    else:
        return bin_search(lo, mid-1, vec, key)

def remove_duplicates(vec):
    ans = []
    n = len(vec)
    ans.append(vec[0])
    for i in range(1,n):
        if vec[i] == vec[i-1]:
            continue
        else:
            ans.append(vec[i])
    return ans


def climbingLeaderboard(scores, alice):
    new_scores = remove_duplicates(scores)
    n = len(new_scores)
    print(new_scores)
    print(alice)
    ans = []
    for ali_score in alice:
        pos = bin_search(0, n-1, new_scores, ali_score)
        print(pos)
        ans.append(pos)

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
