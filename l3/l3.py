from typing import Optional


class LLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Optional[LLNode] = None

    def __repr__(self) -> str:
        return self.data


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None and self.tail is None

    def enqueue(self, el: LLNode) -> None:
        if self.is_empty():
            self.head = self.tail = el
        else:
            prev_head = self.head
            self.head = el
            self.head.next = prev_head

    def dequeue(self) -> Optional[LLNode]:
        if self.is_empty():
            return None
        else:
            prev_head = self.head
            self.head = self.head.next  # type:ignore
            return prev_head


q = LinkedList()

q.enqueue(LLNode("test"))
print(q.head, q.tail)
print(q.dequeue())
print(q.head, q.tail)
