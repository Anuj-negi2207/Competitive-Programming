#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:  
    def fill(self, dict, root):
        if root is None:
            return
        
        dict[root.val] = root.val
        self.fill(dict, root.left)
        self.fill(dict, root.right)
    
    def search(self, dict, root, k):
        if root is None:
            return False
        
        if k - root.val in dict:
            if dict[k - root.val] != root.val:
                return True
        
        flag = self.search(dict, root.left, k) or self.search(dict, root.right, k)
        return flag
    
    def findTarget(self, root, k: int) -> bool:
        dict = {}
        self.fill(dict, root)
        return self.search(dict, root, k)
        
        
        
        
        
            