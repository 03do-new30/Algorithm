# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Sol1. 런너 기법 이용
        slow = fast = head
        rev = None # 역순으로 구성한 연결리스트
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        # 홀수일 때 중간 값을 패스하기 위해서
        if fast:
            slow = slow.next
        
        # 팰린드롬 확인
        # 역순으로 구성한 연결리스트 rev와 slow가 확인해야 할 나머지 원소들의 값이 같은지 비교
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        
        # 팰린드롬이라면 rev는 None일 것 -> True
        # 팰린드롬이 아니라면 rev는 None이 아닐 것 -> False
        return not rev
            
            
        # Sol2. 데크 자료형 사용
        """
        q: Deque = collections.deque()
        
        if not head:
            return True
        
        node = head
        while node:
            q.append(node.val)
            node = node.next
        
        while q:
            if q.popleft() != q.pop():
                return False
        return True
        """