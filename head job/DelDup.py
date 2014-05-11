__author__ = 'rockiee281'
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        #the last remain node
        last = None
        #headnode to return
        new_head = None

        node = head
        need_clean = False
        while node:
            #step 1, if this is the last node
            if not node.next:
                if last:
                    if not need_clean:
                        last.next = node
                else:
                    if not need_clean:
                        new_head = node
                return new_head

            #step 2
            if node.val != node.next.val:
                if need_clean:
                    node = node.next
                    need_clean = False
                    continue
                else:
                    if last:
                        last.next = node
                        last = node
                    else:
                        last = node
                    if not new_head:
                        new_head = node
                    node = node.next
                    continue
            else:
                if last:
                    last.next = None
                node = node.next
                need_clean = True
        return new_head


if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(1)
    #node.next.next = ListNode(2)

    s = Solution()
    node = s.deleteDuplicates(node)
    while node:
        print node.val
        node = node.next