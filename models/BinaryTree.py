from models.Resistor import Resistor
from models.ResistorsTypes import ResistorsTypes
from models.TreeNode import TreeNode


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, resistor: Resistor):
        if self.root is None:
            self.root = TreeNode(resistor)
            self.root.parent = None
        else:
            current_node = self.root
            while True:
                if resistor.nominal < current_node.resistor.nominal:
                    if current_node.left is None:
                        current_node.left = TreeNode(resistor)
                        current_node.left.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                elif resistor.nominal > current_node.resistor.nominal:
                    if current_node.right is None:
                        current_node.right = TreeNode(resistor)
                        current_node.right.parent = current_node
                        break
                    else:
                        current_node = current_node.right

                else:
                    if resistor.type == ResistorsTypes.MLT.name or \
                            resistor.type == ResistorsTypes.OMLT.name or \
                            resistor.type == ResistorsTypes.C2_10.name:
                        if current_node.left is None:
                            current_node.left = TreeNode(resistor)
                            current_node.left.parent = current_node
                            break
                        else:
                            current_node = current_node.left
                    elif resistor.type == ResistorsTypes.C2_14.name or \
                            resistor.type == ResistorsTypes.C2_29B.name or \
                            resistor.type == ResistorsTypes.C2_33H.name:
                        if current_node.right is None:
                            current_node.right = TreeNode(resistor)
                            current_node.right.parent = current_node
                            break
                        else:
                            current_node = current_node.right
                    else:
                        print("we cant insert resistor of this type")

    def find(self, type_to_delete: float):
        if self.root:
            return self.root.find_node_to_delete(type_to_delete)
        else:
            return None

    def delete_nodes_with_type(self, type_to_delete: float):
        node_to_delete = self.find(type_to_delete)
        if node_to_delete:
            while node_to_delete.parent is None:
                if node_to_delete.left:
                    if node_to_delete.right:
                        self.root = node_to_delete.right
                        self.root.parent = None
                        current_node = node_to_delete.right
                        while current_node.left:
                            current_node = current_node.left
                        current_node.left = node_to_delete.left
                        node_to_delete.left.parent = current_node
                    else:
                        self.root = node_to_delete.left
                        self.root.parent = None
                else:
                    if node_to_delete.right:
                        self.root = node_to_delete.right
                        self.root.parent = None
                    else:
                        self.root = None
                node_to_delete = self.find(type_to_delete)
                if node_to_delete is None:
                    break
        while node_to_delete:
            if node_to_delete == node_to_delete.parent.left:
                if node_to_delete.right:
                    node_to_delete.parent.left = node_to_delete.right  # те місце куди силається наш об єкт для видалення замінити посиланням на обєкт зправа
                    node_to_delete.right.parent = node_to_delete.parent
                    current_node = node_to_delete.right
                    while current_node.left:
                        current_node = current_node.left
                        node_to_delete.left.parent = current_node
                    current_node.left = node_to_delete.left  # найлівіше зправа від видаленої ноди вказуватиме на ліву частину видаленої ноди
                elif node_to_delete.left:
                    node_to_delete.parent.left = node_to_delete.left  # зміна місце ноди на його дитину зліва
                    node_to_delete.left.parent = node_to_delete.parent
                else:
                    node_to_delete.parent.left = None
            else:
                if node_to_delete.right:
                    node_to_delete.parent.right = node_to_delete.right
                    node_to_delete.right.parent = node_to_delete.parent
                    current_node = node_to_delete.right
                    while current_node.left:
                        current_node = current_node.left
                        node_to_delete.left.parent = current_node
                    current_node.left = node_to_delete.left
                elif node_to_delete.left:
                    node_to_delete.parent.right = node_to_delete.left
                    node_to_delete.left.parent = node_to_delete.parent
                else:
                    node_to_delete.parent.right = None
            node_to_delete = self.find(type_to_delete)

    def find_and_print_node_with_nominal(self, nominal: int):
        if self.root:
            self.root.find_and_print_node(nominal)
        else:
            return None

    def print_binary_search_tree(self):
        if self.root:
            self.root.print_nodes()
        else:
            return None
