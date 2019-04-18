import sys

def maxProfit(cap, items, index, dic):
	(valor, peso) = items[index-1]

	if (cap, index) in dic:
		return dic[(cap, index)]

	if index == 0 or cap == 0:
		dic[(cap, index)] = 0
		return 0

	if peso > cap:
		dic[(cap,index)] = maxProfit(cap, items, index-1, dic)

	else:
		dic[(cap,index)] = max(maxProfit(cap, items, index-1, dic), valor + maxProfit(cap-peso, items, index-1, dic))

	return dic[(cap,index)]

def main():
	items = []
	cap = int(sys.stdin.readline().rstrip())

	for x in sys.stdin:
		obj, valor, peso = x.rstrip().split()
		items.append((int(valor), int(peso)))
	
	print(maxProfit(cap, items, len(items), {}))

main()