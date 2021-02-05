#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    ct = 0
    arr.sort()
    i,j,n = 0,1,len(arr)
    while j < n:
        print(arr[j],arr[i])
        diff = arr[j] - arr[i]
        if diff < k:
            j += 1
        elif diff > k:
            i += 1
        elif diff == k:
            ct += 1
            j += 1
    return ct


    return ct
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
