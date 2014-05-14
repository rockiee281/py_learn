__author__ = 'liyun'


class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if not x or x < 0:
            return None

        mid = 0
        left = 0
        right = x
        while right - left > 1:
            mid = left + (right - left) / 2
            val = x / mid
            if mid == val:
                return mid
            elif mid > val:
                right = mid
            else:
                left = mid
        return left


if __name__ == '__main__':
    s = Solution()
    print s.sqrt(3)