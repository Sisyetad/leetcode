# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        curr = head
        # while(curr and curr.next):
        #     if curr.val == curr.next.val:
        #         curr.next = curr.next.next
        #     else:
        #         curr = curr.next
        while (curr and curr.next):
            if curr.val == curr.next.val:
                temp = curr.next.next
                curr.next = None
                curr.next = temp
            else:
                curr = curr.next
        if curr.val == head.val:
            head.next = None
        return head
