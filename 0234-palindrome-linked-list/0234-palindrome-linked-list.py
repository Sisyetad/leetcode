# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half of the linked list
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Compare the first half with the reversed second half
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True
