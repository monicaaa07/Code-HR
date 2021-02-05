
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
