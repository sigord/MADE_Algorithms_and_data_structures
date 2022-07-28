import sys
SEPARATOR = "\n"
UNICODE = "utf-8"

############ ---- Main Block ---- ############

def solve():

    data = sys.stdin.buffer.readlines()
    n_lines = len(data)
    
    unit = str(data[0].decode(UNICODE))[:-1].split()
    n = int(unit[0])
    m = int(unit[1])
    graph = [set() for _ in range(n)]
    # чтение ребер
    for i in range(1, n_lines):
        unit = str(data[i].decode(UNICODE))[:-1].split()
        
        u = int(unit[0]) - 1
        v = int(unit[1]) - 1
        if u == v:
            continue
        
        graph[u].add(v)
        graph[v].add(u)
        
    for i in range(len(graph)):
        graph[i] = list(graph[i])
    
    visited = [False] * n
    answer = 0
    components = [None] * n
    
    for i in range(n):
        if visited[i]:
            continue
        
        # dfs
        answer += 1
        visited[i] = True
        queue = [i]
        components[i] = answer
        while queue:
            v = queue.pop()
            for to in graph[v]:
                if not visited[to]:
                    visited[to] = True
                    queue.append(to)
                    components[to] = answer
                    
    print(answer)
    print(*components)

if __name__ == "__main__":
    solve()
    
    
########### Second solution ################

import sys
from sys import setrecursionlimit
import threading
SEPARATOR = "\n"
UNICODE = "utf-8"




############ ---- Main Block ---- ############

def solve():


    def dfs(v, comp, ans):
        visited[v] = True
        comp[v] = ans
        for u in graph[v]:
            if not visited[u]:
                dfs(u, comp, ans)
    
    data = sys.stdin.buffer.readlines()
    n_lines = len(data)
    
    unit = str(data[0].decode(UNICODE))[:-1].split()
    n = int(unit[0])
    m = int(unit[1])
    graph = [set() for _ in range(n)]
    # чтение ребер
    for i in range(1, n_lines):
        unit = str(data[i].decode(UNICODE))[:-1].split()
        
        u = int(unit[0]) - 1
        v = int(unit[1]) - 1
        if u == v:
            continue
        
        graph[u].add(v)
        graph[v].add(u)
        
    for i in range(len(graph)):
        graph[i] = list(graph[i])
    
    visited = [False] * n
    answer = 0
    components = [None] * n
    
    for i in range(n):
        if visited[i]:
            continue
        answer += 1
        dfs(i, components, answer)
        
    print(answer)
    print(*components)
        
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26) 
thread = threading.Thread(target=solve)
thread.start()