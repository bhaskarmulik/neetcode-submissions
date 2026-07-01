# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def valid(left, right, node) -> bool:

            if not node:
                return True

            if node.val > left and node.val < right:
                return valid(left, node.val, node.left) and valid(node.val,right, node.right)
            else:
                return False
        
        return valid(float("-inf"), float("inf"), root)
        