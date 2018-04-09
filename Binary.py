class Tree:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def getHeight(node):
    if node is None:
        return 0;
    else:
        max_Height =1 + max(getHeight(node.left), getHeight(node.right))
        return max_Height


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.left = Tree(8)
root.right.right = Tree(7)
root.left.left.right = Tree(6)
root.left.left.left = Tree(10)


print("The Maximum depth of the tree is:- ", getHeight(root))
