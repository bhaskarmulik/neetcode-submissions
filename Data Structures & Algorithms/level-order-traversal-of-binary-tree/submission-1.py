# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = [root]
        fl = [[root.val]]
        tmp = []

        while q:

            curr = q.pop(0)

            if curr.left:
                tmp.append(curr.left)
            if curr.right:
                tmp.append(curr.right)
            
            if not q:
                if tmp:
                    fl.append([n.val for n in tmp])
                    q = tmp
                    tmp = []

        return fl