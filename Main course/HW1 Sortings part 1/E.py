VALUE_OF_I = 1
VALUE_OF_V = 5
VALUE_OF_X = 10
VALUE_OF_L = 50

def rom_arab(p):
    z = 0
    try:
        p = str(p)
        for i in range(0, len(p)):
            if p[i] == 'I':
                try:
                    if p[i+1] == 'V' or p[i+1] == 'X':
                        z -= VALUE_OF_I
                    else:
                        z += VALUE_OF_I
                except:
                    z += VALUE_OF_I
            elif p[i] == 'V':
                z += VALUE_OF_V
            elif p[i] == 'X':
                try:
                    if p[i+1] == 'L':
                        z -= VALUE_OF_X
                    else:
                        z += VALUE_OF_X
                except:
                    z += VALUE_OF_X
            elif p[i] == 'L':
                z += VALUE_OF_L
            else:
                print("Invalid number")
    except:
        print("Invalid number")
    return z


inter = int(input())
a = list()
for i in range(inter):
    a.append(tuple(map(str, input().split())))
    arab = rom_arab(a[i][1])
    a[i] = a[i] + (arab,)

res = sorted(a, key=lambda x: (x[0], x[2]))

for i in range(inter):
    print(res[i][0], res[i][1], sep=' ')