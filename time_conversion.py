#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def isNoon(s):
    if s[8] == 'P' and s[0:2] != '12':
        return True
    if s[8] == 'A' and s[0:2] == '12':
        return True
    return False

def hrsMinSec(s):
    hs = int(s[0])*10 + int(s[1])
    mn = int(s[3])*10 + int(s[4])
    sc = int(s[6])*10 + int(s[7])

    return [hs, mn, sc]

def intToStr(vec):
    for i in range(len(vec)):
        temp = ''
        if vec[i] < 10:
            temp = '0'
        vec[i] = ''.join([temp, str(vec[i])])
    return vec

def timeConversion(s):
    #
    # Write your code here.
    #
    time = hrsMinSec(s)
    temp = None
    if isNoon(s):
        time[0] = (time[0]+12)%24
    time = intToStr(time)
    ans = ':'.join(time)
    return ans


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
