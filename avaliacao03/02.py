def pg(a, r, n):
   if (n == 1):
      return a
   return pg(a, r, n - 1) * r

print(pg(2, 2, 1))
print(pg(2, 2, 8))
