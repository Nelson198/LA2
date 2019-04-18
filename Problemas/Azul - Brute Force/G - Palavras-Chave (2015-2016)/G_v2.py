from itertools import product
from string import ascii_uppercase
import sys

def hashIt(pw):
	return ((ord(pw[0])*(10**6) + ord(pw[1])*(10**4) + ord(pw[2])*(10**2) + ord(pw[3])) % (ord(pw[0])*11 + ord(pw[1])*101 + ord(pw[2])*1009 + ord(pw[3])*10007))

def checkHash(myhash):
	for pw in product(ascii_uppercase, repeat=4):
		if (int(myhash) == hashIt(pw)):
			return pw
def main():
	myhash = int(sys.stdin.readline())
	print(''.join(checkHash(myhash)))

main()