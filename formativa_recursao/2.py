def exercicio_02(n: int) -> None:
   if (n >= 10):
      return
   print(n)
   exercicio_02(n + 1)

exercicio_02(0)
