import sys

def SubsetSum(valor, seq):
	if valor == 0:
		return 1
	if len(seq) == 0:
		return 0
		
	y = 0    
	for i in range(len(seq)):
		y += seq[i]
		if y == valor:
			return 1
		elif y > valor:
			return SubsetSum(valor, seq[1:])

	return 0

def main():
	count = 0
	valor = int(sys.stdin.readline().rstrip())
	for l in sys.stdin:
		l = list(map(int, l.rstrip().split()))
		count += SubsetSum(valor, l)

	print(count)

main()