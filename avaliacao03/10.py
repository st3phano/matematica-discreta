'''
Em um experimento, certa colônia de bactérias tem inicialmente uma população igual a
50.000. Uma leitura é feita a cada hora e, no final deste intervalo, há três vezes mais bactérias
que antes
'''

def A(n):
   if (n == 0):
      return 50000
   return A(n - 1) * 3

for n in range(0, 11):
   print(f"A({n}) = {A(n)}")
