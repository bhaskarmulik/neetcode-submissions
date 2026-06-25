# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #Use a queue for breadth first search
        q = []
        
        curr = root

        while curr:

            print(f"val : {curr.val}")
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            curr.left, curr.right = curr.right, curr.left

            curr = q.pop(0) if q else None
        
        return root
        