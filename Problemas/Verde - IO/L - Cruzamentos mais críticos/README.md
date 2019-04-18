# Descrição do problema L : Cruzamentos mais críticos

Podemos usar um (multi) grafo pesado para representar um mapa de uma cidade: cada nó representa um cruzamento e cada aresta uma rua (etiquetada com o respectivo comprimento). O objectivo deste problema é listar os cruzamentos de uma cidade por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto o número de ruas que interliga.  

A entrada consistirá numa sequência (não vazia) de nomes de ruas de uma única palavra, com no máximo 100 minúsculas. Os identificadores dos cruzamentos correspondem a uma letra do alfabeto, e cada rua começa (e acaba) no cruzamento identificado pelo primeiro (e último) caracter do respectivo nome. A saída deverá listar os nomes dos cruzamentos por ordem crescente de criticidade, listando cada linha um cruzamento e o número de ruas que interliga. Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo nível de criticidade deverão ser listados por ordem alfabética.  

**Exemplo de entrada:**  

raio  
central  
liberdade  
chaos  
saovictor  
saovicente  
saodomingos  
souto  
capelistas  
anjo  
taxa  

**Saída correspondente:**  

t 1  
a 2  
e 2  
l 2  
r 2  
c 3  
o 3  
s 6  