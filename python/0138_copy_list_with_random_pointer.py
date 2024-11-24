from typing import Optional
from collections import defaultdict


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        old_new_map = defaultdict(Node)

        old_new_map[head] = Node(head.val)

        trail = head.next

        while trail:
            old_new_map[trail] = Node(trail.val)
            trail = trail.next

        while head:
            if head.next:
                old_new_map[head].next = old_new_map[head.next]
            if head.random:
                old_new_map[head].random = old_new_map[head.random]
            head = head.next

        return old_new_map[head]
