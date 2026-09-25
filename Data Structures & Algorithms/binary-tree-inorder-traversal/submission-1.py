# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        res: list[int] = []
        nodes: list[Optional[TreeNode]] = [root]
        while nodes:
            # Add all left most nodes to list
            while nodes[-1].left:
                nodes.append(nodes[-1].left)
            
            # Remove left most nodes from list that do not have a right node
            while nodes and not nodes[-1].right:
                res.append(nodes.pop().val)
            
            # Remove top node and add right node
            if nodes:
                res.append(nodes[-1].val)
                if nodes[-1].right:
                    nodes.append(nodes.pop().right)
                else:
                    nodes.pop()
        return res