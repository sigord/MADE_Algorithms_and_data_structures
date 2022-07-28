from queue import Queue

def solve():
    
    def bfs(x0, y0):
        
        q = Queue()
        used[x0][y0] = True
        q.put((x0, y0))
        while not q.empty():
            x, y = q.get()
            for i, j in zip(dx, dy):
                next_x = x + i
                next_y = y + j
                if (0 <= next_x < n) and (0 <= next_y < n):
                    if not used[next_x][next_y]:
                        p[next_x][next_y] = (x, y)
                        used[next_x][next_y] = True
                        q.put((next_x, next_y))
                        dist[next_x][next_y] = dist[x][y] + 1
        
    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    
    dist = [[0] * n for _ in range(n)]
    p = [[None] * n for _ in range(n)]
    used = [[False] * n for _ in range(n)]
    dx = [2, 2, 1, -1, -2, -2, -1, 1]
    dy = [1, -1, -2, -2, -1, 1, 2, 2]

    bfs(x1, y1)
    print(dist[x2][y2] + 1)
    x, y = x2, y2
    path = []
    while p[x][y] is not None:
        path.append((x + 1, y + 1))
        x, y = p[x][y]
    path.append((x1 + 1, y1 + 1))
    for x, y in reversed(path):
        print(x, y)



if __name__ == "__main__":
    solve()