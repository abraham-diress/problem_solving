# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        out, stack, cur = [], [], root
        last_visited = None

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack[-1]
            if node.right and node.right != last_visited:
                cur = node.right
            else:
                out.append(stack[-1].val)
                last_visited = stack.pop()
        
        return out