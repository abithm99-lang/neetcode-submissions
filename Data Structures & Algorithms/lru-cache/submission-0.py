class DDL:
    def __init__(self,key: int=0, val: int=0, prev: 'DDL'= None , next: 'DDL'= None ):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.head = DDL(-1,-1)
        self.tail = DDL(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head   

    # Helper helper method to remove a node from the linked list
    def _remove(self, node: DDL):
        node_prev, node_nxt = node.prev, node.next
        node_prev.next = node_nxt
        node_nxt.prev = node_prev

    # Helper helper method to insert a node right after the head
    def _insert_at_head(self, node: DDL):
        head_nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_nxt
        head_nxt.prev = node     


    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1

        node = self.hm[key]
        self._remove(node)
        self._insert_at_head(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        #check in the hm
        #if key available, replace the value
        #if not, create a new value next to head
        if key in self.hm:
            node = self.hm[key]
            node.val = value
            self._remove(node)
            self._insert_at_head(node)   
        else:
            if len(self.hm) >= self.capacity:
                # The LRU node is right before the tail
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.hm[lru_node.key]

            newNode = DDL(key,value)
            self._insert_at_head(newNode)
            self.hm[key] = newNode
                         
        
