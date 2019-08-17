#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        string = []
        for j in range(n-i-1):
            string.append(' ')
        for j in range(n-i-1, n):
            string.append('#')
        print(''.join(string))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
