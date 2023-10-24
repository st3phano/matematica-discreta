def D(n):
   if (n == 1):
      return 3
   if (n == 2):
      return 5
   return (n - 1) * D(n - 1) + (n - 2) * D(n - 2)

print(D(1))
print(D(2))
print(D(10))
