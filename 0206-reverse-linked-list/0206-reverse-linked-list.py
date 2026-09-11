# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # aage wale ko pehle save karo
            curr.next = prev        # ab current ka next peeche mod do
            prev = curr             # prev aage khisko
            curr = next_node        # curr bhi aage khisko

        return prev 