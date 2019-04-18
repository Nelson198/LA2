import sys

def avanca(estado):
	if estado[2] == 1:
		estado[1] += 1
	elif estado[2] == 2:
		estado [0] -= 1
	elif estado[2] == 3:
		estado[1] -= 1
	elif estado[2] == 4:
		estado[0] += 1

def virE(estado):			
	if estado[2] == 4:
		estado[2] = 1
	else:
		estado[2] += 1

def virD(estado):							 
	if estado[2] == 1:
		estado[2] = 4
	else:
		estado[2] -= 1

def main():
	for x in sys.stdin:
		estado = [0,0,1]
		ops = x.strip().split()
		menor_x = menor_y = maior_x = maior_y = 0

		for i in ops:
			if i == "A":
				avanca(estado)
			elif i == "E":
				virE(estado)
			elif i == "D":
				virD(estado)
			else:
				print ("({0},{1}) ({2},{3})".format(menor_x, menor_y, maior_x, maior_y))		
				estado = [0,0,1]
				menor_x = menor_y = maior_x = maior_y = 0

			if estado[0] < menor_x:
				menor_x = estado[0]
			if estado[0] > maior_x:
				maior_x = estado[0]
			if estado[1] < menor_y:
				menor_y = estado[1]
			if estado[1] > maior_y:
				maior_y = estado[1]

main()