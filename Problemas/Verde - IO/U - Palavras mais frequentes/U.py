import sys

def main():
	palavras = {}

	for l in sys.stdin:
		a = l.strip().split()
		for x in a:
			if x in palavras:
				palavras[x] += 1
			else:
				palavras[x] = 1

	palavras_ord = sorted(palavras)
	palavras_ord = sorted(palavras_ord, key=lambda x: palavras[x], reverse=True)
	
	for x in palavras_ord:
		print("{0}: {1}".format(x, palavras[x]))

main()