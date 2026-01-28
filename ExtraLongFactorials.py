#!/bin/python3

import math
import os
import random
import re
import sys


def extraLongFactorials(n):
    # Write your code here
    result = 1
    for i in range (2, n+1):
        result = result * i
    print(result)

if __name__ == '__main__':
    n = int(input().strip())
    extraLongFactorials(n)