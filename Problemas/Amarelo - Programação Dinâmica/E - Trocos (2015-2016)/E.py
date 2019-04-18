import sys

def trocar(valor, l, i, d):
	if (valor,i) in d:
		return d[(valor,i)]
	
	if valor == 0:
		d[(valor,i)] = 0
		return 0;
	
	if i == 0:
		d[(valor,i)] = float("inf")
		return float("inf")

	r = float("inf")
	if l[i-1] <= valor:
		r = min(r, 1 + trocar(valor-l[i-1], l, i-1, d))

	r = min(r, trocar(valor, l, i-1, d))
	d[(valor,i)] = r
	
	return d[(valor,i)]

def main():
	l = []
	valor = int(sys.stdin.readline().rstrip())
	for x in sys.stdin:
		moeda, quantia = x.rstrip().split()
		moeda = int(moeda)
		quantia = int(quantia)
		for i in range(0, quantia):
			l.append(moeda)

	print(trocar(valor, l, len(l), {}))

main()