# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = ''
        while head is not None:
            res += str(head.val)
            head = head.next
        mid = len(res)//2
        if len(res) % 2 != 0:
            return res[:mid] == res[:mid:-1]
        else:
            return res[:mid] == res[:mid - 1:-1]
