from __future__ import annotations
from typing import List
import sys
import math
SEPARATOR = "\n"
UNICODE = "utf-8"
EPS = 1e-5
M_PI = math.pi

INF_MAX = 10**6 + 1



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
        
    def is_point_insight_polygon(self, poly: polygon):

        inf_p = point(x = INF_MAX, y = self.y)
        
        n = len(poly.corner_points)
        for i in range(n):
            p1 = poly.corner_points[i]
            p2 = poly.corner_points[((i + 1) % n)]
            
            if p1.y <= p2.y:
                a = p1
                b = p2
            else:
                a = p2
                b = p1
            
            if self.cheking_is_point_on_segment(p1, p2):
                return True
            
            if (self.y > a.y) and (self.y <= b.y) and cheking_segments_intersection(a, b, self, inf_p):
                return True
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
    
    
    def len(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5
            
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
    
    def get_andle(self, b: vector):
        angle = math.atan2(b.y, b.x) - math.atan2(self.y, self.x)
        if angle > M_PI:
            angle -= (2 * M_PI)
        elif angle <= -M_PI:
            angle += (2 * M_PI)
        return angle
        
    
class polygon:
    def __init__(self, corner_points: List[point]):
        self.corner_points = corner_points
    
    def get_perimeter(self):
        perimeter = 0.0
        n = len(self.corner_points)
        for i in range(n - 1):
            perimeter += vector(self.corner_points[i], self.corner_points[i + 1]).len()
        
        perimeter += vector(self.corner_points[n-1], self.corner_points[0]).len()
        return perimeter
    
    def get_triangle_area_with_sign(self):
        n = len(self.corner_points)
        if n != 3:
            raise ValueError('The polygon must have three corner points')
        else:
            v1 = vector(self.corner_points[0], self.corner_points[1])
            v2 = vector(self.corner_points[0], self.corner_points[2])
            return (v1.crossProduct(v2))/2
                
    def get_polygon_area(self):
        n = len(self.corner_points)
        area = 0.0
        for i in range(1, n - 1):
            tr = polygon(corner_points=[self.corner_points[0], self.corner_points[i], self.corner_points[i + 1]])
            area += tr.get_triangle_area_with_sign()
        return abs(area)
        
    def is_polygon_convex(self):
        cp = self.corner_points
        cp.append(self.corner_points[0])
        cp.append(self.corner_points[1])
        poly = polygon(corner_points = cp)
        n = len(poly.corner_points)
        v1 = vector(poly.corner_points[0], poly.corner_points[1])
        v2 = vector(poly.corner_points[1], poly.corner_points[2])
        sign = math.copysign(1.0, v1.crossProduct(v2))
        for i in range(1, n - 1):
            v1 = vector(poly.corner_points[i], poly.corner_points[i + 1])
            v2 = vector(poly.corner_points[i + 1], poly.corner_points[i + 2])
            if math.copysign(1.0, v1.crossProduct(v2)) != sign:
                return False     
        return True
            

def cheking_segments_intersection(p1: point, p2: point, m1: point, m2: point):
    p1p2 = vector(p1, p2)
    p1m1 = vector(p1, m1)
    p1m2 = vector(p1, m2)
    m1m2 = vector(m1, m2)
    m1p1 = vector(m1, p1)
    m1p2 = vector(m1, p2)
    
    if (m1.cheking_is_point_on_segment(p1, p2) or\
        m2.cheking_is_point_on_segment(p1, p2) or\
        p1.cheking_is_point_on_segment(m1, m2) or\
        p2.cheking_is_point_on_segment(m1, m2)):
           return True
        
    if (p1p2.crossProduct(p1m1) * p1p2.crossProduct(p1m2)) < 0 and \
       (m1m2.crossProduct(m1p1) * m1m2.crossProduct(m1p2)) < 0: 
        return True
    else:
        return False
    

    

def solve():
    
    data = sys.stdin.buffer.readlines()
    n_lines = len(data)
    
    command = str(data[0].decode(UNICODE))[:-1].split()
    n = int(command[0])
    px = int(command[1])
    py = int(command[2])
    
    p = point(px, py)
    corner_points = [None] * n
    
    for i in range(1, n_lines):
        command = str(data[i].decode(UNICODE))[:-1].split()
        
        x_i_corner = int(command[0])
        y_i_corner = int(command[1])
        
        corner_points[i-1] = point(x_i_corner, y_i_corner) 
    
    poly = polygon(corner_points)
    
    if p.is_point_insight_polygon(poly):
        print("YES")
    else:
        print("NO")
    
if __name__ == "__main__":
    solve()