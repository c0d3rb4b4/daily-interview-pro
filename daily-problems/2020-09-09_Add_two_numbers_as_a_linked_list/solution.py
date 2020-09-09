# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        if l1 is None and l2 is None and c != 0:
            return ListNode(c)
        elif l1 is None and l2 is None:
            return None

        sum = 0
        if l1 is None:
            sum = l2.val + c
        elif l2 is None:
            sum = l1.val + c
        else:
            sum = l1.val + l2.val + c
        r = ListNode(sum % 10)
        nextL1 = l1.next if l1 is not None else None
        nextL2 = l2.next if l2 is not None else None
        r.next = self.addTwoNumbers(nextL1, nextL2, sum // 10)
        return r

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8