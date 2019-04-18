import sys

def readInput():
	seq = []
	capacity = int(sys.stdin.readline().strip())
	for line in sys.stdin:
		seq.append(int(line))
	seq = sorted(seq)[::-1]
	return capacity, seq

def main():
	count = 0
	capacity, seq = readInput()
	while seq != []:
		if seq[0] <= capacity:
			res = seq[0]
			seq.remove(seq[0])
			remove = []
			for j in range(len(seq)):
				if res + seq[j] <= capacity:
					res += seq[j]
					remove.append(seq[j])
			count += 1
			for x in remove:
				seq.remove(x)
		else:
			seq.remove(seq[0])
	print(count)

main()