import sys
import itertools

def pick(n, seqs):
    return list(itertools.combinations(seqs, n))

def concat(k):
    res = []
    for x in k:
        res += x
    
    return list(set(res))

seqs = []
maxN = 0
for x in sys.stdin:
    x = list(map(int, x.strip().split()))
    maxN = max(maxN, max(x))
    seqs.append(x)

universo = [x for x in range(1, maxN + 1)]

for x in range(len(seqs) + 1):
    c = pick(x, seqs)
    found = False
    for k in c:
        if sorted(concat(k)) == universo:
            found = True
            print(len(k))
            break
    if found:
        break