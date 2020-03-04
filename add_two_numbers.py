# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        x = self.accumulate(l1)
        y = self.accumulate(l2)
        print(x, y, x + y)
        z = [int(d) for d in str(x + y)]
        print(z)
        return self.listToLinked(z)
        
    def accumulate(self, node):
        numbers = []
        
        while node is not None:
            numbers.append(str(node.val))
            node = node.next
            
        return int(''.join(numbers)[::-1])
    
    def listToLinked(self, l):
        linked = ListNode(l.pop())
        lnext = linked
        
        for n in l[::-1]:
            lnext.next = ListNode(l.pop())
            lnext = lnext.next
        
        return linked