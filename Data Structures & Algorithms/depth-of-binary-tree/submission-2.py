# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        if root == None:
            return 0
        
        curr = root

        while curr:

            l = r = None
            if curr.left:
                l = self.maxDepth(curr.left)
            if curr.right:
                r = self.maxDepth(curr.right)
            
            if l is None and r is None:
                return 1
            elif l is None:
                return 1 + r
            elif r is None:
                return 1 + l
            else:
                return 1+ max(l,r)