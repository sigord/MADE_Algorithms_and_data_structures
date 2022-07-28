import sys
import heapq as hp
SEPARATOR = "\n"
UNICODE = "utf-8"
MAX = sys.maxsize

def solve():

    def dijkstra(graph):
        start = 0
        dist[start] = 0
        used = [False] * n
        path = [None] * n
        queue = []
        hp.heappush(queue, (0, start))
        while len(queue) > 0:
            g, u = hp.heappop(queue)
            for v, w in graph[u]:
                if not used[v]:
                    f = g + w
                    if f < dist[v]:
                        dist[v] = f
                        path[v] = u
                        hp.heappush(queue, (f, v))


    data = sys.stdin.buffer.readlines()
    n_lines = len(data)
    
    unit = str(data[0].decode(UNICODE))[:-1].split()
    n = int(unit[0])
    m = int(unit[1])
    dist = [MAX] * n
    graph = [[] for _ in range(n)]

    # чтение ребер
    for i in range(1, n_lines):
        unit = str(data[i].decode(UNICODE))[:-1].split()
        
        u = int(unit[0]) - 1
        v = int(unit[1]) - 1
        w = int(unit[2])
        
        graph[u].append((v,w))
        graph[v].append((u,w))
       
    dijkstra(graph)
    print(*dist)

if __name__ == "__main__":
    solve()