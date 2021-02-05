# Complete the countSwaps function below.
def countSwaps(a):
    temp = 0
    swaps = 0
    for j in range(len(a)):
        for i in range((len(a)-j)-1):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                swaps += 1
    return print("Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}".format(swaps,a[0],a[-1]))
