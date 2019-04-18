import sys

# <------------------------------------ Construtor da lista de adjacências ----------------------------------->
def parse(adj): 
	for x in sys.stdin:
		l = x.split()
		if len(l) == 1:
			adj[l[0]] = []

		else:
			i = 0
			j = 1
			while (i < len(l)) and (j < len(l)):
				if l[i] not in adj:
					adj[l[i]] = []
				if l[j] not in adj:
					adj[l[j]] = []
				adj[l[i]].append(l[j])
				adj[l[j]].append(l[i])
				i += 1
				j += 1
			if l[-1] not in adj[l[0]]:
				adj[l[0]].append(l[-1])
			if l[0] not in adj[l[-1]]:	
				adj[l[-1]].append(l[0])

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
	array = []
	parse(adj)
	for x in adj:
		array.append(len(dfs(adj, x)) + 1)

	if(array == []):
		print(0)
	else:
		print(max(array))

main()