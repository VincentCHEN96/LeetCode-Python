# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        vales = []

        self.inorderTraversal(vales, root)
        for i in range(len(vales) - 1):
            if vales[i] >= vales[i + 1]:
                return False
        return True

    def inorderTraversal(self, vales: [int], root: TreeNode):
        if root != None:
            self.inorderTraversal(vales, root.left)
            vales.append(root.val)
            self.inorderTraversal(vales, root.right)
