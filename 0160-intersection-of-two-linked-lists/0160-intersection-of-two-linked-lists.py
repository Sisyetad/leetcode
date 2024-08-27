# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr =headA
        currB = headB
        res = set()
        while curr:
            res.add(curr)
            curr = curr.next
        while currB:
            if currB in res:
                return currB
            currB = currB.next
        return None
