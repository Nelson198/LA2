import sys
import itertools

# ---------------- Gerador de conjuntos ----------------------------------------------------------------------------

def gerador(sets, i):
    return list(itertools.combinations(sets, i))

def concat(k):
    res = []
    for x in k:
        res += x
    return list(set(res))

# ---------------- Resolução com brute force -----------------------------------------------------------------------

# testa se o candidato c está completo
def complete(universo, c):
    if len(c) != len(universo):
        return False
    return True
    
# testa se um candidato c é uma solução válida para p
def valid(universo, c):
    cs = sorted(c)
    for i in range(len(universo)):
        if cs[i] != universo[i]:
            return False
    return True
    
# procurar solução para p com pesquisa exaustiva
def search(universo, sets):
    c = []
    return aux(universo, c, sets)

def aux(universo, c, sets):
    for x in sets:
        c = x
        if complete(universo, c):
            if valid(universo, c):
                return True
    return False

# ---------------- Tratamento do input -----------------------------------------------------------------------------
sets = []
for x in sys.stdin:
    x = list(x.rstrip().split())
    sets.append([int(s) for s in x])

# ---------------- Cálculo do universo -----------------------------------------------------------------------------
universo = []
for s in sets:
    for i in s:
        if i not in universo:
            universo.append(i)

# ---------------- Cálculo do resultado ----------------------------------------------------------------------------
if len(universo) == 0:
    print(0)
else:
    if(search(sorted(universo), sets)):
        print(1)
    for i in range(2, len(sets)+1):
        conjuntos = gerador(sets, i)
        conjunto = []
        for c in conjuntos:
            conjunto.append(concat(c))  
        if sorted(universo) in conjunto:
            print(i)
            break