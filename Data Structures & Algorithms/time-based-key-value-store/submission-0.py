class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(set)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        for i in range(timestamp, 0, -1):
            curr = self.timeMap.get((key, i), "")
            if not curr:
                continue
            return curr
        
        return ""
