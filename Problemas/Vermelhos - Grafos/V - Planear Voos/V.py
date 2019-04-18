import sys

""" ---------------------------------------------------------------------------- CONSTRUTOR DA LISTA DE ADJACÊNCIAS --------------------------------------------------------------------- """
def parse(adj):
	for l in sys.stdin:
		o, d, w = l.split()
		if o not in adj:
			adj[o] = []
		if d not in adj:
			adj[d] = []
		adj[o].append((d, int(w)))
		adj[d].append((o, int(w)))

""" ------------------------------------------------------------------------------------- TRAVESSIA ------------------------------------------------------------------------------------- """
def dijkstra(adj,o):
	queue = []
	parent = {}
	dist = {}
	for v in adj:
		dist[v] = float("inf")
		queue.append(v)
	dist[o] = 0
	while queue:
		u = min(queue,key=lambda x : dist[x])
		queue.remove(u)
		for (v,w) in adj[u]:
			alt = dist[u] + w
			if alt < dist[v]:
				dist[v] = alt
				parent[v] = u
	return parent, dist

""" ---------------------------------------------------------------------------------------- MAIN --------------------------------------------------------------------------------------- """
def main():
	origem, destino = sys.stdin.readline().split()
	adj = {}
	parse(adj)
	parent, dist = dijkstra(adj, origem)
	for x in dist:
		if x == destino:
			print(dist[x])

main()