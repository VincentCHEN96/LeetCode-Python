# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        height_lt = self.heightOfTree(root.left)
        height_rt = self.heightOfTree(root.right)
        if abs(height_lt - height_rt) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def heightOfTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(self.heightOfTree(root.left), self.heightOfTree(root.right)) + 1
