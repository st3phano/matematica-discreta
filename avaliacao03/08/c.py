def S(n):
   if (n == 1):
      return "a"
   if (n == 2):
      return "b"
   return S(n - 2) + S(n - 1)

for n in range(1, 6):
   print(f"S({n}) = {S(n)}")
