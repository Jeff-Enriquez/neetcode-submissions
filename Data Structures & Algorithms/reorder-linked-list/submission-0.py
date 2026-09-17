# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head

        # Get the middle of the linked list
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Curr is now at the middle of the array
        # Reverse the second half of the array
        curr: Optional[ListNode] = slow.next
        slow.next = None
        prev: Optional[ListNode] = None
        while curr is not None:
            nxt: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr = prev

        # Knit the two halves together
        first: Optional[ListNode] = head
        second: Optional[ListNode] = curr
        while second:
            nxt1: Optional[ListNode] = first.next
            nxt2: Optional[ListNode] = second.next
            first.next = second
            second.next = nxt1
            second = nxt2
            first = nxt1
