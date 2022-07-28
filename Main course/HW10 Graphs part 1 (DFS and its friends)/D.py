import sys
from sys import setrecursionlimit
import threading
SEPARATOR = "\n"
UNICODE = "utf-8"


############ ---- Main Block ---- ############

def solve():

    
    def reg_dfs(i):
        visited[i] = True
        for u in graph[i]:
            if not visited[u]:
                reg_dfs(u)
        order.append(i)
    
    def tran_dfs(j):
        visited[j] = True
        number[j] = s
        for tu in tgraph[j]:
            if not visited[tu]:
                tran_dfs(tu)
    
    data = sys.stdin.buffer.readlines()
    n_lines = len(data)
    
    unit = str(data[0].decode(UNICODE))[:-1].split()
    n = int(unit[0])
    m = int(unit[1])
    
    graph = [[] for _ in range(n)]
    tgraph = [[] for _ in range(n)]
    number = [None for _ in range(n)]
    order = []
    visited = [False] * n
    edges = set() # set
    
    # чтение ребер
    for i in range(1, n_lines):
        unit = str(data[i].decode(UNICODE))[:-1].split()
        
        start = int(unit[0]) - 1
        end = int(unit[1]) - 1
        
        graph[start].append(end)
        tgraph[end].append(start)
    
    for i in range(n):
        if not visited[i]:
            reg_dfs(i)
    
    visited = [False] * n
    s = 1
    for i in range(n):
        j = order[n - 1 - i]
        if not visited[j]:
            tran_dfs(j)
            s += 1
            
    for i in range(n):
        for el in graph[i]:
            if number[i] != number[el]:
                edges.add(tuple([number[i], number[el]]))
    print(len(edges))
        
    
        
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26) 
thread = threading.Thread(target=solve)
thread.start()