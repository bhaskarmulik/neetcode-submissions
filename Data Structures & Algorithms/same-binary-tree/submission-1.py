# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def bfs(self, root : Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        q = [root]
        tracking = [root.val]

        while q:

            if root.left:
                q.append(root.left)
                tracking.append(root.left.val)
            else:
                tracking.append(None)
            if root.right:
                q.append(root.right)
                tracking.append(root.right.val)
            else:
                tracking.append(None)
            
            root = q.pop(0)
        
        return tracking
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        l1 = self.bfs(p)
        l2 = self.bfs(q)

        print(f"l1 : {l1}")
        print(f"l2 : {l2}")

        return l1 == l2        