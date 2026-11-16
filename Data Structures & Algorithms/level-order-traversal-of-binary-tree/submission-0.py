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
        result = []
        order = [root]
        while order:
            level = []
            for X in range(len(order)):
                node = order.pop(0)
                level.append(node.val)
                if node.left:
                    order.append(node.left)
                if node.right:
                    order.append(node.right)
            result.append(level)
        return result