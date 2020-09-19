Alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUV"
def convert32(num):
   if isinstance(num, str):
      n = int(num, 16)
   else:
      n = int(num)
   if n < 32:
      return Alphabet[n]
   else:
      return convert32(n // 32) +  Alphabet[n % 32]