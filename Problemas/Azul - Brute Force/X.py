import sys

def complete(u,c,k,s):
    return len(s) == k

def extensions(u,c,k,s):
    return list(x for x in range(0,len(c)) if x not in s)

def valid(u,c,k,s):
    r = set()
    for i in s:
        r.update(c[i])
    return r == u

def search(u,c,k):
    s = []
    if aux(u,c,k,s):
        return c

def aux(u,c,k,s):
    if complete(u,c,k,s):
        return valid(u,c,k,s)
    for x in extensions(u,c,k,s):
        s.append(x)
        if aux(u,c,k,s):
            return True
        s.pop()
    return False

m = 0
c = []
u = set()

for l in sys.stdin:
    l = set(map(int, l.split()))
    c.append(l)
    for i in l:
        if i > m:
            m = i

u = set(x for x in range(1, m+1))

i = 1
while search(u,c,i) == None:
    i = i+1

print(i)