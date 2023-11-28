class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):

        self.root = Node(root)


#   Root -> Left Subtree -> Right Subtree 
    def preorder(self, start, records):
        if start is not None:
            records.append(start.value) # Root
            records = self.preorder(start.left, records) # Left subtree
            records = self.preorder(start.right, records) # Right subtree

        return records

    
    def postorder(self, start, records):
        if start is not None:
            records = self.postorder(start.left, records) # Left subtree
            records = self.postorder(start.right, records) # Right subtree
            records.append(start.value) # Root
        return records


tree = Tree(5)
tree.root.left = Node(3)
tree.root.right = Node(4)
tree.root.left.left = Node(2)
tree.root.left.right = Node(8)
print(tree.preorder(tree.root, [])) # 5, 3, 2, 8, 4
print(tree.postorder(tree.root, [])) # 2, 8, 3, 4, 5

#        5
#       / \
#      3   4
#     / \   
#    2   8