# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the sorted part's head
        dummy = ListNode(0)
        curr = head
        
        # Iterate through each node in the original list
        while curr:
            # At each step, we'll start inserting the node in the sorted list
            prev = dummy  # Start at the beginning of the sorted list
            next_node = curr.next  # Save the next node to proceed later
            
            # Find the position in the sorted part where curr should be inserted
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # Insert the current node in the sorted list
            curr.next = prev.next
            prev.next = curr
            
            # Move to the next node in the original list
            curr = next_node
        
        # Return the sorted list starting from dummy's next
        return dummy.next