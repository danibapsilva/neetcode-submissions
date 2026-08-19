class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        last = ""

        mp = self.timeMap[key]
        l, r = 0, len(mp) - 1
        while l <= r:
            middle = l + (r - l) // 2

            if mp[middle][1] > timestamp:
                r = middle - 1
            else:
                l = middle + 1
                last = mp[middle][0]
        
        return last