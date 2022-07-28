import sys
MAX_SIZE = 10**6 * 2
A_PAR = 111
P_PAR = 10**9 + 7
SEPARATOR = "\n"
UNICODE = "utf-8"

class HashTable(object):
    """
    Hash table
    Resolving collisions by linear probing
    """
    def __init__(self):

        self.size = MAX_SIZE
        
        self.keys = self.make_array(self.size)
        self.delMark = sys.maxsize


    def make_array(self, size):
        """Return array"""
        return [None] * size

    def hash(self, key):
        return ((A_PAR * key) % P_PAR) % self.size
         
    
    def nextHash(self, oldhash):
        return (oldhash + 1) % self.size
    

    def put(self, key):
        """
        Put item into hash table.
        If it already exists replace value.
        """
        chenged_i = None
        index = self.hash(key)
        while self.keys[index] != None:

            if self.keys[index] == self.delMark:
                chenged_i = index
                self.keys[index] = key

            if self.keys[index] == key:
                if chenged_i != None:
                    self.keys[chenged_i] = self.delMark
                    chenged_i = None
                break

            index = self.nextHash(index)

        if chenged_i == None:
            self.keys[index] = key

        
    def get(self, key):
        """
        Find item by key
        Return key of the item or 
        None if the item wasn't found 
        """
        
        index = self.hash(key)

        while self.keys[index] != None:
            if self.keys[index] == key:
                return "true"
            else:
                index = self.nextHash(index)
        return "false"
    

    def delete(self, key):
        """Delete item by the key"""
        
        index = self.hash(key)
        while self.keys[index] != None:
            if self.keys[index] == key:
                self.keys[index] = self.delMark
                return
            index = self.nextHash(index)
        
############ ---- Main Block ---- ############

def solve():
    set = HashTable()
    data = sys.stdin.buffer.readlines()
    result_exists = []
    n_operations = len(data)
    for i in range(n_operations):
        command = str(data[i].decode(UNICODE))[:-1].split()

        if command[0] == "insert":
            set.put(int(command[1]))
        elif command[0] == "exists":
            result_exists.append(set.get(int(command[1])))
        elif command[0] == "delete":
            set.delete(int(command[1]))

        

    encoded_array = (SEPARATOR.join(result_exists)).encode(UNICODE)
    sys.stdout.buffer.write(encoded_array)


if __name__ == "__main__":
    solve()