def S(n):
   if (n == 1):
      return 2
   return S(n - 1) / 2

for n in range(1, 5):
   print(f"S({n}) = {S(n)}")
