import sys

def main():
	for x in sys.stdin:
		print(bin(int(x.strip()))[2:])

main()