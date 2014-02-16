__author__ = 'rockiee281'
import sys


def calculate(m, n):
    """
    get the greatest common divisor of two positive integer
    """
    if n > m:
        return calculate(n, m)
    r = m % n
    if r == 0:
        return n
    else:
        return calculate(n, r)

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    result = calculate(1024, 48)
    print result

