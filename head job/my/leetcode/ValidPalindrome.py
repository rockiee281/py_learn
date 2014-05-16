__author__ = 'liyun'


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True
        left = 0
        right = len(s) - 1
        while right > left:
            char_l = s[left]
            char_r = s[right]
            if not char_r.isalpha() and not char_r.isalnum():
                right -= 1
                continue
            elif not char_l.isalpha() and not char_l.isalnum():
                left += 1
                continue
            else:
                val = ord(char_l) - ord(char_r)
                if val == 0 or val == 32 or val == -32:
                    right -= 1
                    left += 1
                    continue
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome('A man, a plan, a canal: Panama') == True
    print s.isPalindrome('race a car') == False
    print s.isPalindrome('1a2') == False
    print s.isPalindrome('12a21') == True