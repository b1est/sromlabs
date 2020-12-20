import random 
from random import randrange 
import time
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

def comp(a, b):
   if len(a) > len(b):
      return 1
   elif len(a) < len(b):
      return 0
   else:
      for i in range(len(b)):
         if a[i] > b[i]:
            return 1
         if a[i] < b[i]:
            return 0
      return 1

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



   
def rshiftBin(tmp, k):
   if tmp is None:
      return tmp
   else:
      for i in range(0, k):
         del tmp[-i+1]
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
   
       
def BinConv(num, beta = 16):
   b = []
   num = conv(num, 2, beta)
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
   n2.reverse()
   n1.reverse()
   
   borrow = 0
   for i in range(len(n1)):
      if len(n2) > i:
         num = n2[i]
      temp = n1[i] - num - borrow
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
   while lcmp(r, b) == 1 or lcmp(r, b) == 0:
      t = len(r)
      c = sdth(b, t-k)
      if lcmp(r,c) == -1:
         t = t - 1
         c = sdth(b, t-k)
      
      r = sub(r, c)
      q = ins(q, t-k)
   return q, r

def rBinConv(num, beta):
   Num = ''
   if num == []:
      num.append(0)
   for i in num:
      Num = Num + str(i)
   num = conv(Num, beta, 2)
   return num

def diV(num1, num2):
   q, r = div(BinConv(num1), BinConv(num2))
   q = rBinConv(q, 16)
   r = conv(LongSub(conv(num1), LongMul(conv(num2), conv(q))), 16, 32)
  
   return [q, r]
def rev(n):
   for i in n:
      n.reverse()

def tests(A, B, C):
   test1(A, B, C)
   print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
   test2(A)

def test1(A, B, C):

   print("( A + B ) * C =", rlshift(conv(LongMul(rlshift(LongAdd(conv(A), conv(B))), conv(C)), 16, 32)))
   print("C * ( A + B ) =", rlshift(conv(LongMul(conv(C), rlshift(LongAdd(conv(A), conv(B)))), 16, 32)))
   print("A * C + B * C =", rlshift(conv(LongAdd(rlshift(LongMul(conv(C), conv(B))), rlshift(LongMul(conv(A), conv(C)))), 16, 32)))
   

def test2(A):
   n = random.randrange(101)
   print("n =", n)
   print("n * A =", rlshift(conv(LongMul(conv(A), conv(conv(str(n), 16, 10))), 16, 32)))
   d = conv(A)
   for i in range(n-1):
      d = LongAdd(conv(A), d)
   print("A + A + ... + A = ", rlshift(conv(d,16,32)))

def poW(A, B):
   print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
   pow1_time = time.time()
   print("A ^ B = " + conv(str(power1(conv(A), BinConv(B))), 16, 32) + "\n Время выполнения power1(): %s seconds" % (time.time() - pow1_time))
   pow2_time = time.time()
   print("A ^ B = " + conv(str(power2(conv(A), BinConv(B))), 16, 32) + "\n Время выполнения power2(): %s seconds" % (time.time() - pow2_time))
   print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
#LABA2

def gcd(a, b): 
   
   while lcmp(BinConv(a), BinConv(b)) == 1 or lcmp(BinConv(a), BinConv(b)) == -1:
      if lcmp(BinConv(a), BinConv(b)) == 1:
         a = LongSub(conv(a), conv(b))
         a = conv(a, 16, 32)
      else:
         b = LongSub(conv(b), conv(a))
         b = conv(b, 16, 32)      
   return a

def addBin(a, b):
   if len(b) > len(a):
      a, b = b, a
   res = []
   a.reverse()
   b.reverse()
   carry = 0
   for i in range(len(a)):
      tmp = 0
      if len(b) > i:
         tmp = b[i]
      temp = a[i] + tmp + carry
      res.append(temp % 2)
      carry = temp // 2
   if carry != 0:
      res.append(carry)
   res.reverse()
   return res

def mulOneDigitBin(bigNum, a):
   bigNum.reverse()
   carry = 0
   res = []
   for i in range(len(bigNum)):
      temp = carry + a * bigNum[i]  
      res.append(temp % 2)
      carry = temp // 2
   if carry != 0:
      res.append(carry)
   res.reverse()
   bigNum.reverse()
   return res

def mulBin(a, b):
   if len(b) > len(a):
      b, a = a, b
   res = []
   b.reverse()
   for i in range(len(b)):
      tmp = mulOneDigitBin(a, b[i])
      tmp = sdth(tmp, i)

      res = addBin(tmp, res)
   a.reverse()
   b.reverse()
   return res



