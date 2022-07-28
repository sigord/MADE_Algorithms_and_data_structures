import sys
from sys import setrecursionlimit
import threading
SEPARATOR = "\n"
UNICODE = "utf-8"
SOURCE = 'polycarp'

############ ---- Main Block ---- ############

def solve():
    
    def dfs(v, answer):
        visited[v] = True
        answer += 1
        for u in graph[v]:
            if not visited[u] and u != SOURCE:
                results.append(dfs(u, answer))
        return answer

    data = sys.stdin.buffer.readlines()
    n_lines = len(data)
    
    unit = str(data[0].decode(UNICODE))[:-1].split()
    n = int(unit[0])
    
    graph = dict()
    
    for i in range(1, n_lines):
        unit = str(data[i].decode(UNICODE))[:-1].split()
        
        cur = str(unit[0]).lower()
        prev = str(unit[2]).lower()
        
        if graph.get(cur) is None:
            graph[cur] = set([prev])
        else:
            graph[cur].add(prev)
            
        if graph.get(prev) is None:
            graph[prev] = set([cur])
        else:
            graph[prev].add(cur)
        
    result = 0
    visited = {x: False for x in list(graph.keys())}
    
    results = []
    
    for i in graph.keys():
        if visited[i] or i == SOURCE:
            continue
        answer = 1
        answer = dfs(i, answer)
        result = max(result, answer)
    if len(results) > 0:
        result_ = max(results)
        result = max(result_, result)
    print(result)
    
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)  # better use this constant
thread = threading.Thread(target=solve)
thread.start()