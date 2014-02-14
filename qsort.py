__author__ = 'lx281'
import random
import sys

length = 300


def main():
    arr = []
    for i in range(length):
        arr.append(random.randint(0, 10000))
    print arr
    sys.setrecursionlimit(100000)
    # qsort_inplace(arr, 0, 29)
    print(qsort(arr))


def qsort_inplace(arr, left, right):
    lp = left
    rp = right - 1
    print arr, left, right
    if lp >= rp:
        return
    key = arr[right]
    while True:
        while(arr[lp] <= key) and (lp < rp):
            lp += 1
        while(arr[rp] >= key) and (lp < rp):
            rp -= 1
        arr[lp], arr[rp] = arr[rp], arr[lp]
        if lp >= rp:
            break
    arr[rp], arr[right] = arr[right], arr[rp]
    if left < lp:
        qsort_inplace(arr, left, lp - 1)
    qsort_inplace(arr, rp, right)


def qsort(arr):
    print arr
    if len(arr) < 2:
        return arr
    left = []
    right = []
    key = arr[0]
    for i in xrange(1, len(arr) - 1):
        if arr[i] <= key:
            left.append(arr[i])
        elif arr[i] > key:
            right.append(arr[i])
    return qsort(left) + [key] + qsort(right)


if __name__ == '__main__':
    main()