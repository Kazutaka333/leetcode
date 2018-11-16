# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def __init__(self):
        self.table = {}
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        if head not in self.table:
            self.table[head] = RandomListNode(head.label)
            new_head = self.table[head]
            new_head.next = self.copyRandomList(head.next)
            new_head.random = self.copyRandomList(head.random)
            return new_head
        else:
            return self.table[head]
        
