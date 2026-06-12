# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #To store nodes in the current generation
        curr_gen = [root] if root else []

        val_gen  = []
        #To store nodes in the next generation
        next_gen = []
        #To store the traversal
        final_arr = []


        #First, we give the limiting condition: 
        while curr_gen or next_gen:

            #For nodes in the current generation
            # for node in curr_gen:

            #     #Append to the next generation
            #     next_gen.append(node.left)
            #     next_gen.append(node.right)

            #     #Make a list of the values in the curr gen
            #     val_gen.append(node.val)

            while curr_gen:

                #Append the node to the next gen
                node = curr_gen.pop(0)
                if node is not None:
                    if node.left is not None:
                        next_gen.append(node.left)
                    if node.right is not None:
                        next_gen.append(node.right)
                    #Make a list of values
                    val_gen.append(node.val)

            
            #Debugging
            #Once all the nodes in the curr_gen have been traversed
            curr_gen = next_gen
            final_arr.append(val_gen)
            next_gen = []
            val_gen = []
        
        return final_arr