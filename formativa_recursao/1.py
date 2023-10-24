def exercicio_01(n: int) -> int:
   if (n < 2):
      return 1
   return exercicio_01(n - 1) + 3

print(exercicio_01(5))
