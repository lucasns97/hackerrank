#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def nextMultiple5(num):
    ans = num
    while ans%5 != 0:
        ans += 1
    return ans

def gradingStudents(grades):
    ans = []
    n = len(grades)
    for i in range(n):
        grade = grades[i]
        if grades[i] < 38:
            ans.append(grade)
        else:
            m5 = nextMultiple5(grade)
            if m5 - grade < 3:
                ans.append(m5)
            else:
                ans.append(grade)
    return ans
    

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
