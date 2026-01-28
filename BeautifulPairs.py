#!/bin/python3

import math
import os
import random
import re
import sys


def beautifulPairs(A, B):
    # Write your code here
    A.sort()
    B.sort()
    i = j = 0

    initial_pairs = 0
    n = len(A)

    while i < n and j < n:
        if A[i] == B[j]:
            initial_pairs = initial_pairs + 1
            i = i + 1
            j = j + 1
        elif A[i] < B[j]:
            i = i + 1
        else:
            j = j + 1

    if initial_pairs < n:
        return initial_pairs + 1
    else:
        return initial_pairs - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
