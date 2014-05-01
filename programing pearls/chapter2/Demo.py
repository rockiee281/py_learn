__author__ = 'rockiee281'


def reverse(array, start, end):
    t = array[end]
    while end > start:
        array[end] = array[start]
