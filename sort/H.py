class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __eq__(self, other: "Point") -> bool:
        return self.distance() == other.distance()
    
    def __lt__(self, other: "Point") -> bool:
        return self.distance() < other.distance()
    
    def __gt__(self, other: "Point") -> bool:
        return self.distance() > other.distance()
    
    def __str__(self) -> str:
        return f"{self.x} {self.y}"
    

n = int(input())

points = [Point(*map(int, input().split())) for _ in range(n)]

points.sort()

print(*points, sep="\n")