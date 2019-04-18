import sys

def main():
	adj = {}
	origem, destino = sys.stdin.readline().rstrip().split()
	parse(adj)
	parent, dist = dijkstra(adj, origem)
	for x in dist:
		if x == destino:
			print(dist[x])

def parse(adj):
	for l in sys.stdin:
		l = l.split()

		if len(l) >= 3:
			i = 0
			j = 2
			m = (i+j)//2
			while i <= len(l) and j <= len(l):
				if l[i] not in adj:
					adj[l[i]] = []
				if l[j] not in adj:
					adj[l[j]] = []
				adj[l[i]].append((l[j], int(l[m])))
				adj[l[j]].append((l[i], int(l[m])))
				i += 2
				j += 2
				m = (i+j)//2

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

main()