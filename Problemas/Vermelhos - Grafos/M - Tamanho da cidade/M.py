import sys

""" ---------------------------------------------------------------------------- CONSTRUTOR DA LISTA DE ADJACÊNCIAS --------------------------------------------------------------------- """
def parse(cruzamentos):
	for l in sys.stdin:
		l = l.strip()
		first = l[0]
		last = l[-1] 

		if first not in cruzamentos:
			cruzamentos[first] = {}
		if last not in cruzamentos:
			cruzamentos[last] = {}

		if first != last:
			if first not in cruzamentos[last]:
				cruzamentos[last][first] = []
			if last not in cruzamentos[first]:
				cruzamentos[first][last] = []
			cruzamentos[first][last].append(len(l))
			cruzamentos[last][first].append(len(l))

def minpairs(cruzamentos):
	res = {}
	for x in cruzamentos:
		res[x] = []
		for y in cruzamentos[x]:
			minimo = min(cruzamentos[x][y])
			res[x].append([y, minimo])
	return res

""" ------------------------------------------------------------------------------------- TRAVESSIA ------------------------------------------------------------------------------------- """
def fw(adj):
	dist = {}
	for o in adj:
		dist[o] = {}
		for d in adj:
			if o == d:
				dist[o][d] = 0
			else:
				dist[o][d] = float("inf")
		for (d,w) in adj[o]:
			dist[o][d] = w

	for k in adj:
		for o in adj:
			for d in adj:
				if dist[o][d] > dist[o][k] + dist[k][d]:
					dist[o][d] = dist[o][k] + dist[k][d]
	return dist

""" ---------------------------------------------------------------------------------------- MAIN --------------------------------------------------------------------------------------- """
def main():
	maximo = 0
	cruzamentos = {}

	parse(cruzamentos)
	cruzamentos = minpairs(cruzamentos)

	dist = fw(cruzamentos)

	for x in dist:
		for y in dist[x]:
			maximo = max(maximo, dist[x][y])

	print(maximo)

main()