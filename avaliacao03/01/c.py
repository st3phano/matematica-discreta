def B(n):
   if (n == 1):
      return 1
   return B(n - 1) + n ** 2

print(B(1))
print(B(10))
