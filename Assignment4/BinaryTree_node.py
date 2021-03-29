from queue import Queue
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    def preorder(self):
        result = '['
        def recursive(node):
            nonlocal result
            result += str(node.value)
            result += ' '
            if node.left is not None:
                recursive(node.left)
            if node.right is not None:
                recursive(node.right)

        recursive(self.root)
        result += ']'
        print(result)

    
    def inorder(self):
        result = '['
        def recursive(node):
            nonlocal result
            
            if node.left is not None:
                recursive(node.left)
            result += str(node.value)
            result += ' '
            if node.right is not None:
                recursive(node.right)
        recursive(self.root)
        result += ']'
        print(result)
    
    def postorder(self):
        result = '['
        def recursive(node):
            nonlocal result
            
            if node.left is not None:
                recursive(node.left)
            if node.right is not None:
                recursive(node.right)
            result += str(node.value)
            result += ' '
        recursive(self.root)
        result += ']'
        print(result)

    def bfs(self, value):
        que = Queue()
        que.put(self.root)
        while not que.empty():
            node = que.get()
            if node.value == value:
                return True
            if node.left is not None:
                que.put(node.left)
            if node.right is not None:
                que.put(node.right)
        return False
            
    
    def dfs(self, value):
        result = False
        def recursive(node):
            nonlocal result
            if result is True:
                return
            if node.value == value:
                result = True
                return
            if node.left is not None:
                recursive(node.left)
            if node.right is not None:
                recursive(node.right)
        recursive(self.root)
        return result

tree = BinaryTree([i for i in range(13)])
tree.preorder()
tree.inorder()
tree.postorder()

print(tree.dfs(15))
print(tree.dfs(11))

print(tree.bfs(6))
print(tree.bfs(17))   