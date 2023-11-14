'''
Forneça uma definição recursiva para todas as cadeias binárias (cadeias formadas com os
caracteres 0 e 1) contendo um número ímpar de zeros
'''

'''
0 ∈ C
Se X ∈ C, então 0X0 ∈ C e X1 ∈ C e 1X ∈ C
'''

def C(x):
   if (x == "0"):
      return True
   if (x == ""):
      return False

   if (x[0] == '0' and x[-1] == '0'):
      return C(x[1 : -1])
   if (x[-1] == '1'):
      return C(x[ : -1])
   if (x[0] == '1'):
      return C(x[1 : ])


cadeias = ["0", "01", "011", "0111", "1011", "00110", "101", "1011",
           "1101", "01010", "0010", "00101", "10010", "000100", "10",
           "101", "1011", "1101", "01010", "110", "1101", "1110", "01100",
           "0100", "01001", "10100", "001000", "000", "0001", "00011", "10001",
           "000010", "1000", "10001", "11000", "010000", "00000", "000001", "100000",
           "10000", "00100", "0101", "00", "0000001", "001100", "00100", "010", "001010"]

for x in cadeias:
   print(f"C({x}) = {C(x)}")
