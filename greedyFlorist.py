#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    no_fl = len(c)
    if k >= no_fl:
        return sum(c)
    else:
        c.sort(reverse = True)
        div = no_fl//k
        total = 0
        for mul in range(div):
            start = mul * k
            end = start+k
            total += ((mul+1) * sum(c[start:end]))

        total +=  (div+1) * sum(c[end:])
        print(total)
        return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
