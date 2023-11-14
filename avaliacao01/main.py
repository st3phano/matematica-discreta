'''
Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
operações que serão realizadas entre dois conjuntos de dados.
O programa que você desenvolverá irá receber como entrada do usuário vários conjuntos de
dados e várias operações. Estas operações e dados estarão representadas em um arquivo de textos
contendo apenas os dados referentes as operações que devem ser realizadas segundo a seguinte regra
fixa: a primeira linha do arquivo de texto de entrada conterá o número de operações que estão
descritas no arquivo, este número de operações será um inteiro; as linhas seguintes seguirão sempre o
mesmo padrão de três linhas: a primeira linha apresenta o código da operação (U para união, I para
interseção, D para diferença e C produto cartesiano), a segunda e terceira linhas conterão os elementos
dos conjuntos separados por virgulas. A seguir está um exemplo entradas que podem existir em um
teste para o programa que você irá desenvolver:
U
3, 5, 67, 7
1, 2, 3, 4
I
1, 2, 3, 4, 5
4, 5
D
1, A, C, 34
A, C, D, 23
C
3, 4, 5, 5, A, B, R
1, B, C, D, 1
Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
{𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
a informação e a formatação mostrada a seguir:
União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
contendo um número diferente de operações, operações com dados diferentes, e operações em ordem
diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no
ambiente repl.it quanto no ambiente Github.
Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com,
no mínimo um arquivo de testes criado pelo próprio professor.
'''

from leitura_arquivo import ler_conjunto, ler_operacao
from itertools import product

NOME_ARQUIVO_TESTE = "teste01.txt"
arquivo_teste = open(NOME_ARQUIVO_TESTE, "r")

numero_operacoes = int(arquivo_teste.readline())
for i in range(numero_operacoes):
   operacao = ler_operacao(arquivo_teste)

   SEPARADOR_ELEMENTOS = ','
   conjunto1 = ler_conjunto(arquivo_teste, SEPARADOR_ELEMENTOS)
   conjunto2 = ler_conjunto(arquivo_teste, SEPARADOR_ELEMENTOS)

   UNIAO = 'U'
   INTERSECAO = 'I'
   DIFERENCA = 'D'
   PRODUTO_CARTESIANO = 'C'
   operacao_valida = True
   if (operacao == UNIAO):
      conjunto_resultado = conjunto1 | conjunto2
      print("União", end="")
   elif (operacao == INTERSECAO):
      conjunto_resultado = conjunto1 & conjunto2
      print("Interseção", end="")
   elif (operacao == DIFERENCA):
      conjunto_resultado = conjunto1 - conjunto2
      print("Diferença", end="")
   elif (operacao == PRODUTO_CARTESIANO):
      conjunto_resultado = set(product(conjunto1, conjunto2))
      print("Produto cartesiano", end="")
   else:
      operacao_valida = False
      print("Operação inválida!")

   if (operacao_valida):
      print(f": conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {conjunto_resultado}")

arquivo_teste.close()
