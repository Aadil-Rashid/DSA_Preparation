# Question:
#   Given the root of a binary tree, 
#       determine if it is a valid binary search tree (BST).


class Solution(object):
    # Solution 1: idea here is keep track of previously visited node
    def validateBST(self, root, prev):
        if root is None:
            return True
        left_res = self.validateBST(root.left, prev)

        if prev and (root.val <= prev.val ) :
            return False
            
        prev = root
        right_res = self.validateBST(root.right, prev)

        return left_res and right_res

    # Second 2: Solution where we pass min max for every node 
    def valid_bst_min_max(self, root, min_val, max_val):
        if root is None:
            return True
        left_result = self.valid_bst_min_max(root.left, min_val, root.val)
        if root.val <= min_val or root.val >= max_val:
            return False
        right_result = self.valid_bst_min_max(root.right, root.val, max_val)

        return left_result and right_result


    def isValidBST(self, root):
        prv = None
        # result = self.validateBST(root, prv)
        result = self.valid_bst_min_max(root, float('-inf'), float('inf'))

        return result

        """
        :type root: TreeNode
        :rtype: bool
        """