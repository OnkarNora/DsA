# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Leet code 987 problem link - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
from collections import defaultdict
class Solution(object):
    def verticalTraversal(self, root):
        d = defaultdict(list)
        def solve(root,row,col):
            if not root:
                return 
            d[col].append([root.val,row])
            solve(root.left,row+1,col-1)
            solve(root.right,row+1,col+1)
        solve(root,0,0)
        k = sorted(d.keys())
        result = []
        for i in k:
            temp = sorted(d[i],key=lambda x: (x[1],x[0]))
            result.append([j[0] for j in temp])
        return result
