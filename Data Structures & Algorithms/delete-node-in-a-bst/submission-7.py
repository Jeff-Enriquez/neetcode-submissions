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
        prev_of_min_node: Optional[TreeNode] = curr
        min_node: Optional[TreeNode] = curr.right
        # Traverse both paths at the same time
        while max_node.right and min_node.left:
            prev_of_max_node = max_node
            max_node = max_node.right
            prev_of_min_node = min_node
            min_node = min_node.left
        if not max_node.right:
            # Predecessor (max_node) finished first (or at the same time)
            curr.val = max_node.val
            # Delete max_node, but preserve its left child (it cannot have a right child)
            if curr == prev_of_max_node:
                curr.left = max_node.left
            else:
                prev_of_max_node.right = max_node.left
        else:
            # Successor (min_node) finished first
            curr.val = min_node.val
            # Delete min_node, but preserve its right child (it cannot have a left child)
            if curr == prev_of_min_node:
                curr.right = min_node.right
            else:
                prev_of_min_node.left = min_node.right

        return root
