import sys

def soma(lista):
	nova = []
	i = 0
	while i < len(lista):
		if i == 0:
			nova.append(lista[i])
			i += 1
		elif nova[i-1] < 0:
			nova.append(lista[i])
			i += 1
		else:
			valor = nova[i-1] + lista[i]
			nova.append(valor)
			i += 1

	return max(nova)

def main():
	lista = sys.stdin.readline().rstrip()
	lista = list(map(int, lista.rstrip().split()))
	print(soma(lista))

main()