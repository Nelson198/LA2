import sys

""" ---------------------------------------------------------------------------- CONSTRUTOR DA LISTA DE ADJACÊNCIAS --------------------------------------------------------------------- """
def parse(lista, dimensao):
	adj = {}
	xmin = ymin = 0
	xmax = ymax = dimensao-1

	for i1 in range(dimensao):
		for i2 in range(dimensao):
			if(lista[i1][i2] == ' ') and (i1, i2) not in adj:
				adj[(i1, i2)] = []
				if ((i1+1) <= xmax) and (lista[i1+1][i2] == ' '):
					adj[(i1, i2)].append((i1+1, i2))

				if ((i1-1) >= xmin) and (lista[i1-1][i2] == ' '):
					adj[(i1, i2)].append((i1-1, i2))

				if ((i2+1) <= ymax) and (lista[i1][i2+1] == ' '):
					adj[(i1, i2)].append((i1, i2+1))

				if ((i2-1) >= ymin) and (lista[i1][i2-1] == ' '):
					adj[(i1, i2)].append((i1, i2-1))

	return adj

""" --------------------------------------------------------------------------------- TRAVESSIA POR NÍVEIS ------------------------------------------------------------------------------ """
def bfs(adj,o):
	parent = {}
	discovered = []
	queue = []
	discovered.append(o)
	queue.append(o)
	while queue:
		c = queue.pop(0)
		for n in adj[c]:
			if n not in discovered:
				discovered.append(n)
				parent[n] = c
				queue.append(n)
	return parent

""" ---------------------------------------------------------------------------------------- MAIN --------------------------------------------------------------------------------------- """
def main():
	dimensao = int(sys.stdin.readline())
	lista = []
	origem = (0,0)
	destino = (dimensao-1, dimensao-1)

	for l in sys.stdin:
		l = list(l)
		if l[-1] == "\n":
			del l[-1]
		if l[-1] == "\r":
			del l[-1]
		lista.append(l)
	
	adj = parse(lista, dimensao)
	parent = bfs(adj, origem)
	
	path = []
	path.append(destino)
	while destino in parent:
		destino = parent[destino]
		path.insert(0,destino)

	print(path)
	print(len(path)-1)

main()