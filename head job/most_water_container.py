__author__ = 'liyun'


class Solution:
    # @return an integer
    def maxArea(self, height):
        if not height or len(height) == 1:
            return 0
        low = 0
        high = len(height) - 1
        maxArea = 0
        while high > low:
            maxArea = max(maxArea, (high - low) * min(height[high], height[low]))
            if height[high] > height[low]:
                low += 1
            else:
                high -= 1

        return maxArea


if __name__ == '__main__':
    # height = (7, 1, 23, 5, 6, 7, 123, 3, 8, 12, 12, 2)
    height = [1, 2, 4, 3]
    s = Solution()
    print s.maxArea(height)