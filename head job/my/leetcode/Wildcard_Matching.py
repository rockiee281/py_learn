class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        #For specail cases
        if s is None or p is None:
            return False
        len_s = len(s)
        len_p = len(p)
        if len_s == 0 and len_p == 0:
            return True
        if len_p == 0:
            return False
        if len_s == 0:
            for a in p:
                if a != '*':
                    return False
            return True

        s_i = 0
        p_i = 0
        match_all_flag = False
        while p_i < len_p and s_i < len_s:
            if p[p_i] == '*':
                match_all_flag = True
                p_i += 1
                s_i += 1
            elif p[p_i] == '?':
                p_i += 1
                s_i += 1
            else:
                if s[s_i] != p[p_i]:
                    if not match_all_flag:
                        return False
                    else:
                        s_i += 1
                else:
                    p_i += 1
                    s_i += 1

        # we go through the pattern string, and s is not process over
        if p_i == len_p and s_i < len_s:
            if p[-1] == '*':
                return True
            else:
                return False
        # we go through the s, check if the rest char of P is '*'
        if s_i == len_s:
            if p_i < len_p:
                for char in xrange(p_i, len_p):
                    if p[char] != '*':
                        return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.isMatch('a', 'aa') == False
    print s.isMatch('aa', '*') == True
    print s.isMatch("ab", "?*") == True
    print s.isMatch("b", "*?*?") == False
    print s.isMatch('c', '*?*') == True
