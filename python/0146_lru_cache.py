class LRUCache:
    def __init__(self, capacity: int):
        self.store = {}
        self.max_capacity = capacity
        self.key_stack = []

    def get(self, key: int) -> int:
        out = self.store.get(key, -1)
        if out == -1:
            return out
        self.key_stack.remove(key)
        self.key_stack.append(key)
        return out

    def put(self, key: int, value: int) -> None:
        if self.store.get(key) is None:
            self.store[key] = value
            self.key_stack.remove(key)
            self.key_stack.append(key)
            return
        if len(self.key_stack) == self.max_capacity:
            out = self.key_stack.pop(0)
            self.store.pop(out)
        self.store[key] = value
        self.key_stack.append(key)


test_case = [
    "LRUCache",
    [2],
    "put",
    [1, 1],
    "put",
    [2, 2],
    "get",
    [1],
    "put",
    [3, 3],
    "get",
    [2],
    "put",
    [4, 4],
    "get",
    [1],
    "get",
    [3],
    "get",
    [4],
]
# "get",
#     [2],
#     "put",
#     [1, 8],
#     "put",
#     [3, 7],
#     "get",
#     [1],
#     "get",
#     [2],
#     "get",
#     [3],
#     "get",
#     [4],
#     "get",
#     [5],
#     "get",
#     [2],
#     "get",
#     [3],
#     "get",
#     [4],
#     "put",
#     [1, 9],
#     "put",
#     [6, 6],
#     "get",
#     [1],
#     "get",
#     [2],
#     "get",
#     [3],
#     "get",
#     [4],
#     "get",
#     [5],
#     "get",
#     [6],
# ]

func = None
cache = None

for index, val in enumerate(test_case):
    if index == 1:
        cache = LRUCache(*val)
        continue
    if val == "put":
        func = cache.put
    elif val == "get":
        func = cache.get

    if isinstance(val, list):
        print(func(*val))
