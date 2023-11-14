'''
Escreva uma definição recursiva para uma progressão geométrica com termo inicial 'a' e razão 'r'
'''

def pg(a, r, n):
   if (n == 1):
      return a
   return pg(a, r, n - 1) * r

for n in range(1, 11):
   print(f"pg({1, 2, n}) = {pg(1, 2, n)}")
