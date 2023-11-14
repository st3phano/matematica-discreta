'''
S(1) = 10
S(n) = S(n - 1) + 10, para n >= 2
'''

def S(n):
   if (n == 1):
      return 10
   return S(n - 1) + 10

for n in range(1, 11):
   print(f"S({n}) = {S(n)}")
