# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([])
        queue.append(root)
        tmp = deque([])

        while len(queue) > 0:
            size = len(queue)
            ls = []
            while size > 0:
                cur = queue.popleft()
                ls.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                size -= 1
            tmp.appendleft(ls[:])
        res = list(tmp)

        return res
