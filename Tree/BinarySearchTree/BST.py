

class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertBST(root,node):
    if root == None:
        return BinarySearchTreeNode(node)
    if node >= root.data:
        root.rightChild = insertBST(root.rightChild, node)
    else:
        root.leftChild = insertBST(root.leftChild, node)

    return root 

def preorderTraversal(root):
    if root is None:
        return 
    
    print(root.data)
    preorderTraversal(root.leftChild)
    preorderTraversal(root.rightChild)
                
def searchBST(root,nodeVal):
    if root is None:
        return "not found"
    else:
        if nodeVal == root.data:
            return "Found"
        elif nodeVal>root.data:
            return searchBST(root.rightChild,nodeVal) 
        else:
            return searchBST(root.leftChild,nodeVal)
    
def minimumValue(bstnode):
    current = bstnode
    while current.leftChild:
        current = current.leftChild
    return current

def deleteNodeBST(root,nodeVal):
    if root is None: # if BST does not exists
        return root
    
    if nodeVal > root.data:
        root.rightChild= deleteNodeBST(root.rightChild,nodeVal)
    elif nodeVal < root.data:
        root.leftChild= deleteNodeBST(root.leftChild,nodeVal)
    else:
        # if nodeVal == root.data 
        # 4 scenarios 
        # if both right and left child present
        if root.leftChild is not None and root.rightChild is not None:
            temp = minimumValue(root.rightChild)
            root.data = temp.data
            # delete minValue 
            root.rightChild= deleteNodeBST(root.rightChild,temp.data)
        # if no child 
        if root.leftChild is None and root.rightChild is None:
            root=None
            return root
        # if right child present
        if root.rightChild is None:
            temp = root.leftChild.data 
            root.data = temp
            root.leftChild = None 
            return root
        if root.leftChild is None:
            temp = root.rightChild.data 
            root.data = temp
            root.rightChild = None 
            return root
        



    
    



newBST = None

newBST = insertBST(newBST, 10)
newBST = insertBST(newBST, 5)
newBST = insertBST(newBST, 15)

preorderTraversal(newBST)
print(searchBST(newBST,35))

print("delete 15")
deleteNodeBST(newBST,15)
preorderTraversal(newBST)

print("delete 10")
deleteNodeBST(newBST,10)
preorderTraversal(newBST)

print("delete 5")
deleteNodeBST(newBST,5)
preorderTraversal(newBST)