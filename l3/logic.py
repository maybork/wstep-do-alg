# type:ignore
from typing import Optional
import random
import operator


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

    def enqueue(self, data) -> None:
        if self.is_empty():
            self.head = self.tail = LLNode(data)
        else:
            prev_tail = self.tail
            self.tail = LLNode(data)
            prev_tail.next = self.tail

    def dequeue(self) -> Optional[LLNode]:
        if self.is_empty():
            return None
        else:
            prev_head = self.head
            self.head = self.head.next
            return prev_head

    def __len__(self):
        if self.head is None:
            return 0
        nxt = self.head.next
        n = 1
        while nxt is not None:
            n += 1
            nxt = nxt.next
        return n


def generate_windows(a: int, b: int, c: int, e: int):
    wins = []
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


def generate_queue(n=300):
    queue = LinkedList()
    for _ in range(n):
        tasktype = random.choice(("a", "b", "c"))

        if tasktype == "a":
            queue.enqueue(("a", random.randint(1, 4)))
        elif tasktype == "b":
            queue.enqueue(("b", random.randint(5, 8)))
        elif tasktype == "c":
            queue.enqueue(("c", random.randint(9, 12)))
    return queue


def generate_sorted_queue(n=300, rev=False):
    queue = []
    for _ in range(n):
        tasktype = random.choice(("a", "b", "c"))
        if tasktype == "a":
            queue.append(("a", random.randint(1, 4)))
        elif tasktype == "b":
            queue.append(("b", random.randint(5, 8)))
        elif tasktype == "c":
            queue.append(("c", random.randint(9, 12)))
    queue.sort(key=operator.itemgetter(1), reverse=rev)
    ret = LinkedList()
    for i in queue:
        ret.enqueue(i)
    return ret


def check_for_available_windows(wins, tasktype=None):
    """
    returns the number of an available window, or 0 if none are found
    """
    available = []
    if tasktype is None:
        for win in wins:
            if win[2] == 0:
                available.append(win[0])
    else:
        for win in wins:
            if win[1] in (tasktype, "e"):
                if win[2] == 0:
                    available.append(win[0])
    return available


def symulacja_urzedu(
    n_clients,
    a_wins,
    b_wins,
    c_wins,
    e_wins,
    sorted_q=False,
    rev=False,
    should_print=False,
):
    if sorted_q:
        taskqueue = generate_sorted_queue(n_clients, rev)
    else:
        taskqueue = generate_queue(n_clients)
    windows = generate_windows(a_wins, b_wins, c_wins, e_wins)
    completions = [0 for _ in windows]
    n_wins = len(windows)

    t = 0
    while True:
        # first, check for any occuring tasks
        for win in windows:
            if win[2] > 0:
                # signifies time spent on tasks
                win[2] -= 1
                if win[2] == 0:
                    completions[win[0] - 1] += 1
                    # one client has been successfully served
        while check_for_available_windows(windows) and len(taskqueue):
            ttype = taskqueue.head.data[0]
            avail = check_for_available_windows(windows, ttype)
            if avail:
                windows[random.choice(avail) - 1][2] = taskqueue.dequeue().data[1]
            else:
                break
        # print(len(taskqueue), len(check_for_available_windows(windows)), n_wins)
        if len(taskqueue) == 0 and len(check_for_available_windows(windows)) == n_wins:
            break
        t += 1
    if should_print:
        print(
            "czas obsługi wszystkich klientów:",
            t,
            "\nklienci obsłużeni przez kolejne okienka:",
            completions,
        )
    return t


# generate_sorted_queue(300)
if __name__ == "__main__":
    symulacja_urzedu(1000, 3, 3, 3, 3, should_print=True)
