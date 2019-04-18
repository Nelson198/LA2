import sys

def maxProfit(limite, produtos):
	res = [(0, [])]
	for l in range(1, limite+1):
		maxV = 0
		prodList = []
		for k in produtos:
			valor = produtos[k][0]
			peso = produtos[k][1]
			if peso > l:
				continue

			valor += res[l-peso][0]

			if valor > maxV:
				maxV = valor
				prodList = res[l-peso][1] + [k]
		
		res.append((maxV, prodList))

	print(res[limite][0])

	out = res[limite][1]
	if out:
		out = sorted(out)
		for x in out:
			print(x)

def main():
	limite = int(sys.stdin.readline().rstrip())
	produtos = {}
	for x in sys.stdin:
		x = x.strip().split()
		produtos[x[0]] = (int(x[1]), int(x[2]))

	maxProfit(limite, produtos)
	
main()