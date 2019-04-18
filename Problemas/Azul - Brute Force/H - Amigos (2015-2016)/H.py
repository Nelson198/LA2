import sys
import itertools

def gerador(keys, i):
    return list(itertools.combinations(keys, i))

def search(comb, dic):
	#print("Combinação: " + str(comb))
	for i in range(len(comb)):
		flag = False
		l = list(comb[i])
		#print("Lista: " + str(l))
		for x in l:
			for j in range(len(l)):
				#print("Nome fixo: " + str(x) + "; Nome a ser percorrido: " + str(l[j]))
				if x != l[j] and l[j] in dic[x]:
					flag = True
				elif x != l[j] and l[j] not in dic[x]:
					flag = False
					break
		
			if(flag == False):
				break
		if(flag == True):
			#print("Dicionário: " + str(dic))
			return True

	#print("Dicionário: " + str(dic))
	return False

def main():
	dic = {}
	for nomes in sys.stdin:
		nome1, nome2 = nomes.rstrip().split()
		if nome1 not in dic:
			dic[nome1] = []
		if nome2 not in dic:
			dic[nome2] = []
		dic[nome1].append(nome2)
		dic[nome2].append(nome1)

	for i in range(len(dic.keys()), 2, -1):
		comb = gerador(list(dic.keys()), i)
		boolean = search(comb, dic)
		if(boolean == True):
			print(i)
			return
	print(2)

main()