def T(n):
   if (n == 1):
      return 1
   if (n == 2):
      return 2
   if (n == 3):
      return 3
   return T(n - 1) + 2 * T(n - 2) + 3 * T(n - 3)

print(T(1))
print(T(2))
print(T(3))
print(T(10))
