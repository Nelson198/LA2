import sys

def main():
	cruzamentos = {}

	for x in sys.stdin:
		l = x.strip()
		first = l[0]
		last = l[-1]

		if first == last and first in cruzamentos:
			cruzamentos[first] += 1
		elif first == last and first not in cruzamentos:
			cruzamentos[first] = 1
		
		elif first != last and first in cruzamentos and last in cruzamentos:
			cruzamentos[first] += 1
			cruzamentos[last] += 1
		elif first != last and first in cruzamentos and last not in cruzamentos:
			cruzamentos[first] += 1
			cruzamentos[last] = 1
		elif first != last and first not in cruzamentos and last not in cruzamentos:
			cruzamentos[first] = 1
			cruzamentos[last] = 1
		else:
			cruzamentos[first] = 1
			cruzamentos[last] += 1

	cruzamentos_ord = sorted(cruzamentos)
	cruzamentos_ord = sorted(cruzamentos_ord, key=lambda x: cruzamentos[x])

	for x in cruzamentos_ord:
		print("{0} {1}".format(x, cruzamentos[x]))

main()