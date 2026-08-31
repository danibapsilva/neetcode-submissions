class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node: Node) -> None:
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt
    
    def remove(self, node: Node) -> None:
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = self.cache[key] = Node(key, value)
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]