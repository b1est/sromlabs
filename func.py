Alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def conv(num, to = 32, froM = 16):
    if isinstance(num, str):
         n = int(num, froM)
    else:
        n = int(num)
    if n < to:
        return Alphabet[n]
    else:
        return conv(n // to, to) + Alphabet[n % to]

def LongAdd(a, b,  c = '' , w = 32,  carry = 0):
   n = len(a)
   m = len(b)
   if n > m:
      i = n - m
      b = lshift(b, i)
   if n < m:
      i = m - n
      a = lshift(a, i)
   for i in range(n - 1, -1, -1):
      if isinstance(a[i], str):
         n_A = int(a[i], w)
      else:
         n_A = int(a[i])
      if isinstance(b[i], str):
         n_B = int(b[i], w)
      else:
         n_B = int(b[i])
      temp = n_A + n_B + carry
      c =  Alphabet[temp % 32] + c
      carry = temp // 32    
   return Alphabet[carry] + c

def LongAddDv(a, b,  c = '' ,  carry = 0):
   n = len(a)
   for i in range(n - 1, -1, -1):
      if isinstance(a[i], str):
         n_A = int(a[i], 2)
      else:
         n_A = int(a[i])
      if isinstance(b[i], str):
         n_B = int(b[i], 2)
      else:
         n_B = int(b[i])
      temp = n_A + n_B + carry
      c =  Alphabet[temp % 2] + c
      carry = temp // 2    
   return Alphabet[carry] + c




def LongSub(a, b, c = '', w = 32, borrow = 0):
   n = len(a)
   m = len(b)
   if n > m:
      i = n - m
      b = lshift(b, i)
   if n < m:
      i = m - n
      a = lshift(a, i)
   for i in range(n-1, -1,-1):
      if isinstance(a[i], str):
         n_A = int(a[i], w)
      else:
         n_A = int(a[i])
      if isinstance(b[i], str):
         n_B = int(b[i], w)
      else:
         n_B = int(b[i])
      temp = n_A - n_B - borrow 
      if temp >= 0:
         c =  Alphabet[temp % 32] + c
         borrow = 0
      else:
         c = Alphabet[(w + temp) % 32] + c
         borrow = 1     
   return Alphabet[borrow] + c

def LongMulOneDigit (a, b, c = '', w = 32):
   carry = 0
   n = len(a)
   if isinstance(b, str):
      n_b = int(b, w)
   else:
      n_b = int(b)
   for i in range(n-1, -1,-1):
      if isinstance(a[i], str):
         n_A = int(a[i], w)
      else:
         n_A = int(a[i])
      temp = n_A * n_b + carry
      c =  Alphabet[temp % 32] + c
      carry = temp // 32
   if carry == 0:
      return c
   else:
      c = Alphabet[carry] + c
      return c

def shift(temp, i):
   for j in range(i):
      temp = temp + '0'
   return temp

def LongMulOneDigitDv (a, b, c = ''):
   carry = 0
   n = len(a)
   if isinstance(b, str):
      n_b = int(b, 2)
   else:
      n_b = int(b)
   for i in range(n-1, -1,-1):
      if isinstance(a[i], str):
         n_A = int(a[i], 2)
      else:
         n_A = int(a[i])
      temp = n_A * n_b + carry
      c =  Alphabet[temp % 2] + c
      carry = temp // 2
   if carry == 0:
      return c
   else:
      c = Alphabet[carry] + c
      return c
def lshift(tmp, k):
   for i in range(k):
      tmp = '0' + tmp
   return tmp
def LongMulDv(a, b, c = ''):
   n = len(a)
   for i in range(n-1, -1,-1):
      tmp = LongMulOneDigitDv(a, b[i], '')     
      k = abs(i - n + 1)
      tmp = shift(tmp, k)
      if i == n - 1:
         c = tmp 
      else:
         if len(c) < len(tmp):
            c = '0' + c

         c = LongAddDv( c, tmp, '')
         
   return c
def LongMul(a, b, c = '', w = 32):
   n = len(a)
   m = len(b)
   if n > m:
      i = n - m
      b = lshift(b, i)
   if n < m:
      i = m - n
      a = lshift(a, i)
   for i in range(n-1, -1,-1):
      tmp = LongMulOneDigit(a, b[i], '', w)     
      k = abs(i - n + 1)
      tmp = shift(tmp, k)
      if i == n - 1:
         c = tmp 
      else:
         if len(c) < len(tmp):
            c = '0' + c

         c = LongAdd( c, tmp, '', w)
         
   return c

def LongShiftBitsToHigh(b, n):   
   of_int = n // 32
   bit = n % 32
   if bit == 0:
      return shift(b, of_int)
   of_bit_2 = 32 - bit
   high_bit = b[len(b) - 1] >> of_bit_2
   if high_bit != 0:
      k = 1 
   else: 
      k = 0
   big = len(b) + of_int + k
   i = len(big) - 1
   if high_bit != 0:
      i = i - 1
      big[i] = high_bit
   j = len(b) - 1
   while j > 0:
      j = j - 1
      t = b[j] << bit
      i = i - 1
      j = j - 1
      big[i] = t | b[j] >> of_bit_2
   big[i] = b[j] << bit
   return big

def LongDivMod (a, b):
   res = []
   k1 = a[len(b)-1]
   if isinstance(k1, str):
      k1 = int(k1, 32)
   else:
      k1 = int(k1)
   k = (len(b)-1 * 32) + k1.bit_length()
   r = a
   q = 0
   r2 = conv(r, 10, 32)
   b2 = conv(b, 10, 32)
   while r2 >= b2: 
      r1 = r[len(r)-1]
      if isinstance(r1, str):
         r1 = int(r1, 32)
      else:
         r1 = int(r1)
      t = (len(r)-1 * 32) + r1.bit_length()
      c = LongShiftBitsToHigh(b, t - k)
      b2 = conv(b, 10, 32)
      if r < c: 
         t = t - 1
         c = LongShiftBitsToHigh(b, t - k)
         b2 = conv(b, 10, 32)

      r = LongSub(r, c, '', 32)
      r2 = conv(r, 10, 32)
      q = q + 2**(t - k)
   q = conv(q, 32, 16)
   r = conv(r, 32, 16)
   res.append(q)
   res.append(r)
   return res

def rev(s):
    return s[::-1]
def LongPower (a, b, c = '1'): 
   b = rev(b)
   for i in b:
      print('It works!' )
      if i == '1':
         c =  LongMulDv(c, a, '') 
      a = LongMulDv(a, a, '')
   return c
   