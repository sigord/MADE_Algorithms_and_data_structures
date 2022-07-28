from __future__ import annotations
import sys
EPS = 1e-5

class point:  
    def __init__(self, x: int = None, y: int = None):
        if x is not None and y is not None:
            self.x = x
            self.y = y
        else:
            self.x = 0
            self.y = 0
    
    def __eq__(self, other: point) -> bool:
        return (self.x == other.x) and (self.y == other.y)
    
    def cheking_is_point_on_segment(self, p1: point, p2: point):
    
        p1p2 = vector(p1, p2)
        p1m = vector(p1, self)
        mp1 = vector(self, p1)
        mp2 = vector(self, p2)
        
        if abs(p1p2.crossProduct(p1m)) < EPS and mp1.dotProduct(mp2) <= 0:
            return True
        else:
            return False
    
class vector:
    def __init__(self, a: point = None, b: point = None, x1: int = None, y1: int = None,\
                 x2: int = None, y2: int = None, X: int = None, Y: int = None):
        if a is not None and b is not None:
            self.x = b.x - a.x
            self.y = b.y - a.y
        elif x1 is not None and x2 is not None and y1 is not None and y2 is not None:
            self.x = x2 - x1
            self.y = y2 - y1
        elif X is not None and Y is not None:
            self.x = X
            self.y = Y
        else:    
            self.x = 0
            self.y = 0
            
    def __eq__(self, other: vector) -> bool:
        return (self.x == other.x) and (self.y == other.y)
    
    def __add__(self, other: vector):
        x = self.x + other.x
        y = self.y + other.y
        return vector(X = x, Y = y)

    def crossProduct(self, b: vector):
        return self.x * b.y - self.y * b.x

    def dotProduct(self, b: vector):
        return self.x * b.x + self.y * b.y

def solve():
    input = sys.stdin.readline
    
    def inlt():
        return(list(map(int, input().split())))

    x1, y1, x2, y2, x3, y3 = inlt()
    
    m = point(x1, y1)
    p1 = point(x2, y2)
    p2 = point(x3, y3)
    
    if m.cheking_is_point_on_segment(p1, p2):
        print("YES")
    else:
        print("NO")
    

if __name__ == "__main__":
    solve()