import sys
from sys import setrecursionlimit
import threading
SEPARATOR = "\n"
UNICODE = "utf-8"
MAX = 1e20


def solve():
    
    def findShortests():
        dist[s] = 0
        for _ in range(n):
            for j_ in range(m):
                u_ = edges[j_][0]
                v_ = edges[j_][1]
                w_ = edges[j_][2]
                if ((dist[u_] < MAX) and (dist[v_] > (dist[u_] + w_))):
                    dist[v_] = max(-MAX, (dist[u_] + w_))
        
    def dfs(v):
        used[v] = True
        for u in graph[v]:
            if not used[u]:
                dfs(u)
    
    data = sys.stdin.buffer.readlines()
    n_lines = len(data)
    
    unit = str(data[0].decode(UNICODE))[:-1].split()
    n = int(unit[0])
    m = int(unit[1])
    s = int(unit[2]) - 1
    
    dist = [MAX] * n
    graph = [set() for _ in range(n)]
    edges = [[]] * m
    
    for i in range(1, n_lines):
        unit = str(data[i].decode(UNICODE))[:-1].split()
        
        u = int(unit[0]) - 1
        v = int(unit[1]) - 1
        w = int(unit[2])
        graph[u].add(v)
        edges[i-1] = (u, v, w)
    
    for i in range(len(graph)):
        graph[i] = list(graph[i])
    
    findShortests()
            
    used = [False] * n
    
    
    for i in range(n):
        for j in range(m):
            u = edges[j][0]
            v = edges[j][1]
            w = edges[j][2]
            if ((dist[u] < MAX) and (dist[v] > (dist[u] + w)) and (not used[v])):
                dfs(v)
                
    for i in range(n):
        if dist[i] == MAX:
            print("*")
        elif used[i]:
            print("-")
        else:
            print(dist[i])
    
    
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=solve)
thread.start()