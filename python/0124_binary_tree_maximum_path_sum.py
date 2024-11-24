from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        def output(node: TreeNode, result):
            if not node:
                return 0, result

            left_node_max, left_result = output(node.left, result)
            right_node_max, right_result = output(node.right, result)

            left_node_max = max(left_node_max, 0)
            right_node_max = max(right_node_max, 0)

            return (
                node.val + max(left_node_max, right_node_max),
                max(
                    left_result,
                    right_result,
                    node.val + left_node_max + right_node_max,
                    result,
                ),
            )

        _, max_sum = output(root, result)

        return max_sum
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]


s = Solution()


# tree = TreeNode(-15)
# tree.left = TreeNode(10)
# tree.right = TreeNode(20)
# tree.right.left = TreeNode(15)
# tree.right.left.right = TreeNode(-5)
# tree.right.right = TreeNode(5)

tree = TreeNode(2)
tree.left = TreeNode(-1)


print(s.maxPathSum(tree))
