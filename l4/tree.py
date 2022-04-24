# type: ignore
from __future__ import annotations
from typing import Optional
from collections import deque, defaultdict

import binarytree


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    @property
    def height(self):
        if self.left:
            lheight = self.left.height
        else:
            lheight = 0
        if self.right:
            rheight = self.right.height
        else:
            rheight = 0
        return min(lheight, rheight) + 1

    def __repr__(self) -> str:
        return self.val

    def breadth_first(self):
        print(f"\nstarting bfs on root node {self.val}")
        res = []
        queue = deque()

        queue.append(self)

        while queue:
            res.append(queue[0].val)
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        print("breadth first traversal\n", " -> ".join(res))

    def depth_first(self):
        print(f"\nstarting dfs on root node {self.val}")
        ret = []
        stack = deque()
        current = self

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                ret.append(current.val)
                current = current.right
            else:
                break
        print("depth first traversal (inorder)\n", " -> ".join(ret))


def main() -> int:
    tree = Node("1")
    tree.left = Node("2")
    tree.right = Node("3")
    tree.left.left = Node("4")
    tree.left.right = Node("5")
    tree.right.left = Node("6")
    tree.right.right = Node("7")
    tree.right.right.right = Node("8")

    tree.breadth_first()
    tree.depth_first()

    # Użycie wyłącznie klasy Node, nie rozróżniając korzenia jako szczególnego elementu, możemy zacząć poszukiwania
    # od dowolnego elementu w drzewie.

    tree = (
        tree.left
    )  # Zamiast liścia "1", korzeniem będzie element "2" (lewe dziecko poprzedniego korzenia)

    tree.breadth_first()
    tree.depth_first()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
