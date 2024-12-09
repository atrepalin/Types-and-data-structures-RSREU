from random import randint
import queue

import sys
from typing import Generator, TypeVar, Optional, List

T = TypeVar("T")


class Node:
    def __init__(self, key: T):
        self.data: T = key
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class BinarySearchTree:
    def __init__(self, array: List[T] = []):
        self.root: Optional[Node] = None

        for item in array:
            self.insert(item)

    def insert(self, key: T) -> None:
        self.root = self._insert(self.root, key)

    def _insert(self, node: Optional[Node], key: T) -> Node:
        if node is None:
            return Node(key)
        if key < node.data:
            node.left = self._insert(node.left, key)
        elif key > node.data:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key: T) -> bool:
        return self._search(self.root, key)

    def _search(self, node: Optional[Node], key: T) -> bool:
        if node is None:
            return False
        if key == node.data:
            return True
        if key < node.data:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def order_up(self) -> List[T]:
        return list(self._order_up(self.root))

    def _order_up(self, node: Optional[Node]) -> Generator[T, None, None]:  # LNR
        if node is None:
            return []

        yield from self._order_up(node.left)
        yield node.data
        yield from self._order_up(node.right)

    def order_down(self) -> List[T]:
        return list(self._order_down(self.root))

    def _order_down(self, node: Optional[Node]) -> Generator[T, None, None]:  # RNL
        if node is None:
            return []

        yield from self._order_down(node.right)
        yield node.data
        yield from self._order_down(node.left)

    def prefix_order(self) -> List[T]:
        return list(self._prefix_order(self.root))

    def _prefix_order(self, node: Optional[Node]) -> Generator[T, None, None]:  # NLR
        if node is None:
            return []

        yield node.data
        yield from self._prefix_order(node.left)
        yield from self._prefix_order(node.right)

    def postfix_order(self) -> List[T]:
        return list(self._postfix_order(self.root))

    def _postfix_order(self, node: Optional[Node]) -> Generator[T, None, None]:  # LRN
        if node is None:
            return []

        yield from self._postfix_order(node.left)
        yield from self._postfix_order(node.right)
        yield node.data

    def bfs(self) -> Generator[T, None, None]:
        q: queue.Queue[Optional[Node]] = queue.Queue()
        q.put(self.root)

        while not q.empty():
            node = q.get()
            if node is not None:
                yield node.data
                q.put(node.left)
                q.put(node.right)

    def find_max(self) -> T:
        if self.root is None:
            raise ValueError("Tree is empty")
        return self._max_node(self.root).data

    def _max_node(self, node: Node) -> Node:
        current = node
        while current.right is not None:
            current = current.right
        return current

    def size(self) -> int:
        return self._size(self.root)

    def _size(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def delete(self, key: T) -> None:
        self.root = self._delete(self.root, key)

    def _delete(self, node: Optional[Node], key: T) -> Optional[Node]:
        if node is None:
            return node
        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            max_node = self._max_node(node.left)
            node.data = max_node.data
            node.left = self._delete(node.left, max_node.data)
        return node

    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def print_tree(self) -> None:
        self._print_tree(self.root)

    def _print_tree(self, node: Optional[Node], level: int = 0) -> None:
        if node is None:
            return

        self._print_tree(node.left, level + 1)
        print("." * level + str(node.data))
        self._print_tree(node.right, level + 1)


bst = BinarySearchTree()

for cmd in sys.stdin:
    inp = cmd.rstrip("\n")
    cmd = inp.split()

    if cmd[0] == "ADD":
        x = int(cmd[1])

        if bst.search(x):
            print("ALREADY")
        else:
            bst.insert(x)
            print("DONE")
    elif cmd[0] == "DELETE":
        x = int(cmd[1])

        if bst.search(x):
            bst.delete(x)
            print("DONE")
        else:
            print("CANNOT")
    elif cmd[0] == "SEARCH":
        x = int(cmd[1])

        if bst.search(x):
            print("YES")
        else:
            print("NO")
    elif cmd[0] == "PRINTTREE":
        bst.print_tree()
