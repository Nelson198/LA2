import sys

def ssm(l):
	tamanho = len(l)
	ss = []
	atual = []

	for i in range(0, tamanho):
		valor_fixo = l[i]
		atual.append(valor_fixo)

		for j in range(i+1, tamanho):
			if l[j] >= valor_fixo:
				atual.append(l[j])
				valor_fixo = l[j]

		ss.append(atual)
		atual = []

	return ss

def main():
	l = []
	for x in sys.stdin:
		l.append(int(x.rstrip()))

	lista = ssm(l)
	maximo = 0
	for e in lista:
		if len(e) > maximo:
			maximo = len(e)

	print(maximo)

main()