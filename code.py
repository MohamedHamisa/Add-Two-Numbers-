class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):

        def fn(node): 
            """Return number represented by linked list."""
            ans = 0
            while node:
                ans = 10*ans + node.val
                node = node.next
            return ans 
        
        dummy = node = ListNode()
        for x in str(fn(l1) + fn(l2)): 
            node.next = ListNode(int(x))
            node = node.next
        return dummy.next 









