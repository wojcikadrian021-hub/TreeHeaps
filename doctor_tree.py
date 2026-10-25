class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        found = self.find(node.left, name)
        if found is not None:
            return found
        return self.find(node.right, name)

    def insert(self, parent_name, doctor_name, side):
        if side not in ("left", "right"):
            print("Invalid side. Use 'left' or 'right'.")
            return False

        parent = self.find(self.root, parent_name)
        if parent is None:
            print("Parent doctor not found:", parent_name)
            return False
        if getattr(parent, side) is not None:
            print("That side already has a doctor.")
            return False

        setattr(parent, side, DoctorNode(doctor_name))
        return True

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))

    # Edge cases
    tree.insert("Dr. Missing", "Dr. Test", "left")
    tree.insert("Dr. Croft", "Dr. Test", "middle")
    tree.insert("Dr. Croft", "Dr. Test", "left")
    assert tree.preorder(None) == []
    assert tree.preorder(tree.root) == ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Carson", "Dr. Goldsmith"]
    assert tree.inorder(tree.root) == ["Dr. Morgan", "Dr. Phan", "Dr. Carson", "Dr. Croft", "Dr. Goldsmith"]
    assert tree.postorder(tree.root) == ["Dr. Morgan", "Dr. Carson", "Dr. Phan", "Dr. Goldsmith", "Dr. Croft"]
