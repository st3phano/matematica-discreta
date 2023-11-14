'''
1, 3, 9, 27, ...
'''

def S(n):
   if (n == 1):
      return 1
   return S(n - 1) * 3

for n in range(1, 5):
   print(f"S({n}) = {S(n)}")
