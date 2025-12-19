# Basic structure of the Tree is TreeNode
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def preorderTraveral(node):
    """
    Preorder traversal using recursion
    """
    if node is None:
        return
    
    print(node.data)
    preorderTraveral(node.leftChild)
    preorderTraveral(node.rightChild)

def inorderTraversal(node):
    if node is None:
        return 
    
    inorderTraversal(node.leftChild)
    print(node.data)
    inorderTraversal(node.rightChild)

def postorderTraversal(node):
    if node is None:
        return 
    postorderTraversal(node.leftChild)
    postorderTraversal(node.rightChild)
    print(node.data)

def levelorderTraversal(node):
    if node is None:
        return 
    else:
        import collections
        queue = collections.deque()
        queue.append(node) # we insert a node into the queue
        while queue:
            val = queue.popleft()
            print(val.data)
            if val.leftChild is not None:
                queue.append(val.leftChild)
            if val.rightChild is not None:
                queue.append(val.rightChild)

def searchNode(node,nodeVal):
    if node is None:
        return "BT does not exists"
    else:
        import collections
        queue = collections.deque()
        queue.append(node) # we insert a node into the queue
        while queue:
            val = queue.popleft()
            if val.data == nodeVal:
                return True
            if val.leftChild is not None:
                queue.append(val.leftChild)
            if val.rightChild is not None:
                queue.append(val.rightChild)
    return False

def insertNode(node,nodeVal):
    if node is None:
        root = TreeNode(nodeVal)
        return root 
    else:
        import collections
        queue=collections.deque()
        queue.append(node)
        while queue:
            val = queue.popleft()
            if val.leftChild is None:
                val.leftChild = TreeNode(nodeVal)
                return f"{nodeVal} inserted"
            else:
                queue.append(val.leftChild)
            
            if val.rightChild is None:
                val.rightChild=TreeNode(nodeVal)
                return f"{nodeVal} inserted"
            else:
                queue.append(val.rightChild)

def getDeepestNode(root):
    if root is None:
        return 
    else:
        import collections
        queue = collections.deque()
        queue.append(root)
        while queue:
            val = queue.popleft()
            # print(val.data)
            if val.leftChild is not None:
                queue.append(val.leftChild)
            if val.rightChild is not None:
                queue.append(val.rightChild)
        deepestNode=val.data  
    return deepestNode

def deleteDeepestNode(root,deepNode):
    if not root:
        return 
    else:
       if root is None:
        return 
    else:
        import collections
        queue = collections.deque()
        queue.append(root)
        while queue:
            val = queue.popleft()
            if val.data is deepNode:
                val.data=None
                return
            if val.rightChild:
                if val.rightChild is deepNode:
                    root.
            






            


def max_depth(node):
    if node is None:
        return 0
    leftCalc = max_depth(node.leftChild)
    rightCalc = max_depth(node.rightChild)

    return 1+max(leftCalc,rightCalc)



    

root = TreeNode(9)
left = TreeNode(4)
right = TreeNode(10)
left1 = TreeNode(2)

root.leftChild = left
root.rightChild = right
root.leftChild.leftChild = left1

print(root.data)
print(root.leftChild.data)
print(root.rightChild.data)
print("Preorder Traversal")
preorderTraveral(root)

print("Inorder Traversal")
inorderTraversal(root)

print("Postorder Traversal")
postorderTraversal(root)

print("Levelorder Traversal")
levelorderTraversal(root)

print(f"max depth is {max_depth(root)}")

print(searchNode(root,3))

print(insertNode(root,5))

preorderTraveral(root)

print("Delete node")
deepestNode = getDeepestNode(root)
deleteDeepestNode(root,deepestNode)