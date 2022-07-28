import sys
from sys import setrecursionlimit
import threading
SEPARATOR = "\n"
UNICODE = "utf-8"


############ ---- Main Block ---- ############

def solve():

    def dfs(v):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                dfs(u)
                
        answer.append(v)
                
    def dfsforCycle(v):
        color[v] = 1
        
        for u in graph[v]:
            if color[u] == 0:
                if dfsforCycle(u):
                    return True
            elif color[u] == 1:
                return True
        color[v] = 2
        return False
                
    def checkCycle(): 
        hasCycle = False
        for i in range(n):
            hasCycle = dfsforCycle(i)
            if hasCycle:
                answer.clear()
                print(-1)
                break
        return hasCycle
                
    
    def topsort():
        if not checkCycle():
            for i in range(n):
                visited[i] = False

            for i in range(n):
                if not visited[i]:
                    dfs(i)
                    
            answer.reverse()
            for i in range(len(answer)):
                print(answer[i] + 1, end=' ')
                
    data = sys.stdin.buffer.readlines()
    n_lines = len(data)
    
    unit = str(data[0].decode(UNICODE))[:-1].split()
    n = int(unit[0])
    m = int(unit[1])
    graph = [set() for _ in range(n)]
    color = [0 for _ in range(n)]
    visited = [False] * n
    answer = []
    # чтение ребер
    for i in range(1, n_lines):
        unit = str(data[i].decode(UNICODE))[:-1].split()
        
        start = int(unit[0]) - 1
        end = int(unit[1]) - 1
        
        graph[start].add(end)
        
    for i in range(len(graph)):
        graph[i] = list(graph[i])
        
    topsort()
        
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)  # better use this constant
thread = threading.Thread(target=solve)
thread.start()