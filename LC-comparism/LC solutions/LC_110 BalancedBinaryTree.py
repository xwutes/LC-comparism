# LC_110 BalancedBinaryTree
``
def isBalanced(self, root: TreeNode) -> bool:
    return self.helper(root) != -1

def helper(self, root):
    if not root:
        return 0
    left = self.helper(root.left)
    right = self.helper(root.right)
    if left == -1 or right == -1 or abs(left - right) > 1:  # heights diff more than 1, unbalanced
        return -1
    return 1 + max(left, right)         # this line will return tree height