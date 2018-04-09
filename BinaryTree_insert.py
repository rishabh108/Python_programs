def getHeight(node):
    if node is None:
        return 0
    else:
        max_height = 1 + max(getHeight(node.left), getHeight(node.right))
        return max_height


class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


root = Tree(12)
root.insert(6)
root.insert(14)
root.insert(3)

print(getHeight(root))