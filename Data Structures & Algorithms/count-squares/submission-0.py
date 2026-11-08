class CountSquares:

    def __init__(self):
        self.points = []
        self.pointsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pointsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point

        res = 0
        for x, y in self.points:
            if (
                abs(px - x) != abs(py - y) or
                px == x or
                py == y
            ): # opposite diagonal corner doesnt exist
                continue
            
            # the other two corners
            res += self.pointsCount[(x, py)] * self.pointsCount[(px, y)]
        return res
