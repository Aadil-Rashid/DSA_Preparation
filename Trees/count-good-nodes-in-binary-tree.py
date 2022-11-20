# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    """
    Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
    Return the number of good nodes in the binary tree.
    """
    
    answer = 0
    
    def cal_goodNodes(self, root, max_val):
        if root is None:
            return
        if root.val >= max_val:
            max_val = root.val
            self.answer += 1
        left_part = self.cal_goodNodes(root.left, max_val)
        right_part = self.cal_goodNodes(root.right, max_val)


    def goodNodes(self, root):
   
        self.cal_goodNodes(root, float('-inf'))
        return self.answer

        """
        :type root: TreeNode
        :rtype: int
        """