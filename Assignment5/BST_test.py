from BST import BinarySearchTree


bst = BinarySearchTree()

import random
x = list(range(20))
random.shuffle(x)
for el in x:
    bst.insert(el)
bst.root.display()

bst.remove(6)
bst.root.display()

bst.remove(10)
bst.root.display()