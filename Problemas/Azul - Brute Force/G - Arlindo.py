import itertools
import sys
from string import ascii_uppercase

def hashIt(pw):
	return ((ord(pw[0])*(10**6) + ord(pw[1])*(10**4) + ord(pw[2])*(10**2) + ord(pw[3])) % (ord(pw[0])*11 + ord(pw[1])*101 + ord(pw[2])*1009 + ord(pw[3])*10007))


def checkHash(myhash):
	for pw in itertools.product(ascii_uppercase, repeat=4):
		if (int(myhash) == hashIt(pw)):
			return pw
	return "Nao encontrei"

myhash = int(sys.stdin.readline())

print(''.join(checkHash(myhash)))

'''
G : Palavras-Chave

Uma aplicação web usa passwords com 4 caracteres maiúsculos para autenticas os utilizadores. Por questões de segurança, as passwords não são
armazenadas em claro na base de dados, sendo apenas guardado um hash das mesmas. Dada uma password cujos códigos ascii dos 4 caracteres são,
respectivamente, c1, c2, c3, e c4, o hash é calculado da seguinte forma:

(c1*(10**6) + c2*(10**4) + c3*(10**2) + c4) % (c1*11 + c2*101 + c3*1009 + c4*10007)

Um hacker teve acesso à base de dados de password e pretende descobrir qual a password que corresponde a cada hash. Implemente um programa para
ajudar este hacker, ou seja, um programa que dado um hash imprime a respectiva password. Assuma que a cada hash corresponde uma e apenas uma 
password.

Exemplo de entrada:

464132

Saída correspondente:

PASS

'''