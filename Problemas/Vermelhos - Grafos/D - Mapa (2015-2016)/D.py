import sys

def adjacent(l, c, x, y):
	return( (l+1 == x and c == y) or (l-1 == x and c == y)
			or (l == x and c+1 == y) or (l == x and c-1 == y) )

def dijkstra(adj, o):
	queue = []
	dist = {}
	for v in adj:
		dist[v] = float("inf")
		queue.append(v)
	dist[o] = 0
	while queue:
		u = min(queue, key=lambda x: dist[x])
		queue.remove(u)
		for v in adj[u]:
			alt = dist[u] + 1
			if alt < dist[v]:
				dist[v] = alt
	return dist

adj = {}

i = 0
for line in sys.stdin:
	line = list(map(int, line.strip()))
	j = 0
	if i == 0:
		o = ((0,0), int(line[0]))
	for j in range(len(line)):
		adj[(j,i), line[j]] = []
		j += 1
	i += 1


for x in adj:
	for y in adj:
		if adjacent(x[0][0], x[0][1], y[0][0], y[0][1]) and abs(x[1] - y[1]) <= 1 and y not in adj[x]:
			adj[x].append(y)
			adj[y].append(x)

dist = dijkstra(adj, o)

lastrow = {}
for x in dist:
	if x[0][1] == i - 1 and dist[x] != float("inf"):
		lastrow[x[0]] = dist[x]

if lastrow:
	answer = min(lastrow, key=lambda x: (lastrow[x], -x[0]))
	print(answer[0], lastrow[answer])