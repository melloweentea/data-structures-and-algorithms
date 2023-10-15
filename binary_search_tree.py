class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            # add data in the left subtree
            if self.left:
                #left node has a value, not a leaf node
                self.left.add_child(data)
            else:
                self.left = Node(data)
        else:
            #add data in the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Node(data)

    def in_order_traversal(self):
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #visit base node 
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def build_tree(elements):
        root = Node(elements[0])

        for i in range(1, len(elements)):
            root.add_child(elements[i])
        
        return root