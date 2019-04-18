import sys

def hash(password):
	c1 = ord(password[0]) 
	c2 = ord(password[1])
	c3 = ord(password[2])
	c4 = ord(password[3])
	return (c1*(10**6) + c2*(10**4) + c3*(10**2) + c4) % (c1*11 + c2*101 + c3*1009 + c4*10007)

def complete(h,c):
	return len(c) == 4

def extensions(h,c):
	return [chr(x) for x in range(ord('A'), ord('Z')+1)]

def valid(h,c):
	return h == hash(c)

def search(h):
	c = []
	if aux(h,c):
		return c

def aux(h,c):
	if complete(h,c):
		return valid(h,c)
	for x in extensions(h,c):
		c.append(x)
		if aux(h,c):
			return True
		c.pop()
	return False

hashed_password = int(sys.stdin.readline())
hacked_password = search(hashed_password)

for char in hacked_password:
	sys.stdout.write(char)

print()