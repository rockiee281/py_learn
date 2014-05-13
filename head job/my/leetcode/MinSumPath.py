__author__ = 'rockiee281'


class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        return minSum(grid, m - 1, n - 1)


cache = {}


def minSum(grid_data, m, n):
    # cache the result
    key = '%d_%d' % (m, n)

    if key in cache:
        return cache[key]
        #print key

    val = 0
    if m == 0 and n == 0:
        val = grid_data[0][0]
    elif m == 0:
        val = minSum(grid_data, m, n - 1) + grid_data[m][n]
    elif n == 0:
        val = minSum(grid_data, m - 1, n) + grid_data[m][n]
    else:
        val = min(minSum(grid_data, m - 1, n), minSum(grid_data, m, n - 1)) + grid_data[m][n]
    cache[key] = val
    return val


if __name__ == '__main__':
    # grid = ((1, 2, 3, 4), (3, 2, 1, 3), (12, 33, 21, 1), (4, 2, 1, 0), (2, 1, 3, 5))
    # grid = [[1]]
    grid = [[1]]
    # print len(grid), len(grid[0])

    s = Solution()
    print s.minPathSum(grid)