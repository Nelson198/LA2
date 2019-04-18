import sys

def distance(p1, p2):
	return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

# <------------------------------------------- Travessia por níveis ------------------------------------------>
def bfs(o, d, boardSize):
	discovered = []
	queue = []
	discovered.append(o)
	queue.append((o,0))
	while queue:
		p = min(queue, key=lambda x: (distance(x[0], d), x[1]))
		queue.remove(p)
		if p[0] == d:
			return p[1]
		x = p[0][0]
		y = p[0][1]
		dist = p[1]
		if x-2 >= 0 and y+1 < boardSize and (x-2,y+1) not in discovered:
			discovered.append((x-2,y+1))
			queue.append(((x-2,y+1),dist+1))
		if x-1 >= 0 and y+2 < boardSize and (x-1,y+2) not in discovered:
			discovered.append((x-1,y+2))
			queue.append(((x-1,y+2),dist+1))
		if x+1 < boardSize and y+2 < boardSize and (x+1,y+2) not in discovered:
			discovered.append((x+1,y+2))
			queue.append(((x+1,y+2),dist+1))
		if x+2 < boardSize and y+1 < boardSize and (x+2,y+1) not in discovered:
			discovered.append((x+2,y+1))
			queue.append(((x+2,y+1),dist+1))
		if x+2 < boardSize and y-1 >= 0 and (x+2,y-1) not in discovered:
			discovered.append((x+2,y-1))
			queue.append(((x+2,y-1),dist+1))
		if x-1 >= 0 and y-2 >= 0 and (x-1,y-2) not in discovered:
			discovered.append((x-1,y-2))
			queue.append(((x-1,y-2),dist+1))
		if x+1 < boardSize and y-2 >= 0 and (x+1,y-2) not in discovered:
			discovered.append((x+1,y-2))
			queue.append(((x+1,y-2),dist+1))
		if x-2 >= 0 and y-1 >= 0 and (x-2,y-1) not in discovered:
			discovered.append((x-2,y-1))
			queue.append(((x-2,y-1),dist+1))

	return -1

def main():
	boardSize = int(sys.stdin.readline().strip())

	for coords in sys.stdin:
		coords = coords.strip().split()
		coords = list(map(int,coords))
		point0 = (coords[0],coords[1])
		point1 = (coords[2],coords[3])
		if (point0 in [(0,0), (0,boardSize-1), (boardSize-1,0), (boardSize-1,boardSize-1)] or point1 in [(0,0), (0,boardSize-1), (boardSize-1,0), (boardSize-1,boardSize-1)]) and abs(coords[2]-coords[0]) == 1 and abs(coords[3]-coords[1]) == 1:
			print(4)
		else:
			numMovements = bfs(point0, point1, boardSize)
			print(numMovements)

main()