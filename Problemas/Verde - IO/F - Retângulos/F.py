import sys

def check(coords):
	maxX = 0
	maxY = 0
	for coord in coords:
		if coord[2] > maxX:
			maxX = coord[2]
		if coord[3] > maxY:
			maxY = coord[3]
	return([maxX, maxY])

def initBoard(coords):
	board = []
	maxX = coords[0]
	maxY = coords[1]
	for y in range(maxY + 1):
		board.append(" " * (maxX+1))
	for i in range(len(board)):
		board[i] = list(board[i])
	return(board)

def updateBoard(board, coordenadas):
	for lista in coordenadas:
		preencher(lista, board)

def preencher(lista, board):
	firstX = lista[0]
	firstY = lista[1]
	secondX = lista[2]
	secondY = lista[3]
	for y in range(firstY, secondY + 1):
		for x in range(firstX, secondX + 1):
			board[y][x] = '#'

def printBoard(board):
	for i in range(len(board)):
		"".join(board[i])
		print("".join(board[i]))

def main():
	coordenadas = []
	for valores in sys.stdin:
		extremos = [int(s) for s in valores.split()]
		coordenadas.append(extremos)
	if len(coordenadas) != 0:
		coords_MAX = check(coordenadas)
		board = initBoard(coords_MAX)
		updateBoard(board, coordenadas)
		printBoard(board)

main()