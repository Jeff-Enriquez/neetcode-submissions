# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """Solution for detecting cycles in a singly-linked list."""

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Check if a linked list contains a cycle.

        Uses Floyd's cycle-finding algorithm (tortoise and hare) with two
        pointers moving at different speeds. If a cycle exists, the fast
        pointer will eventually meet the slow pointer.

        Args:
            head: The head node of the linked list.

        Returns:
            True if the linked list has a cycle, False otherwise.
        """
        if head is None:
            return False
        
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True

        return False
