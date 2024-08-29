# BINARY TREE TRAVERSAL #

Tree Traversal refers to the process of visiting or accessing each node of the tree exactly once in a certain order. Tree traversal algorithms help us to visit and process all the nodes of the tree.
Since tree is not a linear data structure, there are multiple nodes which we can visit after visiting a certain node. There are multiple tree traversal techniques which decide the order in which the nodes of the tree are to be visited.

A Tree Data Structure can be traversed in following ways:

- Depth First Search or DFS
  - Inorder Traversal: Inorder traversal visits the node in the order: Left -> Node -> Right (Used to get nodes in increasing order)

    ```python
    def in_order_recurssive(node):
        # LNR: Left, Node, Right
        if not node:
            return
        
        in_order_recurssive(node.left)
        print(node.val, end=" ")
        in_order_recurssive(node.right)
        

    def in_order_iterative(node):
        # LNR: Left, Node, Right
        stack = []
        output = []

        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            output.append(node.val)
            node = node.right

        print(output)
    ```

  - Preorder Traversal: Preorder traversal visits the node in the order: Node -> Left -> Right (used to copy nodes)

    ```python
    def pre_order_recursive(node):
        # NLR = Node, Left, Right
        if not node:
            return
        
        # recursive code:
        print(node.val, end=" ")
        pre_order_recursive(node.left)
        pre_order_recursive(node.right)


    def pre_order_iterative(node):
        stack = [node]
        output = []

        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print(output)

    ```

  - Postorder Traversal: Postorder traversal visits the node in the order: Left -> Right -> Node (Used to delete a tree)

  ```python
    def post_order_recursive(node):
        # LRN: Left, Right, Node 
        if not node:
            return  
      
        post_order_recursive(node.left)
        post_order_recursive(node.right)
        print(node.val, end=" ")


    def post_order_iterative(node):
        # LRN: Left, Right, Node        
        stack = [node]
        output = []
        
        while stack:
            node = stack.pop()
            output.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        print(output[::-1])
  ```

- Breadth First Search or BFS
  - Level Order Traversal: visits all nodes present in the same level completely before visiting the next level.

    ```python
    from collections import deque

    def level_order_traversal(node):
        # Nodes at same level stay together.
        q = deque([node])
        output = []

        while q:
            node = q.popleft()
            output.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print(output[::-1])

    ```

## Example Problems ##

- [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
- [Binary Tree paths](https://leetcode.com/problems/binary-tree-paths/)
- [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- [Binary Tree Max Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
