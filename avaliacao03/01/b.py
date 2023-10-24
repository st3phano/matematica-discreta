def A(n):
   if (n == 1):
      return 2
   return A(n - 1) ** -1

print(A(1))
print(A(10))
