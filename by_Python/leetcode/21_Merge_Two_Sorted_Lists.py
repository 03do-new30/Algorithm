# 출처: https://velog.io/@kgh732/Python-%EC%9C%BC%EB%A1%9C-%ED%91%B8%EB%8A%94-Leetcode21.-Merge-Two-Sorted-Lists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # head of the merged linked list
        head = ListNode(-1)
        curr = head
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next, list1 = list1, list1.next
            else:
                curr.next, list2 = list2, list2.next
            
            curr = curr.next
        
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return head.next
        