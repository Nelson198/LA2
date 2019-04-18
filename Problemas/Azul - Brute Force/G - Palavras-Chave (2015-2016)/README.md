# Descrição do problema G : Palavras-Chave

Uma aplicação web usa passwords com 4 caracteres maiúsculos para autenticas os utilizadores. Por questões de segurança, as passwords não são armazenadas em claro na base de dados, sendo apenas guardado um hash das mesmas. Dada uma password cujos códigos ascii dos 4 caracteres são, respectivamente, c1, c2, c3, e c4, o hash é calculado da seguinte forma:

(c1\*(10\*\*6) + c2\*(10\*\*4) + c3\*(10\*\*2) + c4) % (c1\*11 + c2\*101 + c3\*1009 + c4\*10007)  

Um hacker teve acesso à base de dados de password e pretende descobrir qual a password que corresponde a cada hash. Implemente um programa para ajudar este hacker, ou seja, um programa que dado um hash imprime a respectiva password. Assuma que a cada hash corresponde uma e apenas uma 
password.

**Exemplo de entrada:**  

464132

**Saída correspondente:**

PASS
