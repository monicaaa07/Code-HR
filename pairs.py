
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
