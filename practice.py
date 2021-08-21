# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    Btree = None
    
    def __init__(self, input_list):
        self.Btree = input_list
    
    def findingGood(self, X, index) -> int:
        to_ret = 1
        if index>0:
            if self.Btree[int((index-1)/2)] > X:
                to_ret = 0
            else:
                self.findingGood(X, int((index-1)/2))
        
        return to_ret
                                 
    def goodNodes(self) -> int:
        count_good = 1
        
        for index in range(1, len(self.Btree)):
            if self.Btree[index] == None:
                continue
            X = self.Btree[index]
            count_good += self.findingGood(X, index)
        
        return count_good
        

temp = [3,1,4,3,None,1,5]

s = Solution(temp)
print(s.goodNodes())    
                