def lcm(a, b):
   if lcmp(BinConv(a), BinConv(b)) == -1:
      d = a
      a = b
      b = d    
   gcD = gcd(a, b)
   
   a = diV(a, gcD)[0]
   
   res = LongMul(conv(b), conv(a))
   
   return conv(res, 16, 32)



def barret(x, n, m):
   
   if len(x) != 2 * len(n) + 1:
      return div(x,n)[1]
   else:
      q = rshiftBin(x, len(n) - 1)
      q = mulBin(q, m) 
      q = rshiftBin(q, len(n) + 1)
      r = sub(x, mulBin(q, n))
      while comp(r, n) == 1:
         r = sub(r, n) 
      if r == []:
         return [0]
      return r
   

  
def addMod(a = 'd852d3a2099fa0ef4'.upper(), b ='047A091AC46AFE31'.upper(), n = '047A091AC46CBE30'.upper()):
   summ = conv(LongAdd(conv(a), conv(b)), 10, 32)
   mu = BinConv(conv(str(2**(2*len(summ))), 16, 10))
   summ = BinConv(summ, 10)
   mu = div(mu, BinConv(n))[0]
   n = BinConv(n)
   Barret = rBinConv(barret(summ, n, mu), 16)
   return Barret

   
def subMod(a = 'd852d3a2099fa0ef4'.upper(), b ='047A091AC46AFE31'.upper(), n = '047A091AC46CBE30'.upper()):
   sub = conv(LongSub(conv(a), conv(b)), 10, 32)
   mu = BinConv(conv(str(2**(2*len(sub))), 16, 10))
   sub = BinConv(sub, 10)
   mu = div(mu, BinConv(n))[0]
   n = BinConv(n)
   Barret = rBinConv(barret(sub, n, mu), 16)
   return Barret

def mulMod(a = '47a091ac'.upper(), b ='d852d3a2'.upper(), n = '047A091AC46CBE30'.upper()):
   mul = conv(LongMul(conv(a), conv(b)), 10, 32)
   mu = BinConv(conv(str(2**(2*len(mul))), 16, 10))
   mul = BinConv(mul, 10)
   mu = div(mu, BinConv(n))[0]
   n = BinConv(n)
   Barret = rBinConv(barret(mul, n, mu), 16)
   return Barret
   

def powMod():
   a = '1EAEDD'
   b = '3'.upper()
   n = '47a091ac'.upper()
   a = BinConv(a)
   b = BinConv(b)
   n = BinConv(n)
   return gorner(a, b, n)

def test11(): 
    
    a = "1EAEDD395588036066915AF60F3F84502967BD8617DC"
    b = "1253FBED85830A10694A33E1C0DF38E62C8F6B2575B1"
    c = "1253FBEF85830A10694A33E1C0DF38E62C8F6B2575B1"
    n = "247A"


    add = addBin(BinConv(a), BinConv(b))
    
    m1 = mulMod(rBinConv(add, 16), c, n)
    m2 = mulMod(c, rBinConv(add, 16) , n)

    num1 = mulBin(BinConv(a), BinConv(c))
    num2 = mulBin(BinConv(b), BinConv(c))
    resAdd = addMod(rBinConv(num1, 16), rBinConv(num2, 16), n)

    if m1 == m2 or m1 == resAdd:
        print("Yes -3")
    else:
        print("Nu ne polyshilos")

def test22(): 
    
    n1 =  "1E"
    n2 =  "12"
    mod = "A"


    numNa = mulMod(n1, n2, mod)
    
    tmp = '0'
    
    for i in range(len(str(int(n1, 16)))):
        tmp = addMod(tmp, n2, mod)
    
    if tmp == numNa:
        print("Yes -3")
    else:
        print("Nu ne polyshilos")


def ArithmeticMod():
   s = time.time()
   add = addMod()
   print(add + "\nTime: "+ str(time.time()- s) + " seconds")
   s = time.time()
   sub = subMod()
   print(sub + "\nTime: "+ str(time.time()- s) + " seconds")
   s = time.time()
   mul = mulMod()
   print(mul+ "\nTime: "+ str(time.time()- s) + " seconds")
   s = time.time()
   p = rBinConv(powMod(), 16)
   print(p + "\nTime: "+ str(time.time()- s) + " seconds" )
   
def stb(s):
    tmp = []
    for i in range(len(s)):
        tmp.append(int(s[i]))
    return tmp

def bts(b): 
    binary = ''
    for i in b:
        binary = binary + str(i)
    if binary == '' or binary == None:
        return '0'
    else:
        return binary

   
def gorner(a, b, n):
   c = [1]
   mu = div(sdth([1], 2**len(n)), n)[0]
   b.reverse()
   for i in b:
      if i == 1:
         c = barret(mulBin(c.copy(), a.copy()), n, mu)
      a = barret(mulBin(a.copy(), a.copy()), n, mu)
   return c