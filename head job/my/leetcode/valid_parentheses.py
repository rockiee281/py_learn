__author__ = 'liyun'


class Solution:
    # @return a boolean
    def isValid(self, s):
        if not s:
            return True
        stack = []
        brackets_pair = {'(': ')', '[': ']', '{': '}'}
        right_brackets = (')', '}', ']')
        for i in xrange(len(s)):
            if s[i] in brackets_pair:
                stack.append(brackets_pair[s[i]])
            elif s[i] in right_brackets:
                bracket = stack.pop()
                if bracket != s[i]:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print s.isValid('([)]') == False