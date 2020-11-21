import random 
from random import randrange 
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

def LongAdd(a, b,  c = '',  carry = 0):
   n = len(a)
   m = len(b)
   if n > m:
      i = n - m
      b = lshift(b, i)
   if n < m:
      i = m - n
      a = lshift(a, i)
      n = m
   for i in range(n - 1, -1, -1):
      if isinstance(a[i], str):
         n_A = int(a[i], 32)
      else:
         n_A = int(a[i])
      if isinstance(b[i], str):
         n_B = int(b[i], 32)
      else:
         n_B = int(b[i])
      temp = n_A + n_B + carry
      c =  Alphabet[temp % 32] + c
      carry = temp // 32    
   return Alphabet[carry] + c

def LongSub(a, b, c = '', borrow = 0):
   n = len(a)
   m = len(b)
   if n > m:
      i = n - m
      b = lshift(b, i)
   if n < m:
      i = m - n
      a = lshift(a, i)
      n = m
   for i in range(n-1, -1,-1):
      if isinstance(a[i], str):
         n_A = int(a[i], 32)
      else:
         n_A = int(a[i])
      if isinstance(b[i], str):
         n_B = int(b[i], 32)
      else:
         n_B = int(b[i])
      temp = n_A - n_B - borrow 
      if temp >= 0:
         c =  Alphabet[temp % 32] + c
         borrow = 0
      else:
         c = Alphabet[(32 + temp) % 32] + c
         borrow = 1     
   return Alphabet[borrow] + c

def LongMulOneDigit (a, b, c = ''):
   carry = 0
   n = len(a)
   if isinstance(b, str):
      n_b = int(b, 32)
   else:
      n_b = int(b)
   for i in range(n-1, -1,-1):
      if isinstance(a[i], str):
         n_A = int(a[i], 32)
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

def lshift(tmp, k):
   for i in range(k):
      tmp = '0' + tmp
   return tmp

def rlshift(tmp):
   k = 0
   if tmp[0] == '0':
      for i in range(len(tmp)):
         if tmp[i] == '0' and tmp[i + 1] == '0':
            k += 1
         else:
            tmp = tmp[k+1::]
            break
   return tmp


def LongMul(a, b, c = ''):
   n = len(a)
   m = len(b)
   if n > m:
      i = n - m
      b = lshift(b, i)
   if n < m:
      i = m - n
      a = lshift(a, i)
      n = m
   for i in range(n-1, -1,-1):
      tmp = LongMulOneDigit(a, b[i], '')     
      k = abs(i - n + 1)
      tmp = shift(tmp, k)
      if i == n - 1:
         c = tmp 
      else:
         if len(c) < len(tmp):
            c = '0' + c

         c = LongAdd( c, tmp, '')      
   return c

def power1(a, b):
   res = '1'
   b.reverse()
   for i in b:
      if i == 1:
         res = rlshift(LongMul(res, a))
      a = rlshift(LongMul(a, a))
   return res

def power2(a, b):
   res = '1'
   for i in range(len(b)):
      if b[i] == 1:  
         res = rlshift(LongMul(res, a))  
      if i != len(b) - 1:   
         res = rlshift(LongMul(res, res))
   return res

def convf(a):
   b = []
   for i in range(0, len(a), 8):
      b.append(int(a[i:i+8], 16)) 
   return b
def rconvf(a):
   b = []
   k = ''
   c = ''
   if len(a) == 0:
      return 0
   else:
      for i in a:
	      k = str(hex(i))
	      k = k[2::].upper()
	      b.append(k)
   for i in b:
      c = c + i
   return c

def lcmp(a, b):
   if len(a) > len(b):
      return 1
   elif len(a) < len(b):
      return -1
   else:
      for i in range(len(b)):
         if a[i] > b[i]:
            return 1
         if a[i] < b[i]:
            return -1
      return 0 
       
def BinConv(num):
   b = []
   num = conv(num, 2)
   for i in num:
      b.append(int(i))
   d = b.copy()
   return d

def sdth(n, i):
    N = n.copy()
    for i in range(i):
        N.append(0)
    return N

def ins(n, i):
   N = n.copy()
   if len(N) > i:
      N.reverse()
      N[i] = 1
      N.reverse()
   else:
      N.append(1)
      N = sdth(N, i)
   return N

