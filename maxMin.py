
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
