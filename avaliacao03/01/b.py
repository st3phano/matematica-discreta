'''
A(1) = 2
A(n) = A(n - 1) ** -1, para n >= 2
'''

def A(n):
   if (n == 1):
      return 2
   return A(n - 1) ** -1

for n in range(1, 11):
   print(f"A({n}) = {A(n)}")
