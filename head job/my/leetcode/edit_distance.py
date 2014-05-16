__author__ = 'liyun'
import sys

sys.setrecursionlimit(1000000)


class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if cmp(word1, word2) == 0:
            return 0

        len_1 = len(word1)
        len_2 = len(word2)
        if len_1 == 0 or len_2 == 0:
            return max(len_1, len_2)
        cache = {}
        return min_edit_dis(word1, len_1 - 1, word2, len_2 - 1)


cache = {}


def min_edit_dis(w1, index1, w2, index2):
    key = "%d_%d" % (index1, index2)
    if key in cache:
        return cache[key]
    val = 0
    if index1 == 0 or index2 == 0:
        if w1[index1] == w2[index2]:
            val = max(index1, index2)
        else:
            val = max(index1, index2) + 1
    else:
        if w1[index1] == w2[index2]:
            val = min(min_edit_dis(w1, index1 - 1, w2, index2) + 1, min_edit_dis(w1, index1, w2, index2 - 1) + 1,
                      min_edit_dis(w1, index1 - 1, w2, index2 - 1))
        else:
            val = min(min_edit_dis(w1, index1 - 1, w2, index2) + 1, min_edit_dis(w1, index1, w2, index2 - 1) + 1,
                      min_edit_dis(w1, index1 - 1, w2, index2 - 1) + 1)
    cache[key] = val
    print 'the value of %s is %d' % (key, val)
    return val




if __name__ == '__main__':
    s = Solution()
    # print s.minDistance('abc', 'ac') == 1
    # print s.minDistance('abc', 'acd') == 2
    print s.minDistance(
        'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef',
        'bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg')