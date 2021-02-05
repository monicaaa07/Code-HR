#!/bin/python3

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
