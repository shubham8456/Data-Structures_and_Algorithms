# Problem 7 at:
# https://algocademy.com/blog/10-best-coding-exercises-for-mastering-recursion-from-beginner-to-advanced/

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=' ')

# Test the functions
root = TreeNode(1)

root.left  = TreeNode(2)
root.right = TreeNode(3)

root.left.left  = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder traversal:")
inorder_traversal(root)
print("\nPreorder traversal:")
preorder_traversal(root)
print("\nPostorder traversal:")
postorder_traversal(root)
