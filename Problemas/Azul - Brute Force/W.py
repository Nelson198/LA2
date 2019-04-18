import sys

def parse(adj):
    for l in sys.stdin:
        o,d = l.split()
        if o not in adj:
            adj[o] = []
        if d not in adj:
            adj[d] = []
        adj[o].append(d)
        adj[d].append(o)

def extensions(adj,k,c):
    i  = list(adj.keys())[len(c)]
    cv = [c[x] for x in adj[i] if x in c]
    return [(i,x) for x in range(k) if x not in cv]

def search(adj,k):
    c = {}
    l=len(adj)
    if aux(adj,k,c,l):
        return c

def aux(adj,k,c,l):
    if l==len(c):
        return True
    for i,x in extensions(adj,k,c):
        c[i] = x
        if aux(adj,k,c,l):
            return True
        c.pop(i)
    return False

adj = {}
parse(adj)

i = 1
while search(adj,i) == None:
    i+=1

print(i)