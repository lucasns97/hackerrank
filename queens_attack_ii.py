#!/bin/python3

import math
import os
import random
import re
import sys

def possibleMove(r_q, c_q, mov_r, mov_c, step, n, k, obstacles):
    test_r = r_q + mov_r*step
    test_c = c_q + mov_c*step
    if test_r <= 0 or test_r > n:
        return False, k
    elif test_c <= 0 or test_c > n:
        return False, k
    else:
        for obs in range(k):
            if test_r != obstacles[obs][0]:
                continue
            elif test_c == obstacles[obs][1]:
                obstacles.remove([test_r, test_c])
                k -= 1
                return False, k
        return True, k

def removeNotSeenObstacles(obstacles, k, r_q, c_q):
    vec = []
    for i in range(k):
        dif_r = abs(obstacles[i][0] - r_q)
        dif_c = abs(obstacles[i][1] - c_q)
        if dif_r != 0 and dif_c != 0:
            if dif_r != dif_c:
                vec.append([obstacles[i][0], obstacles[i][1]])
    for i in vec:
        obstacles.remove(i)


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    moves = 0
    removeNotSeenObstacles(obstacles, k, r_q, c_q)
    k = len(obstacles)
    mov_r = [1, 1, 0, -1, -1, -1, 0, 1]
    mov_c = [0, -1, -1, -1, 0, 1, 1, 1]

    for m in range(len(mov_r)):
        step = 1
        go, k = possibleMove(r_q, c_q, mov_r[m], mov_c[m], step, n, k, obstacles)
        while go:
            moves += 1
            step += 1
            go, k = possibleMove(r_q, c_q, mov_r[m], mov_c[m], step, n, k, obstacles)

    return moves



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
