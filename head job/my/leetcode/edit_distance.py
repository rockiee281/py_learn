__author__ = 'liyun'


class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if cmp(word1, word2) == 0:
            return 0

        len_1 = len(word1)
        len_2 = len(word2)
        if len_1 == 0 or len_2 == 0:
            return max(len_1, len_2)

        max_common = 0
        for i in xrange(len_1):
            cursor_1 = index_1 = i
            index_2 = 0
            cursor_2 = 0
            common = 0
            # print '-------loop %d--------' % i
            while index_1 < len_1:
                if cursor_2 == len_2:
                    cursor_2 = index_2
                    index_1 += 1
                    cursor_1 = index_1
                    continue
                # print word1[cursor_1] + "|" + word2[cursor_2]
                if word1[cursor_1] == word2[cursor_2]:
                    common += 1
                    cursor_1 += 1
                    cursor_2 += 1
                    index_1 = cursor_1
                    index_2 = cursor_2
                else:
                    cursor_2 += 1
            max_common = max(common, max_common)
            # print '-------loop %d end, common is %d,max is %d--------' % (i, common, max_common)
        return len_1 + len_2 - 2 * max_common


if __name__ == '__main__':
    s = Solution()
    print s.minDistance('abc', 'ac') == 1
    print s.minDistance('abc', 'acd') == 2
    print s.minDistance('dddabc', 'sssacd')