def P(n):
   if (n == 1):
      return 1
   return n ** 2 * P(n - 1) + n - 1

print(P(1))
print(P(10))
