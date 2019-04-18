import sys

def main():
	for x in sys.stdin:
		print(int(x.strip(), 2))

main()