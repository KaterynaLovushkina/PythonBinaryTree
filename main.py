from models import *
from models.BinaryTree import BinarySearchTree
from models.Resistor import Resistor

if __name__ == '__main__':
    Tree1 = BinarySearchTree()
    Tree1.insert(Resistor("MLT", 20, 10, 9))
    Tree1.insert(Resistor("C2_14", 10, 10, 8.8))
    Tree1.insert(Resistor("OMLT", 25, 10, 4.6))
    Tree1.insert(Resistor("C2_14", 10, 10, 4.7))
    Tree1.insert(Resistor("C2_29B", 10, 10, 4))
    Tree1.insert(Resistor("C2_33H", 5, 10, 4))

    #Tree1.find_and_print_node_with_nominal(10)
    print()
    Tree1.print_binary_search_tree()
    Tree1.delete_nodes_with_type(4.7)
    print()
    Tree1.print_binary_search_tree()
