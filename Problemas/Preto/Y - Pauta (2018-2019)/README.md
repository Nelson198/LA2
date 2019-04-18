# Descrição do problema Y : Pauta

Neste problema deve apresentar a pauta com a avaliação dos alunos de uma disciplina. Para tal irá receber a lista de alunos inscritos na disciplina (formato "[Num] [Nome]"), e a notas do exame (formato "[Num] [Nota]"). Como resultado deverá apresentar a listagem de todos os alunos (formato "[Num] [Nome] : [Nota]"), ordenada pelo nome, e em que a nota deverá ser alternativamente a letra "F" (faltou ao exame), a letra "R" (reprovado) ou a nota do exame arredondada às unidades (aprovado).

O formato dos dados de entrada é um conjunto de linhas contendo o número e nome dos alunos inscritos separados por um espaço, seguido de uma linha contendo unicamente o carácter -, seguido por último de um conjunto de linhas contendo número e nota do exame separados por espaço. Pode assumir que só poderá aparecer uma nota por número, e que todas as notas correspondem a alunos inscritos.

Exemplo de entrada:  

11111 Jose Oliveira  
22222 Francisco Pinto  
33333 Manuel Pereira  
\-  
33333 12.3  
22222 8.2  

Saída correspondente:  

22222 Francisco Pinto : R  
11111 Jose Oliveira : F  
33333 Manuel Pereira : 12