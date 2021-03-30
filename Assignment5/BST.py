class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
       
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # Ref: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/40885162
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def __search(self, value):
        node = self.root
        parent = None
        direction = None
        
        while node:
            if node.value == value:
                break
            elif node.value < value:
                parent = node
                direction = 'right'
                node = node.right
            elif node.value > value:
                parent = node
                direction  = 'left'
                node = node.left

        return parent, node, direction
    # def insert(self, value):
    #     def recursive(node, value):
    #         if node.value>value:
    #             if node.left:
    #                 recursive(node.left, value)
    #             else:
    #                 node.left = Node(value, None, None)
    #         elif node.value<value:
    #             if node.right:
    #                 recursive(node.right, value)
    #             else:
    #                 node.right = Node(value, None, None)
    #         else:
    #             return
    #     if self.root:
    #         recursive(self.root)
    #     else:
    #         self.root = Node(value)
    def insert(self, value):
        parent, node, direction = self.__search(value)

        if self.root is None:
            self.root = Node(value)
            return True

        if node:
            return False
        elif direction == 'left':
            parent.left = Node(value, None, None)
        else:
            parent.right = Node(value, None, None)
        return True
    
        

    # def search(self, value):
    #     def recursive(node, value):
    #         if node is None:
    #             return False
    #         if node.value == value:
    #             return True
    #         elif node.value<value:
    #             return recursive(node.right)
    #         elif node.value>value:
    #             return recursive(node.left)
        
    #     return recursive(self.root, value)
    def search(self, value):
        node, _, _ = self.__search(value)
        return node

    def remove(self, value):
        parent, node, direction = self.__search(value)

        # 해당 value의 노드가 없는 경우
        if node is None:
            return False

        # 1.자식 노드가 없는 경우
        if (node.left is None) and (node.right is None):
            # 1-1. 부모 노드가 없는 경우(root)
            if parent is None:
                self.root = None
            # 1-2. 왼쪽 자식인 경우
            elif direction == 'left':
                parent.left = None
            # 1-3. 오른쪽 자식인 경우
            elif direction == 'right':
                parent.right = None
            else:
                print("1.error")
        # 2-1. 자식이 하나만 있는경우(왼쪽)
        elif node.left and (node.right is None):
            # 2-1-1. 삭제 노드가 부모 노드가 없는 경우(root)
            if parent is None:
                self.root = node.left
            # 2-1-2. 해당 노드가 부모 노드의 왼쪽인 경우
            elif direction == 'left':
                parent.left = node.left
            # 2-1-3. 해당 노드가 부모 노드의 오른쪽인 경우
            elif direction == 'right':
                parent.right = node.left
            else:
                print("2-1.error")
        # 2-2. 자식이 하나만 있는경우(오른쪽)
        elif (node.left is None) and node.right:
            # 2-2-1. 삭제 노드가 부모 노드가 없는 경우(root)
            if parent is None:
                self.root = node.right
            # 2-2-2. 해당 노드가 부모 노드의 왼쪽인 경우
            elif direction == 'left':
                parent.left = node.right
            # 2-2-3. 해당 노드가 부모 노드의 오른쪽인 경우
            elif direction == 'right':
                parent.right = node.right
            else:
                print("2-2.error")
        # 3.두 자식이 모두 있는 경우(왼쪽 서브트리에서 가장 오른쪽 노드로 대체)
        elif node.left and node.right:
            sub_parent = node
            sub_node = node.left
            while sub_node.right:
                sub_parent = sub_node
                sub_node = sub_node.right
            # 대체할 노드의 왼쪽노드가 있는경우
            if sub_node.left:
                sub_parent.left = sub_node.left
            
            # 대체할 노드와 부모사이 관계 끊기
            if sub_parent is not node:
                sub_parent.right = None
            
            # 자리 바꾸기
            if node.left is not sub_node:
                sub_node.left = node.left
            
            sub_node.right = node.right


            # 3-1. 부모 노드가 없는 경우(root)
            if parent is None:
                self.root = sub_node
            elif direction == 'left':
                parent.left = sub_node
            elif direction == 'right':
                parent.right = sub_node
            else:
                print("3.error")
        else:
            print("Remove Error")