def sub(n1, n2):
   res = []
   rev([n1, n2])
   borrow = 0
   for i in range(len(n1)):
      if len(n2) > i:
         num2 = n2[i]
      temp = n1[i] - num2 - borrow
      if temp >= 0:
         res.append(temp)
         borrow = 0
      else:
         res.append(temp + 2)
         borrow = 1
   res.reverse()
   while(len(res) != 0):
      if res[0] == 0:
         del res[0]
      else:
         break
   return res

def div(a, b):
   k = len(b)
   r = a
   q = []
   while lcmp(r, b) == 1 or lcmp(r, b) == 1 :
      t = len(r)
      c = sdth(b, t-k)
      if lcmp(r,c) == -1:
         t -= 1
         c = sdth(b, t-k)
      r = sub(r, c)
      q = ins(q, t-k)
   return q, r

def diV(num1, num2):
   q, r = div(BinConv(num1), BinConv(num2))
   Q = ''
   R = ''
   for i in q:
      Q = Q + str(i)
   for j in r:
      R = R + str(j)
   q = conv(Q, 16, 2)
   r = conv(R, 16, 2)
   print(q, r)
def rev(n):
   for i in n:
      n.reverse()

def tests():
   test1()
   test2()

def test1():
   A = '170076B15F9575D21DE39D5C429799BBCDDB867016DE2248E3CFDE73A4D70C8636A9E41ABE671E7B9FB4739A5FF64DF9D0D3A64E0C9B20BFE58F1C62B28477EE9FD202010BAC440ADF3CA016A32DB844F23DEC2AB93AE869A6262FC23C5CE419807CDBA930A5433884E3B34B22477289BD3A7712CDD4B4110BD9887E7428FDF7'
   B = '09D1C2D6E1591932F73C2F499C4E0A2E252DE828CDA7842CE0972C4101FE772B56C45C475EDDEDAEC2DBD13E375E02D2C149B69AB51FF3F94533CA34A815484EC86DACE936BDC62B5F3F9EB6F5BE6BD253E256181D35D7D63EE24459824D462C53676E3DFF98700415ADA65FDA7CBD3B3F359C817F52BEDA70C9DD85F68473C6'
   c = '20D2398840EE8F05151FCCA5DEE5A3E9F3096E98E485A675C4670AB4A6D583B18D6E40621D450C2A629044D8975450CC921D5CE8C1BB14B92AC2E6975A99C03D683FAEEA426A0A363E7C3ECD98EC241746204242D670C03FE508741BBEAA2A45D3E449E7303DB33C9A9159AAFCC42FC4FC7013944D2772EB7CA366046AAD71BD'
   a = conv(A)
   b = conv(B)
   c = conv(c)
   AsumB = LongAdd(a, b)
   AsumB = AsumB[1::]
   res1 = LongMul(AsumB, c)
   res2 = LongMul(c, AsumB)
   l = LongMul(a, c)
   m = LongMul(c, b)
   res3 = LongAdd(m, l)
   res1 = res1[2::]
   res2 = res2[2::]
   res3 = res3[3::]
   res1 = conv(res1, 16, 32)
   res2 = conv(res2, 16, 32)
   res3 = conv(res3, 16, 32)
   print("( a + b ) * c =", res1)
   print("c * ( a + b ) =", res2)
   print("a * c + b * c =", res3)
   

def test2():
   A = '170076B15F9575D21DE39D5C429799BBCDDB867016DE2248E3CFDE73A4D70C8636A9E41ABE671E7B9FB4739A5FF64DF9D0D3A64E0C9B20BFE58F1C62B28477EE9FD202010BAC440ADF3CA016A32DB844F23DEC2AB93AE869A6262FC23C5CE419807CDBA930A5433884E3B34B22477289BD3A7712CDD4B4110BD9887E7428FDF7'

   n = random.randrange(101)
   N = n
   print("n =", n)
   n = str(hex(n))
   n = n[2::]
   n = conv(n)
   A = conv(A)
   res1 = conv(LongMul(A, n), 16, 32)

   d = A

   for i in range(N-1):
      d = LongAdd(A, d)
   res2 = conv(d,16,32)

   print("n*A =", res1)
   print("A+A+...+A=", res2)