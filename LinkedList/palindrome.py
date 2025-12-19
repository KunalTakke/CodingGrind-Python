# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        list_1 = []
        # brute force solution
        current_node = head
        while current_node is not None:
            list_1.append(current_node.val)
            current_node=current_node.next
        list_2 = list_1[::-1]
        
        return list_1 == list_2

sol = Solution()
res = sol.isPalindrome([1,2,2,1])
print(res)