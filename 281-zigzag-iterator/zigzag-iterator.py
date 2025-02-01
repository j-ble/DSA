class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.q = collections.deque()
        if v1:
            self.q.append((0, v1))
        if v2:
            self.q.append((0, v2))

    def next(self) -> int:
        idx, vec = self.q.popleft()
        res = vec[idx]
        if idx + 1 < len(vec):
            self.q.append((idx + 1, vec))
        return res
        
    def hasNext(self) -> bool:
        return bool(self.q)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())