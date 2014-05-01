__author__ = 'rockiee281'

"""
a[i][j] < a[i+1][j]
a[i][j] < a[i][j+1]

"""
a = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]


def search_val(val):
    """
    @rtype : tuple
    @param val:
    @return: None if not match, index if match
    """
    row = len(a)
    col = len(a[0])
    for i in xrange(row):
        if a[i][col - 1] < val:
            continue
        elif a[i][col - 1] == val:
            return i, col - 1
        else:
            for j in xrange(col - 1, -1, -1):
                if a[i][j] > val:
                    continue
                elif a[i][j] == val:
                    return i, j
                else:
                    break
    return None


for array in a:
    print array
print search_val(7)