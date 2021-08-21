import numpy as np
from numpy.core.numeric import allclose

class Solution:
    dictionary = {}
    def __init__(self, matrix):
        for i in matrix:
            self.dictionary[i[0]] = []
        for i in matrix:
            self.dictionary[i[0]].append((i[1], i[2]))
    
    def print_dict(self):
        print(self.dictionary)

    def path_exist(self, root, final, path, all_path):

        print(root)
        print(path)
        print(all_path)
        print("\n")
        
        np.append(path, root) 
        if root is final:
            np.append(all_path, path)
            return
            
        else:
            short_list = self.dictionary[root]
            for i in range(len(short_list)):
                temp = short_list[i]
                s.path_exist(temp[0], final, path, all_path)
            
                    
 
matrix = [[1, 2, 6,], [2, 3, 7], [2, 4, 9], [1, 4, 18], [3, 4, 8]]
s = Solution(matrix)
s.print_dict()

all_path = np.array([])
path = np.array([])
s.path_exist(1, 4, path, all_path)
print(all_path)
