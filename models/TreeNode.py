from models.Resistor import Resistor


class TreeNode:

    def __init__(self, resistor: Resistor):
        self.left = None
        self.right = None
        self.parent = None
        self.resistor = resistor

    def find_node_to_delete(self, type_to_delete: float):
        if self.resistor.accuracy_in_percentage == type_to_delete:
            return self
        left_result = None
        right_result = None
        if self.left:
            left_result = self.left.find_node_to_delete(type_to_delete)
        if self.right:
            right_result = self.right.find_node_to_delete(type_to_delete)
        return left_result if left_result else right_result

    def find_and_print_node(self, nominal: int):
        if self.left:
            self.left.find_and_print_node(nominal)
        if self.right:
            self.right.find_and_print_node(nominal)
        if self.resistor.nominal == nominal:
            print(self.resistor)

    def print_nodes(self):
        if self.left:
            self.left.print_nodes()
        print(self.resistor)
        if self.right:
            self.right.print_nodes()

