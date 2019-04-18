import sys

def complete(adj,k,c):
    return len(adj) == len(c)

def extensions(adj,k,c):
    i = list(adj.keys())[len(c)]
    cv = [c[x] for x in adj[i] if x in c]
    return [(i,x) for x in range(k) if x not in cv]

def valid(adj,k,c):
    return True

def search(adj,k):
    c = {}
    if aux(adj,k,c):
        return c

def aux(adj,k,c):
    if complete(adj,k,c):
        return valid(adj,k,c)

    for i,x in extensions(adj,k,c):
        c[i] = x
        if aux(adj,k,c):
            return True
        c.pop(i)

    return False

def main():
    dic = {}
    for x in sys.stdin:
        x = x.rstrip().split()
        if x[0] not in dic:
            dic[x[0]] = []
        if x[1] not in dic:
            dic[x[1]] = []
        dic[x[0]].append(x[1])
        dic[x[1]].append(x[0])
    
    d = search(dic, len(dic))
    #print(d)
    print(max(d.values())+1)

main()