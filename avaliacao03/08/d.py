'''
p, p - q, p + q, p - 2q, p + 2q, p - 3q, ...
'''

def S(p, q, n):
   if (n == 1):
      return p
   if (n == 2):
      return p - q
   if (n % 2 == 0):
      return S(p, q, n - 2) - q
   else:
      return S(p, q, n - 2) + q

for n in range(1, 11):
   print(f"S({n}) = {S(0, 1, n)}")
