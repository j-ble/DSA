# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iteratively
        prev, curr = None, head

        while curr:
            nxt = curr.next # saves the next node
            curr.next = prev # reverse the pointer
            prev = curr # moving prev node to the curr node
            curr = nxt # moving curr to the the next node
        return prev # returns the head
