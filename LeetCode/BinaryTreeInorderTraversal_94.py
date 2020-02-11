# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        traversal = []
        self.myInorderTraversal(traversal, root)
        return traversal

    def myInorderTraversal(self, traversal: [int], root: TreeNode):
        if root != None:
            self.myInorderTraversal(traversal, root.left)
            traversal.append(root.val)
            self.myInorderTraversal(traversal, root.right)
