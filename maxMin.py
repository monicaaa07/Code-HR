#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    print(arr)
    min_diff = arr[-1] - arr[0]
    for i,val in enumerate(arr):
        start = i
        end = i + (k-1)
        if end >= len(arr):
            return min_diff
        if (arr[end] - arr[start]) < min_diff:
            min_diff = arr[end] - arr[start]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
