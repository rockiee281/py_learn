__author__ = 'liyun'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        nodelist = []
        node = head
        while node:
            nodelist.append(node)
            node = node.next
        len_l = len(nodelist)
        if n == len_l:
            if n == 1:
                return None
            else:
                return nodelist[1]
        elif n == 1:
            nodelist[-2].next = None
            return nodelist[0]
        else:
            nodelist[len_l - n - 1].next = nodelist[len_l - n + 1]
            return nodelist[0]


if __name__ == '__main__':
    head = None
    pre = None
    l = 4
    n = 2
    for i in xrange(l):
        node = ListNode(i)
        if pre:
            pre.next = node
        else:
            head = node
        pre = node

    s = Solution()
    ret = s.removeNthFromEnd(head, n)
    while ret:
        print ret.val
        ret = ret.next