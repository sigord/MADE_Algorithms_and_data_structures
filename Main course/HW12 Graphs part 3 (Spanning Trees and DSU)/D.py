import sys
SEPARATOR = "\n"
UNICODE = "utf-8"

############ ---- Main Block ---- ############

def solve():
    
    def get(x):
        if p[x] != x:
            p[x] = get(p[x])
        return p[x]
    
    def union(x, y):
        x = get(x)
        y = get(y)
        if x != y:
            if size[x] < size[y]:
                x, y = y, x
                    
            p[y] = x
            size[x] = size[x] + size[y]
                
        
    data = sys.stdin.buffer.readlines()
    n_lines = len(data)
    
    unit = str(data[0].decode(UNICODE))[:-1].split()
    n = int(unit[0])
    m = int(unit[1])
    
    graph = [[]] * m
    
    for i in range(1, n_lines):
        unit = str(data[i].decode(UNICODE))[:-1].split()
        
        u = int(unit[0]) - 1
        v = int(unit[1]) - 1
        w = int(unit[2])
        
        graph[i-1] = (u, v, w)
    
    graph = sorted(graph, key=lambda x : x[2])
    
    p = [i for i in range(n)]
    size = [i for i in range(n)]
    
    result = 0
    for i in range(m):
           
        u = graph[i][0]    
        v = graph[i][1]
        w = graph[i][2]
        
        if get(v) != get(u):
            result += w
            union(v, u)        
        
    print(result)
            

if __name__ == "__main__":
    solve()