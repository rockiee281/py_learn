class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        star = False
        index_s = 0
        index_p = 0
        cursor_s = 0
        cursor_p = 0
        len_s = len(s)
        len_p = len(p)
        while cursor_s < len_s:
            #special case for cursor_p move the end of p
            if cursor_p == len_p:
                if not star:
                    return False
                else:
                    index_s += 1
                    cursor_s = index_s
                    cursor_p = index_p
                    continue

            if p[cursor_p] == '*':
                while p[cursor_p] == '*':
                    cursor_p += 1
                    if cursor_p == len_p:
                        return True
                index_s = cursor_s
                index_p = cursor_p
                star = True
                continue
            elif p[cursor_p] == '?':
                cursor_s += 1
                cursor_p += 1
                continue
            else:
                if p[cursor_p] != s[cursor_s]:
                    if not star:
                        return False
                    else:
                        index_s += 1
                        cursor_s = index_s
                        cursor_p = index_p
                        continue
                else:
                    cursor_s += 1
                    cursor_p += 1
                    continue

        #check the rest char of p
        for index in xrange(cursor_p, len_p):
            if p[index] != '*':
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print s.isMatch('a', 'aa') == False
    print s.isMatch('aa', '*') == True
    print s.isMatch("ab", "?*") == True
    print s.isMatch("b", "*?*?") == False
    print s.isMatch('c', '*?*') == True
    print s.isMatch('aa', 'a') == False

