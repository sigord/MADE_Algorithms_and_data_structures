import sys
SEPARATOR = "\n"
UNICODE = "utf-8"
MAX = sys.maxsize - 1
NONEEDGE = 100000



def solve():
    
    def findNegativeCycle():
        dist = [MAX] * n
        p = [-1] * n
        dist[0] = 0
        for i in range(n):
            x = -1
            for j in range(len(edges)):
                u = edges[j][0]
                v = edges[j][1]
                w = edges[j][2]
                if (dist[v] > (dist[u] + w)):
                    dist[v] = max(-MAX, (dist[u] + w))
                    p[v] = u
                    x = v
        if (x == -1):
            print("NO")
        else:
            print("YES")
            cycle = []
            y = x
            for i in range(n):
                y = p[y]
            cur = y
            while True:
                cycle.append(cur)
                if (cur == y) and (len(cycle) > 1):
                    break
                cur = p[cur]
            cycle.reverse()
            print(len(cycle) - 1) 
            for i in range(1, len(cycle)):
                print(cycle[i] + 1, end="")
                if i != (len(cycle) - 1):
                    print(" ", end="")
            
            print()
                
    
    data = sys.stdin.buffer.readlines()
    n_lines = len(data)
    
    unit = str(data[0].decode(UNICODE))[:-1].split()
    n = int(unit[0])
    
    edges= []

    
    for i in range(1, n_lines):
        unit = str(data[i].decode(UNICODE))[:-1].split()
        for j in range(n):
            w = int(unit[j])
            if w != NONEEDGE:
                edges.append([(i - 1), j, w])
                
    findNegativeCycle()    
            

if __name__ == "__main__":
    solve()