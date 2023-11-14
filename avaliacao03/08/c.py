'''
a, b, a + b, a + 2b, 2a + 3b, ...
'''

def S(a, b, n):
   if (n == 1):
      return a
   if (n == 2):
      return b
   return S(a, b, n - 2) + S(a, b, n - 1)

for n in range(1, 11):
   print(f"S({n}) = {S(0, 1, n)}")
