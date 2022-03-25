a = []

def set_v(a, i, v):
    while len(a) <= i:
        a.append(None)
    a[i] = v

set_v(a, 1, 1)
set_v(a, 2, 3)
set_v(a, 0, 2)

print(a)

aset = set(['123', '456', '789'])
bset = set(['456', '789', '012'])
adb = list(aset - bset)
bda = list(bset - aset)
print(adb)
print(bda)
print(len(aset))