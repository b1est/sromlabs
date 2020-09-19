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

def LongAdd(a, b, c, carry = 0):
   n = len(a)
   for i in range(n - 1, -1, -1):
      if isinstance(a[i], str):
         n_A = int(a[i], 16)
      else:
         n_A = int(a[i])
      if isinstance(b[i], str):
         n_B = int(b[i], 16)
      else:
         n_B = int(b[i])
      temp = n_A + n_B + carry
      c =  Alphabet[temp % 16] + c
      carry = temp // 16
        
   return Alphabet[carry] + c
