# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None

        res = []
        queue = deque()
        queue.append(root)
        
        while len(queue) > 0:
            size = len(queue)
            list = []
            while size > 0:
                cur = queue.popleft()
                list.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                size -= 1
            res.append(list[:])

        return res
