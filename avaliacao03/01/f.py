def W(n):
   if (n == 1):
      return 2
   if (n == 2):
      return 5
   return W(n - 1) * W(n - 2)

print(W(1))
print(W(2))
print(W(10))
