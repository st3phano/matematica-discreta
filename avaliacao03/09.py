'''
Membros antigos da Sociedade de Pitágoras definiram números figurados como sendo o
número de pontos em uma certa configuração geométrica. Os primeiros números triangulares
são 1, 3, 6 e 10
'''

def T(n):
   if (n == 1):
      return 1
   return T(n - 1) + n

for n in range(1, 11):
   print(f"T({n}) = {T(n)}")
