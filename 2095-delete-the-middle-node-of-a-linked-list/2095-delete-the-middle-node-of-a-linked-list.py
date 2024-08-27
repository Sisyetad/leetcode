# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0
        
        while(current):
            count+=1
            current= current.next
        current = head
        if count == 1:
            return None
        for i in range(count//2-1):
            current = current.next
        current.next = current.next.next
        return head
