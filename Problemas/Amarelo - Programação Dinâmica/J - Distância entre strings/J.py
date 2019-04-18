import sys

def aux(a, i, b, j, m):
	if (i,j) in m:
		return m[(i,j)]

	if i == 0:
		m[(i,j)] = j
	
	elif j == 0:
		m[(i,j)] = i

	elif a[i-1] == b[j-1]:
		m[(i,j)] = aux(a, i-1, b, j-1, m)

	else:
		m[(i,j)] = min(1 + aux(a, i, b, j-1, m),
					   1 + aux(a, i-1, b, j, m),
					   1 + aux(a, i-1, b, j-1, m))
	return m[(i,j)]

def main():
	l = []
	for x in sys.stdin:
		l.append(x.rstrip())
		if len(l) == 2:
			prox = l[1]
			print(aux(l[0], len(l[0]), l[1], len(l[1]), {}))
			l = []
			l.append(prox)

main()