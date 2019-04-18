import sys

def parse(dimensao):
	adj = {}
	for i1 in range(0, dimensao):
		for i2 in range(0, dimensao):
			adj[(i1, i2)] = []

	for i in range(len(adj)):
		c1 = list(adj.keys())[i][0]
		c2 = list(adj.keys())[i][1]
		if (c1-2 < dimensao) and (c1-2 >= 0) and (c2+1 < dimensao) and (c2+1 >= 0):
			adj[(c1,c2)].append((c1-2,c2+1))
		if (c1-2 < dimensao) and (c1-2 >= 0) and (c2-1 < dimensao) and (c2-1 >= 0):
			adj[(c1,c2)].append((c1-2,c2-1))
		if (c1+2 < dimensao) and (c1+2 >= 0) and (c2+1 < dimensao) and (c2+1 >= 0):
			adj[(c1,c2)].append((c1+2,c2+1))
		if (c1+2 < dimensao) and (c1+2 >= 0) and (c2-1 < dimensao) and (c2-1 >= 0):
			adj[(c1,c2)].append((c1+2,c2-1))
		if (c1+1 < dimensao) and (c1+1 >= 0) and (c2+2 < dimensao) and (c2+2 >= 0):
			adj[(c1,c2)].append((c1+1,c2+2))
		if (c1+1 < dimensao) and (c1+1 >= 0) and (c2-2 < dimensao) and (c2-2 >= 0):
			adj[(c1,c2)].append((c1+1,c2-2))
		if (c1-1 < dimensao) and (c1-1 >= 0) and (c2-2 < dimensao) and (c2-2 >= 0):
			adj[(c1,c2)].append((c1-1,c2-2))
		if (c1-1 < dimensao) and (c1-1 >= 0) and (c2+2 < dimensao) and (c2+2 >= 0):
			adj[(c1,c2)].append((c1-1,c2+2))

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
	for x in sys.stdin:
		o1, o2, d1, d2 = x.split()
		origem = (int(o1), int(o2))
		destino = (int(d1), int(d2))

		v = parse(dimensao)
		parent = bfs(v, origem)

		if (origem in [(0,0), (0, dimensao-1), (dimensao-1, 0), (dimensao-1, dimensao-1)] or destino in [(0,0), (0, dimensao-1), (dimensao-1, 0), (dimensao-1, dimensao-1)]) and abs(destino[0]-origem[0]) == 1 and abs(destino[1]-origem[1]) == 1:
			print(4)

		else:
			path = []
			path.append(destino)
			while destino in parent:
				destino = parent[destino]
				path.insert(0,destino)

			print(len(path)-1)


main()