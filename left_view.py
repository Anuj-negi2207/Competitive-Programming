class tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    
def create(root, key):
    if root is None:
        return tree(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = create(root.right, key)
        else:
            root.left = create(root.left, key)
    return root

  


def leftView(root, level, depth):
    if root == None:
        return 

    if level > depth:
        print(root.data)
        depth = level
        level += 1

    leftView(root.left, level, depth)  
    leftView(root.right, level, depth)
        

"""

def leftViewUtil(root, level, max_level):
     
    # Base Case
    if root is None:
        return
 
    # If this is the first node of its level
    if (max_level[0] < level):
        print(root.data)
        max_level[0] = level
 
    # Recur for left and right subtree
    leftViewUtil(root.left, level + 1, max_level)
    leftViewUtil(root.right, level + 1, max_level)


 
# A wrapper over leftViewUtil()
def leftView(root):
    max_level = [0]
    leftViewUtil(root, 1, max_level)

"""

if __name__ == "__main__":
    r = tree(50)
    create(r, 55)
    create(r, 45)
    create(r, 100)
    create(r, 60)
    create(r, 36)

    leftView(r, 1, 0)
