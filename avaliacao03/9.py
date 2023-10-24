def T(n):
   if (n == 1):
      return 1
   if (n == 2):
      return 3
   return T(n - 1) + n

for n in range(1, 11):
   print(f"T({n}) = {T(n)}")
