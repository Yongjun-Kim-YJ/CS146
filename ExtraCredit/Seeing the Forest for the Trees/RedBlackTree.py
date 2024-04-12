class Node:
    def __init__(self, data, color='red'):
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None, color='black')
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL
        
        parent = None
        current = self.root
        
        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right
        
        new_node.parent = parent
        
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        
        new_node.color = 'red'
        self.fix_insert(new_node)
    
    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
        
        self.root.color = 'black'
    
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder_traversal(self, node):
        if node != self.NIL:
            self.inorder_traversal(node.left)
            print(node.data, end=' ')
            self.inorder_traversal(node.right)

    def delete(self, data):
        node_to_delete = self.find_node(self.root, data)
        if node_to_delete == self.NIL:
            return
        
        y_original_color = node_to_delete.color
        x = None

        if node_to_delete.left == self.NIL:
            x = node_to_delete.right
            self.transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.NIL:
            x = node_to_delete.left
            self.transplant(node_to_delete, node_to_delete.left)
        else:
            y = self.minimum(node_to_delete.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node_to_delete:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node_to_delete.right
                y.right.parent = y

            self.transplant(node_to_delete, y)
            y.left = node_to_delete.left
            y.left.parent = y
            y.color = node_to_delete.color

        if y_original_color == 'black':
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    sibling = x.parent.right

                if sibling.left.color == 'black' and sibling.right.color == 'black':
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.right_rotate(sibling)
                        sibling = x.parent.right

                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    sibling.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    sibling = x.parent.left

                if sibling.right.color == 'black' and sibling.left.color == 'black':
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.left_rotate(sibling)
                        sibling = x.parent.left

                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    sibling.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = 'black'

    def find_node(self, current_node, data):
        while current_node != self.NIL and current_node.data != data:
            if data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def display(self, node, indent, last):
        if node != self.NIL:
            print(indent, end='')
            if last:
                print("R----", end='')
                indent += "     "
            else:
                print("L----", end='')
                indent += "|    "
            s_color = "RED" if node.color == 'red' else "BLACK"
            print(f'{node.data}({s_color})')
            self.display(node.left, indent, False)
            self.display(node.right, indent, True)

if __name__ == "__main__":
    rbt = RedBlackTree()
    values_to_insert = [20, 15, 25, 10, 18, 30, 5, 12]
    for value in values_to_insert:
        rbt.insert(value)
    
    print("In-order Traversal of Created Tree:")
    rbt.inorder_traversal(rbt.root)
    print("\n")
    
    print("Deleting node with value 10")
    rbt.delete(10)
    print("In-order Traversal after Deletion:")
    rbt.inorder_traversal(rbt.root)
    print("\n")
    
    print("Tree Structure:")
    rbt.display(rbt.root, "", True)