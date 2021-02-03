#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    d = dict(contests)
    l =  [c[0] for c in contests]
    t =  [c[1] for c in contests]
    imp_ct = sum(t)
    if k>=imp_ct:
        return sum(l)
    else:
        imp_luck_pts = []
        nonimp_luck_pts = []
        for i,tval in enumerate(t):
            if tval == 1:
                imp_luck_pts.append(l[i])
            else:
                nonimp_luck_pts.append(l[i])

        imp_luck_pts.sort(reverse =True)
        total = 0

        for i in range(0,k):
            total  += imp_luck_pts[i]

        total += sum(nonimp_luck_pts)

        for i in range(k,len(imp_luck_pts)):
            total -= imp_luck_pts[i]

        return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
