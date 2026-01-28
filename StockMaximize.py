#!/bin/python3

import math
import os
import random
import re
import sys

def stockmax(prices):
    profit = 0
    max_price = 0

    for i in range(len(prices) - 1, -1, -1):
        if prices[i] < max_price:
            profit += (max_price - prices[i])
        if prices[i] >= max_price:
            max_price = prices[i]

    return profit


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
