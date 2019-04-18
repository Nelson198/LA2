import sys

def isPrefix(palavra, lista):
	prefix = []
	for p in lista:
		if palavra.startswith(p):
			prefix.append(p)
	
	return prefix

def biggerPhrase(palavra, lista, final_word):
	prefix = isPrefix(palavra, lista)
	
	aux = []
	for p in prefix:
		aux.append(palavra[len(p):])

	if palavra == "" or prefix == []:
		return final_word[:-1]
	
	else:
		result = ""
		for i in range(0, len(prefix)):
			word = biggerPhrase(aux[i], lista, final_word + prefix[i] + " ")
			word_aux = list(word)
			result_aux = list(result)

			for x in word_aux:
				if x == " ":
					word_aux.remove(x)

			for x in result_aux:
				if x == " ":
					result_aux.remove(x)

			if len(word_aux) > len(result_aux):
				result = word
		return result

def main():
	lista = []
	palavra = sys.stdin.readline().rstrip()
	for x in sys.stdin:
		lista.append(x.rstrip())

	print(biggerPhrase(palavra, lista, ""))

main()