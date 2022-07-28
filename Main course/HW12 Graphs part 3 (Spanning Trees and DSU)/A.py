import sys
from sys import setrecursionlimit
import threading
SEPARATOR = "\n"
UNICODE = "utf-8"
MAXPLUS = 400000


############ ---- Main Block ---- ############

def solve():
    
    p = [int()] * MAXPLUS
    max_ = [int()] * MAXPLUS
    min_ = [int()] * MAXPLUS
    size_ = [int()] * MAXPLUS
    result_list = []
    
    def init():

        for i in range(1, n+1):
            p[i] =  i
            size_[i] = 1
            max_[i] = i
            min_[i] = i
    
    def get(x):
        if p[x] != x:
            p[x] = get(p[x])
        return p[x]
        
    
    def union(x, y):
        x = get(x)
        y = get(y)
        
        if x != y:
            if size_[x] < size_[y]:
                x, y = y, x
                
            p[y] = x
            size_[x] = size_[x] + size_[y]
            
            if max_[x] < max_[y]:
                max_[x] = max_[y]
            else:
                max_[y] = max_[x]
            
            if min_[x] > min_[y]:
                min_[x] = min_[y]
            else:
                min_[y] = min_[x]
            
    def get_show(x):
        x = get(x)
        return(str(min_[x]) + " " + str(max_[x]) + " " + str(size_[x]))

        
        
    data = sys.stdin.buffer.readlines()
    n_lines = len(data)
    
    command = str(data[0].decode(UNICODE))[:-1].split()
    n = int(command[0])
    
    init()
    
    for i in range(1, n_lines):
        command = str(data[i].decode(UNICODE))[:-1].split()
        
        if command[0] == "union":
            union(int(command[1]), int(command[2])) 
        elif command[0] == "get":
            result_list.append(str(get_show(int(command[1]))))
    
    encoded_array = (SEPARATOR.join(result_list)).encode(UNICODE)
    sys.stdout.buffer.write(encoded_array)            


if __name__ == "__main__":
    solve()
