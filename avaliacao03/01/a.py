def S(n):
   if (n == 1):
      return 10
   return S(n - 1) + 10

print(S(1))
print(S(10))
