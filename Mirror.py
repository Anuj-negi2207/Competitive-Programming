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

def inorder(root):
    if root == None:
        return 
    
    else:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def Mirror(root):
    if root == None:
        return
    else:
        root.left, root.right = root.right, root.left
        Mirror(root.left)
        Mirror(root.right)

if __name__ == "__main__":
    root = tree(50)
    create(root, 45)
    create(root, 55)
    create(root, 100)
    create(root, 65)
    create(root, 30)

print("inorder - ")
inorder(root)

print("after Mirror")
Mirror(root)
inorder(root)
    
