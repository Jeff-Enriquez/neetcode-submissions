# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent: Optional[TreeNode] = None
        curr: Optional[TreeNode] = root

        # Find node with the key
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        # Key was not found
        if not curr:
            return root
        
        # Curr node has 0 nodes or 1 child node
        if not curr.left or not curr.right:
            # Child is null or the 1 child node
            child: Optional[TreeNode] = curr.left if curr.left else curr.right
            # Root node has the key, return the child node
            if not parent:
                return child
            # Remove reference of the node with key
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child
            return root

        # Curr node has 2 child nodes
        prev_of_max_node: Optional[TreeNode] = curr
        max_node: Optional[TreeNode] = curr.left
        while max_node.right:
            prev_of_max_node = max_node
            max_node = max_node.right
        
        curr.val = max_node.val
        if curr == prev_of_max_node:
            curr.left = None
        else:
            if max_node.left:
                prev_of_max_node.right = max_node.left
            else:
                prev_of_max_node.right = None

        return root
