import sys
SEPARATOR = "\n"
UNICODE = "utf-8"
P = 47
M = 10 ** 9

def solve():


    def substring_equality(a, b, c, d):
        return get_hash(a, b) == get_hash(c, d)

    def get_hash(l, r):
        return (hashes[r + 1] - (hashes[l] * pows[r - l + 1]) % M + M) % M 


    data = sys.stdin.buffer.readlines()
    n_lines = len(data)
    
    unit = str(data[0].decode(UNICODE))[:-1].split()
    string = str(unit[0])
    
    unit = str(data[1].decode(UNICODE))[:-1].split()
    n = int(unit[0])

    result_list = []
    hashes = [None] * (len(string) + 1)
    pows = [None] * (len(string) + 1)

    hashes[0] = 0
    pows[0] = 1

    for i in range(len(string)):
        hashes[i + 1] = (hashes[i] * P + ord(string[i])) % M
        pows[i + 1] = (pows[i] * P) % M


    for i in range(2, n_lines):
        unit = str(data[i].decode(UNICODE))[:-1].split()
        a = int(unit[0]) - 1
        b = int(unit[1]) - 1
        c = int(unit[2]) - 1
        d = int(unit[3]) - 1

        if substring_equality(a, b, c, d):
            result_list.append("Yes")
        else:
            result_list.append("No")


    encoded_array = (SEPARATOR.join(result_list)).encode(UNICODE)
    sys.stdout.buffer.write(encoded_array)   
            

if __name__ == "__main__":
    solve()