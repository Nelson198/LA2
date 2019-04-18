import sys

# <------------------------------------ Construtor da lista de adjacências ----------------------------------->
def parse(lista, adj):
	maxx = len(lista)
	for x in range(len(lista)):
		for y in range(len(lista[x])):
			if lista[x][y] == ' ':
				adj[(x,y)] = []

				if x-1 >= 0 and lista[x-1][y] == ' ':
					adj[(x,y)].append((x-1, y))
				if x+1 < maxx and lista[x+1][y] == ' ':
					adj[(x,y)].append((x+1, y))
				if y-1 >= 0 and lista[x][y-1] == ' ':
					adj[(x,y)].append((x, y-1))
				if lista[x][y+1] == ' ':
					adj[(x,y)].append((x, y+1))

# <---------------------------------------- Travessia em Profundidade ---------------------------------------->
def dfs_aux(adj, o, discovered, parent):
	discovered.append(o)
	for d in adj[o]:
		if d not in discovered:
			parent[d] = o
			dfs_aux(adj, d, discovered, parent)
	return parent
	
def dfs(adj, o):
	return dfs_aux(adj, o, [], {})

def main():
	adj = {}
	lista = []
	y, x = map(int, sys.stdin.readline().rstrip().split())
	for l in sys.stdin:
		l = list(l.rstrip())
		lista.append(l)

	parse(lista, adj)
	#print(dfs(adj, (x,y)))
	print(len(dfs(adj, (x,y))) + 1)

main()								