# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n_1 = ''
        n_2 = ''

        while l1 is not None:
            n_1 += str(l1.val)
            l1 = l1.next
        while l2 is not None:
            n_2 += str(l2.val)
            l2 = l2.next
        
        res = str(int(n_1[::-1]) + int(n_2[::-1]))[::-1]
        head = ListNode(res[0])
        cur_node = head

        for r in res[1:]:
            cur_node.next = ListNode(r)
            cur_node = cur_node.next
        return head
