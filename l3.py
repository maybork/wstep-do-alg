import random
from typing import Optional


def generate_windows(a: int, b: int, c: int, e: int):
    wins = []
    if sum((a, b, c, e)) != 10:
        raise ValueError
    index = 1
    for a_wins in range(a):
        wins.append([index, "a", 0])
    index += 1
    for b_wins in range(b):
        wins.append([index, "b", 0])
        index += 1
    for c_wins in range(c):
        wins.append([index, "c", 0])
        index += 1
    for e_wins in range(e):
        wins.append([index, "e", 0])
        index += 1
    return wins


wins = generate_windows(1, 2, 3, 4)

wins[0][2] = 1
print(wins)


class LinkedList:
    def __init__(self):
        self.head: Optional[LLNode] = None
        self.tail: Optional[LLNode] = None

    def append(self, el):
        if self.head is None:
            self.head = LLNode(el)
            self.tail = self.head
        elif self.tail is not None:
            new_el = LLNode(el)
            self.tail.next = new_el
            self.tail = new_el

    def pop(self):
        if self.head:
            tmp = self.head
            if len(self) == 1:
                self.tail = None
            self.head = self.head.next
            return tmp

    def __len__(self):
        if self.head is None:
            return 0
        nxt = self.head.next
        n = 1
        while nxt is not None:
            n += 1
            nxt = nxt.next
        return n

    def __repr__(self) -> str:
        if self.head is None:
            return "empty LinkedList"
        res = repr(self.head) + "->"
        l = []
        nxt = self.head.next
        while nxt is not None:
            l.append(repr(nxt))
            nxt = nxt.next
        return res + "->".join(l)


class LLNode:
    def __init__(self, data):
        self.data = data
        self.next: Optional[LLNode] = None

    def __repr__(self):
        return f"{self.data}"


def generate_queue(n=40):
    queue = LinkedList()
    for _ in range(40):
        tasktype = random.choice(("a", "b", "c"))

        if tasktype == "a":
            queue.append(("a", random.randint(1, 4)))
        elif tasktype == "b":
            queue.append(("b", random.randint(5, 8)))
        elif tasktype == "c":
            queue.append(("c", random.randint(9, 12)))
    return queue


q = generate_queue()
# print(q.head)


def check_for_available_windows(wins, tasktype):
    for win in wins:
        if win[1] == tasktype:
            if win[2] == 0:
                return win[0]
    else:
        return 0


q = LinkedList()
q.append("a")
q.append("a")
q.append("a")
q.append("a")

print(q)
