# https://leetcode.com/problems/lru-cache/description/
# https://neetcode.io/problems/lru-cache?list=neetcode250

class Node:
    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)    # dummy head and tail
        self.left.next, self.right.prev = self.right, self.left

    def _remove(self, node: Node) -> None:
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv 

    def _add(self, node: Node) -> None:
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]
