#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    n_par = False
    if n%2 == 0:
        n_par = True

    p_par = False
    if p%2 == 0:
        p_par = True

    count_l = 0
    if p_par:
        count_l = p//2
    else:
        count_l = (p-1)//2
    
    count_r = 0
    if n_par:
        if p_par:
            count_r = (n-p)//2
        else:
            count_r = (n-(p-1))//2
    else:
        if p_par:
            count_r = (n-(p+1))//2
        else:
            count_r = (n-p)//2
    
    ans = 0
    if count_r > count_l:
        ans = count_l
    else:
        ans = count_r
    
    return ans
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
