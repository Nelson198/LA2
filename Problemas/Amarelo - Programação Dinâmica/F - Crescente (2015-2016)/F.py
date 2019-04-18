import sys

def max_longest_Increasing_SubSet(l, nova):
	for i in range(1 , len(l)):
		for j in range(0 , i):
			if l[i] >= l[j] and nova[i] < nova[j]+1:
				nova[i] = nova[j]+1

	return max(nova)

def main():
	l = []
	nova = []
	for x in sys.stdin:
		l.append(int(x.rstrip()))
		nova.append(1)

	print(max_longest_Increasing_SubSet(l, nova))

main()